/**
 * spider.js
 * 
 * A polite, tiny crawler that:
 *  - crawls from a start URL (BFS)
 *  - respects robots.txt Disallow (basic)
 *  - normalizes links and enforces same-origin if configured
 *  - indexes pages into searchIndex + docStore
 * 
 * Uses only built-in 'https/http' to avoid extra deps; if 'cheerio' is present,
 * doc extraction quality improves automatically via docStore's defaultExtractor.
 */

const http = require('http');
const https = require('https');
const { URL } = require('url');
const { addPageToIndex } = require('./searchIndex');
const docStore = require('./docStore');

/**
 * @typedef {Object} CrawlOptions
 * @property {number} [maxPages=50]
 * @property {number} [maxDepth=2]
 * @property {boolean} [sameOriginOnly=true]
 * @property {number} [delayMs=150]  polite delay between requests
 */

function sleep(ms) { return new Promise(res => setTimeout(res, ms)); }

/**
 * Basic robots cache per origin.
 * Map<origin, {disallow: string[]}>
 */
const robotsCache = new Map();

async function fetchRobots(u) {
  try {
    const url = new URL(u);
    const robotsUrl = `${url.protocol}//${url.host}/robots.txt`;
    if (robotsCache.has(url.origin)) return robotsCache.get(url.origin);

    const text = await fetchText(robotsUrl);
    const disallow = [];
    if (text) {
      const lines = text.split(/\r?\n/);
      for (const line of lines) {
        const m = line.match(/^\s*Disallow:\s*(\S+)/i);
        if (m && m[1]) disallow.push(m[1].trim());
      }
    }
    const entry = { disallow };
    robotsCache.set(url.origin, entry);
    return entry;
  } catch {
    return { disallow: [] };
  }
}

async function isAllowedByRobots(u) {
  try {
    const url = new URL(u);
    const robots = await fetchRobots(u);
    const path = url.pathname || '/';
    for (const rule of robots.disallow) {
      if (!rule || rule === '/') continue;
      if (path.startsWith(rule)) return false;
    }
    return true;
  } catch {
    return true;
  }
}

/**
 * Fetch text via http/https
 */
function fetchText(u) {
  return new Promise((resolve) => {
    try {
      const url = new URL(u);
      const lib = url.protocol === 'http:' ? http : https;
      const req = lib.get(u, { headers: { 'User-Agent': 'TinySearchEngineBot/1.0' } }, (res) => {
        if (res.statusCode >= 300 && res.statusCode < 400 && res.headers.location) {
          // follow simple redirects
          const location = new URL(res.headers.location, u).toString();
          res.resume();
          resolve(fetchText(location));
          return;
        }
        let data = '';
        res.setEncoding('utf8');
        res.on('data', chunk => data += chunk);
        res.on('end', () => resolve(data));
      });
      req.on('error', () => resolve(''));
    } catch {
      resolve('');
    }
  });
}

function extractLinks(baseUrl, html) {
  const links = [];
  const re = /<a\s+[^>]*href\s*=\s*["']([^"']+)["'][^>]*>/gi;
  let m;
  while ((m = re.exec(html)) !== null) {
    try {
      const href = m[1];
      const abs = new URL(href, baseUrl);
      if (abs.protocol === 'http:' || abs.protocol === 'https:') {
        links.push(abs.toString());
      }
    } catch { /* ignore bad URLs */ }
  }
  return links;
}
//  parse dom find a tags 

function normalizeUrl(raw) {
  try {
    const u = new URL(raw);
    u.hash = ''; // drop fragment
    return u.toString();
  } catch {
    return null;
  }
}

async function indexPage(url, html, index) {
  // Store doc (improves extraction if cheerio exists)
  const doc = docStore.upsertDocument(url, html);
  // Build a plain text string for the keyword index
  const text = [doc.title, ...(doc.headings || []), doc.bodyText].filter(Boolean).join(' ');
  addPageToIndex(index, url, text);
}

/**
 * Crawl starting at startUrl and populate index + docStore.
 * @param {string} startUrl
 * @param {Map<string, Set<string>>} index
 * @param {import('./docStore')} _docStore not used directly; ensures caller passes it
 * @param {CrawlOptions} options
 */
async function crawl(startUrl, index, _docStore, options = {}) {
  const { maxPages = 50, maxDepth = 2, sameOriginOnly = true, delayMs = 150 } = options;

  const start = new URL(startUrl);
  const origin = start.origin;

  /** @type {Set<string>} */
  const visited = new Set();
  /** @type {Array<{url:string, depth:number}>} */
  const queue = [{ url: normalizeUrl(startUrl), depth: 0 }];

  let count = 0;

  while (queue.length && count < maxPages) {
    const { url, depth } = queue.shift();
    if (!url || visited.has(url)) continue;

    // same-origin enforcement
    if (sameOriginOnly && new URL(url).origin !== origin) continue;

    // robots check
    if (!(await isAllowedByRobots(url))) continue;

    visited.add(url);

    const html = await fetchText(url);
    if (!html) continue;

    await indexPage(url, html, index);
    count++;

    if (depth < maxDepth) {
      const links = extractLinks(url, html);
      for (const l of links) {
        const n = normalizeUrl(l);
        if (n && !visited.has(n)) queue.push({ url: n, depth: depth + 1 });
      }
    }

    if (delayMs > 0) await sleep(delayMs);
  }

  return { pagesCrawled: count, visitedCount: visited.size };
}

module.exports = {
  crawl,
  // exporting helpers for tests
  extractLinks,
  normalizeUrl,
  fetchText,
  isAllowedByRobots,
  indexPage,
};
