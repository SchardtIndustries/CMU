
import { readFile, writeFile } from 'node:fs/promises';
import { pathToFileURL } from 'node:url';

/** Read newline-delimited names, trimming whitespace and skipping blank lines. */
export async function readNames(filePath) {
  const raw = await readFile(filePath, 'utf8');
  return raw
    .split('\n')
    .map(s => s.trim())
    .filter(Boolean);
}

/** Compute { adds, drops } given arrays of names. */
export function diffStudents(beforeNames, afterNames) {
  const beforeSet = new Set(beforeNames);
  const afterSet = new Set(afterNames);

  const drops = [];
  for (const name of beforeSet) {
    if (!afterSet.has(name)) drops.push(name);
  }

  const adds = [];
  for (const name of afterSet) {
    if (!beforeSet.has(name)) adds.push(name);
  }

  // Sort for deterministic results
  adds.sort((a, b) => a.localeCompare(b));
  drops.sort((a, b) => a.localeCompare(b));
  return { adds, drops };
}

/**
 * Orchestrates reading before/after files, computing diff,
 * and writing "adds" and "drops" files.
 */
export async function buildAddsAndDrops({
  beforePath = 'before',
  afterPath = 'after',
  addsPath = 'adds',
  dropsPath = 'drops',
} = {}) {
  const [beforeNames, afterNames] = await Promise.all([
    readNames(beforePath),
    readNames(afterPath),
  ]);

  const { adds, drops } = diffStudents(beforeNames, afterNames);

  const addsOut = adds.join('\n') + (adds.length ? '\n' : '');
  const dropsOut = drops.join('\n') + (drops.length ? '\n' : '');

  await Promise.all([
    writeFile(addsPath, addsOut, 'utf8'),
    writeFile(dropsPath, dropsOut, 'utf8'),
  ]);

  return { adds, drops };
}

// CLI: node Due_29_Oct/students/diffRoster.js [before] [after] [adds] [drops]
if (import.meta.url === pathToFileURL(process.argv[1]).href) {
  (async () => {
    try {
      const beforePath = process.argv[2] || 'before';
      const afterPath = process.argv[3] || 'after';
      const addsPath = process.argv[4] || 'adds';
      const dropsPath = process.argv[5] || 'drops';
      const { adds, drops } = await buildAddsAndDrops({ beforePath, afterPath, addsPath, dropsPath });
      console.log('adds:\n' + adds.join('\n'));
      console.log('drops:\n' + drops.join('\n'));
    } catch (err) {
      console.error('Error:', err?.message || String(err));
      process.exitCode = 1;
    }
  })();
}
