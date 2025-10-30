
import { readFile, writeFile } from 'node:fs/promises';
import { pathToFileURL } from 'node:url';

const POKEAPI_BASE = 'https://pokeapi.co/api/v2/pokemon/';

/** Read names from a file (one per line), trimming and skipping blanks. */
export async function readTopList(filePath = 'top5pokemon') {
  const raw = await readFile(filePath, 'utf8');
  return raw
    .split('\n')
    .map(s => s.trim())
    .filter(Boolean);
}

/** Fetch a single Pokémon by name (case-insensitive); returns { name, base_experience }. */
export async function fetchPokemonByName(name) {
  const url = `${POKEAPI_BASE}${encodeURIComponent(name.toLowerCase())}`;
  const res = await fetch(url, { redirect: 'follow' });
  if (!res.ok) {
    throw new Error(`Failed to fetch ${name}: ${res.status} ${res.statusText}`);
  }
  const json = await res.json();
  // Use the input name for output formatting to preserve any provided casing
  return { name, base_experience: json.base_experience };
}

/** Build sorted mapping and write to output file. */
export async function buildBestPokemon(
  inputPath = 'top5pokemon',
  outputPath = 'bestpokemon'
) {
  const names = await readTopList(inputPath);

  const results = await Promise.all(
    names.map(async (n) => {
      const p = await fetchPokemonByName(n);
      return p;
    })
  );

  // Sort descending by base_experience
  results.sort((a, b) => b.base_experience - a.base_experience);

  // Format:
  // name: base_experience
  const lines = results.map(r => `${r.name}: ${r.base_experience}`).join('\n') + '\n';
  await writeFile(outputPath, lines, 'utf8');

  return results; // returned for convenience/testing
}

// CLI usage: node Due_28_Oct/bestPokemonBuilder.js [inputPath] [outputPath]
if (import.meta.url === pathToFileURL(process.argv[1]).href) {
  (async () => {
    try {
      const input = process.argv[2] || 'top5pokemon';
      const output = process.argv[3] || 'bestpokemon';
      await buildBestPokemon(input, output);
      // Print object format as a courtesy
      const data = await readFile(output, 'utf8');
      console.log(data.trim());
    } catch (err) {
      console.error('Error:', err?.message || String(err));
      process.exitCode = 1;
    }
  })();
}
