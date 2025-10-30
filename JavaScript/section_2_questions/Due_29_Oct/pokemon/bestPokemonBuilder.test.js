// Due_29_Oct/pokemon/bestPokemonBuilder.test.js
import { jest } from '@jest/globals';

// Mock fs/promises BEFORE importing the module under test
const mockFs = {
  readFile: jest.fn(),
  writeFile: jest.fn(),
};
jest.unstable_mockModule('node:fs/promises', () => mockFs);

describe('bestPokemonBuilder', () => {
  beforeEach(() => {
    jest.resetModules(); // reset ESM module registry for fresh imports
    jest.restoreAllMocks();
    mockFs.readFile.mockReset();
    mockFs.writeFile.mockReset();
  });

  test('readTopList parses names, trims, and skips blanks', async () => {
    // Arrange fs mock
    const INPUT = 'charizard\n  mewtwo \n\npikachu\r\neevee\n  arceus  ';
    mockFs.readFile.mockResolvedValue(INPUT);

    // Import AFTER mocks are set
    const { readTopList } = await import('./bestPokemonBuilder.js');

    // Act
    const names = await readTopList('top5pokemon');

    // Assert
    expect(names).toEqual(['charizard', 'mewtwo', 'pikachu', 'eevee', 'arceus']);
    expect(mockFs.readFile).toHaveBeenCalledWith('top5pokemon', 'utf8');
  });

  test('fetchPokemonByName hits PokeAPI with lowercased name and returns base_experience', async () => {
    // Import (fs won’t be used here, but import still respects the mock)
    const { fetchPokemonByName } = await import('./bestPokemonBuilder.js');

    // Mock fetch
    const fetchSpy = jest.spyOn(global, 'fetch').mockResolvedValue({
      ok: true,
      json: async () => ({ base_experience: 340 }),
      status: 200,
      statusText: 'OK',
    });

    const p = await fetchPokemonByName('MewTwo'); // mixed case input
    expect(p).toEqual({ name: 'MewTwo', base_experience: 340 });
    expect(fetchSpy).toHaveBeenCalledWith(
      'https://pokeapi.co/api/v2/pokemon/mewtwo',
      { redirect: 'follow' }
    );
  });

  test('buildBestPokemon sorts by base_experience desc and writes output', async () => {
    // Arrange fs mocks
    mockFs.readFile.mockResolvedValue(
      'charizard\nmewtwo\npikachu\narceus\neevee\n'
    );
    mockFs.writeFile.mockResolvedValue(undefined);

    // Mock fetch per Pokémon
    const baseMap = {
      charizard: 267,
      mewtwo: 340,
      pikachu: 112,
      arceus: 324,
      eevee: 65,
    };
    jest.spyOn(global, 'fetch').mockImplementation(async (url) => {
      const name = url.split('/').filter(Boolean).pop();
      const be = baseMap[name];
      if (be == null) {
        return { ok: false, status: 404, statusText: 'Not Found' };
      }
      return {
        ok: true,
        json: async () => ({ base_experience: be }),
        status: 200,
        statusText: 'OK',
      };
    });

    // Import AFTER mocks
    const { buildBestPokemon } = await import('./bestPokemonBuilder.js');

    // Act
    const results = await buildBestPokemon('top5pokemon', 'bestpokemon');

    // Assert: order is mewtwo, arceus, charizard, pikachu, eevee
    expect(results.map(r => r.name)).toEqual(['mewtwo', 'arceus', 'charizard', 'pikachu', 'eevee']);

    const expectedOut =
      'mewtwo: 340\n' +
      'arceus: 324\n' +
      'charizard: 267\n' +
      'pikachu: 112\n' +
      'eevee: 65\n';

    expect(mockFs.writeFile).toHaveBeenCalledWith('bestpokemon', expectedOut, 'utf8');
  });
});
