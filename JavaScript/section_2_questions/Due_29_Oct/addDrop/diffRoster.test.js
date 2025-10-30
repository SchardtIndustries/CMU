
import { jest } from '@jest/globals';

// Mock fs/promises BEFORE importing the module under test
const mockFs = {
  readFile: jest.fn(),
  writeFile: jest.fn(),
};
jest.unstable_mockModule('node:fs/promises', () => mockFs);

describe('diffRoster', () => {
  beforeEach(() => {
    jest.resetModules();
    jest.restoreAllMocks();
    mockFs.readFile.mockReset();
    mockFs.writeFile.mockReset();
  });

  test('diffStudents computes adds and drops (pure function)', async () => {
    const { diffStudents } = await import('./diffRoster.js');

    const before = ['A', 'B', 'C'];
    const after = ['B', 'C', 'D', 'E'];
    const { adds, drops } = diffStudents(before, after);

    expect(adds).toEqual(['D', 'E']);
    expect(drops).toEqual(['A']);
  });

  test('buildAddsAndDrops reads files, writes adds and drops correctly (your data)', async () => {
    // Provided file contents (exactly as in the assignment)
    const BEFORE = `Guillermo Cormier
Florence Becker
Ms. Tasha DuBuque
Ricardo Carter
Dr. Louis Paucek
Diane Keeling
Kendra Batz
Levi Spinka
Tracy Ruecker
Gerald Beier
Irene McGlynn
Beatrice Stroman
Edna Rutherford
Edmund Schuppe
Latoya Treutel
Marc Stiedemann
Roy Batz
Dr. Wendell Swaniawski
Harvey Greenholt Jr.
Warren Rogahn
Marco Lynch
Ernestine Skiles
Mrs. Alexandra Pollich
Meghan Harris
Jacquelyn Kuvalis
Lynda Tremblay
Dustin Schmitt
Henrietta Wolff
Mr. Walter Yundt
Cary Spinka IV
Dr. Kelvin Bins
Paul Hartmann
`;

    const AFTER = `Meghan Harris
Marc Stiedemann
Levi Spinka
Ricardo Carter
Diane Keeling
Ernestine Skiles
Harvey Greenholt Jr.
Warren Rogahn
Jacquelyn Kuvalis
Roy Batz
Stewart Bradtke I
Tracy Ruecker
Mrs. Alexandra Pollich
Dixie Klocko
Dr. Louis Paucek
Beatrice Stroman
Florence Becker
Kendra Batz
Dr. Wendell Swaniawski
Edmund Schuppe
Dustin Schmitt
Paul Hartmann
Gerald Beier
Dr. Kelvin Bins
Marco Lynch
Henrietta Wolff
Latoya Treutel
Marco Hills
Edna Rutherford
Lynda Tremblay
`;

    // Order of readFile calls depends on our implementation; map by filename
    mockFs.readFile.mockImplementation(async (path, enc) => {
      if (path === 'before') return BEFORE;
      if (path === 'after') return AFTER;
      throw new Error('Unexpected read: ' + path);
    });
    mockFs.writeFile.mockResolvedValue(undefined);

    const { buildAddsAndDrops } = await import('./diffRoster.js');

    const res = await buildAddsAndDrops({
      beforePath: 'before',
      afterPath: 'after',
      addsPath: 'adds',
      dropsPath: 'drops',
    });

    // Deterministic sorted outputs
    expect(res.adds).toEqual([
      'Dixie Klocko',
      'Marco Hills',
      'Stewart Bradtke I',
    ]);

    expect(res.drops).toEqual([
      'Cary Spinka IV',
      'Guillermo Cormier',
      'Irene McGlynn',
      'Mr. Walter Yundt',
      'Ms. Tasha DuBuque',
    ]);

    // File writes (alphabetical, one per line, trailing newline)
    const expectedAdds =
      'Dixie Klocko\n' +
      'Marco Hills\n' +
      'Stewart Bradtke I\n';

    const expectedDrops =
      'Cary Spinka IV\n' +
      'Guillermo Cormier\n' +
      'Irene McGlynn\n' +
      'Mr. Walter Yundt\n' +
      'Ms. Tasha DuBuque\n';

    expect(mockFs.writeFile).toHaveBeenCalledWith('adds', expectedAdds, 'utf8');
    expect(mockFs.writeFile).toHaveBeenCalledWith('drops', expectedDrops, 'utf8');
  });
});
