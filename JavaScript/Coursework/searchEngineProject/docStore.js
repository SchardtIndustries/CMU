/**
 * docStore.js
 * 
 * A tiny in-memory document store that keeps enough structure
 * for ranking: title, headings, body tokens, term frequencies,
 * and token positions. Also tracks document frequency per term.
 */

const { extractKeywords } = require('./searchIndex');

function tokenize(text) {
  if (!text) return [];
  const m = String(text).toLowerCase().match(/\b\w+\b/g);
  return m ? m : [];
}

function incrementDf(termsSet) {
  for (const t of termsSet) {
    docFreq.set(t, (docFreq.get(t) || 0) + 1);
  }
}

function decrementDf(termsSet) {
  for (const t of termsSet) {
    const cur = docFreq.get(t) || 0;
    if (cur <= 1) docFreq.delete(t);
    else docFreq.set(t, cur - 1);
  }
}

/**
 * Naive HTML extraction with optional cheerio.
 * Returns title, headings[], bodyText.
 */
function defaultExtractor(htmlOrText) {
  let title = '';
  const headings = [];
  let bodyText = '';

  try {
    const cheerio = require('cheerio');
    const $ = cheerio.load(htmlOrText);
    title = ($('title').text() || '').trim();
    $('h1,h2,h3').each((_, el) => headings.push($(el).text().trim()));
    bodyText = $('body').text() || $.root().text() || '';
  } catch {
    // Fallback: strip tags crudely
    const noScripts = String(htmlOrText).replace(/<script[\s\S]*?<\/script>/gi, '');
    title = (noScripts.match(/<title[^>]*>([\s\S]*?)<\/title>/i) || [,''])[1].trim();
    const headingMatches = [...noScripts.matchAll(/<h[1-3][^>]*>([\s\S]*?)<\/h[1-3]>/gi)];
    for (const m of headingMatches) headings.push(m[1].replace(/<[^>]+>/g, '').trim());
    bodyText = noScripts.replace(/<[^>]+>/g, ' ');
  }

  return { title, headings, bodyText };
}

/**
 * Insert or replace a document.
 * Builds tokens, positions, and term frequencies.
 * @param {string} url
 * @param {string} htmlOrText
 * @param {{extractor?: (s:string)=>{title:string, headings:string[], bodyText:string}}} [opts]
 */
function upsertDocument(url, htmlOrText, opts = {}) {
  if (!url) return;

  // If replacing, first remove to keep DF correct
  if (docs.has(url)) removeDocument(url);

  const extractor = opts.extractor || defaultExtractor;
  const { title, headings, bodyText } = extractor(htmlOrText);

  const titleTokens = tokenize(title);
  const headingTokens = headings.map(h => tokenize(h));
  const bodyTokens = tokenize(bodyText);

  const allTokens = [...titleTokens, ...headingTokens.flat(), ...bodyTokens];

  // Build positions map
  const positions = new Map();
  const termFreq = new Map();
  for (let i = 0; i < allTokens.length; i++) {
    const t = allTokens[i];
    termFreq.set(t, (termFreq.get(t) || 0) + 1);
    if (!positions.has(t)) positions.set(t, []);
    positions.get(t).push(i);
  }

  // For DF we only count distinct terms in this doc
  const distinct = new Set(allTokens);
  incrementDf(distinct);

  const doc = {
    url,
    title,
    headings,
    bodyText,
    titleTokens,
    headingTokens,
    bodyTokens,
    termFreq,
    positions,
  };
  docs.set(url, doc);

  return doc;
}

function removeDocument(url) {
  const doc = docs.get(url);
  if (!doc) return;
  const distinct = new Set([
    ...doc.titleTokens,
    ...doc.headingTokens.flat(),
    ...doc.bodyTokens,
  ]);
  decrementDf(distinct);
  docs.delete(url);
}

function getDocument(url) {
  return docs.get(url);
}

function getAllDocs() {
  return docs.entries();
}

function getCorpusSize() {
  return docs.size;
}

function getDocFreq(term) {
  return docFreq.get(String(term).toLowerCase()) || 0;
}

module.exports = {
  upsertDocument,
  removeDocument,
  getDocument,
  getAllDocs,
  getCorpusSize,
  getDocFreq,
  tokenize, // exported for tests
  defaultExtractor,
};
