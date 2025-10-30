/**
 * cli.js
 * 
 * Minimal interactive CLI for the tiny search engine.
 * Commands:
 *   :crawl <url> [maxPages=50] [maxDepth=2]
 *   :exit
 * Otherwise: treats input as a query and prints ranked results.
 */

const readline = require('readline');
const { createIndex } = require('./searchIndex');
const { search } = require('./searchAlgorithm');
const { rankSearchResults } = require('./ranking');
const docStore = require('./docStore');
const { crawl } = require('./spider');

const index = createIndex();

function printHelp() {
  console.log(`
Tiny Search Engine
Commands:
  :crawl <url> [maxPages] [maxDepth]    Crawl and index from a start URL
  :exit                                 Exit
  :help                                 Show this help

Type a query to search the in-memory index.
`);
}

async function handleCommand(line) {
  const parts = line.trim().split(/\s+/);
  const cmd = parts[0].toLowerCase();

  if (cmd === ':exit') {
    process.exit(0);
  }
  if (cmd === ':help') {
    printHelp();
    return;
  }
  if (cmd === ':crawl') {
    if (parts.length < 2) {
      console.log('Usage: :crawl <url> [maxPages] [maxDepth]');
      return;
    }
    const url = parts[1];
    const maxPages = Number(parts[2] || 50);
    const maxDepth = Number(parts[3] || 2);
    console.log(`Crawling ${url} (maxPages=${maxPages}, maxDepth=${maxDepth})...`);
    try {
      const res = await crawl(url, index, docStore, { maxPages, maxDepth });
      console.log(`Done. Pages crawled: ${res.pagesCrawled}`);
    } catch (e) {
      console.error('Crawl error:', e.message || e);
    }
    return;
  }

  // Default: treat as query
  const query = line.trim();
  if (!query) return;
  const urls = search(index, query);
  const ranked = rankSearchResults(index, query, urls, { docStore });

  if (ranked.length === 0) {
    console.log('No results.');
  } else {
    console.log(`Results for "${query}":`);
    for (let i = 0; i < Math.min(10, ranked.length); i++) {
      const u = ranked[i];
      const d = docStore.getDocument(u);
      const title = (d && d.title) ? d.title : u;
      console.log(`${i + 1}. ${title}\n   ${u}`);
    }
  }
}

async function main() {
  printHelp();
  const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout,
    prompt: '> '
  });

  rl.prompt();
  rl.on('line', async (line) => {
    try {
      await handleCommand(line);
    } catch (e) {
      console.error('Error:', e.message || e);
    }
    rl.prompt();
  }).on('close', () => {
    process.exit(0);
  });
}

if (require.main === module) {
  main();
}

module.exports = { main };
