/**
 * ranking.js
 * 
 * Ranks candidate URLs for a query using a simple combination of:
 * - TF-IDF (per term)
 * - Location boosts (title/headings vs body)
 * - Proximity of query terms (crude average distance)
 * 
 * CommonJS module to match the project's style.
 */

const { extractKeywords } = require('./searchIndex');

/**
 * @typedef {Object} RankingWeights
 * @property {number} tfidf
 * @property {number} location
 * @property {number} proximity
 */

/**
 * @param {Map<string, Set<string>>} index
 * @param {string} query
 * @param {string[]} urls
 * @param {Object} options
 * @param {import('./docStore')} options.docStore
 * @param {RankingWeights} [options.weights]
 * @returns {string[]} urls sorted by descending score
 */
function rankSearchResults(index, query, urls, { docStore, weights } = {}) {
  if (!Array.isArray(urls) || urls.length === 0) return [];
  if (!query || typeof query !== 'string') return urls;

  const w = Object.assign({ tfidf: 1.0, location: 0.5, proximity: 0.25 }, weights || {});

  const terms = Array.from(extractKeywords(query)); // Set -> Array
  const N = docStore.getCorpusSize();

  // Precompute DF/IDF
  const idf = new Map();
  for (const t of terms) {
    const df = docStore.getDocFreq(t) || 0;
    // smoothed IDF to avoid div-by-zero; +1 inside log is common tweak
    const val = Math.log((N + 1) / (df + 1)) + 1;
    idf.set(t, val);
  }

  /** @type {Array<{url:string, score:number}>} */
  const scored = [];

  for (const url of urls) {
    const doc = docStore.getDocument(url);
    if (!doc) {
      scored.push({ url, score: 0 });
      continue;
    }

    const tfidfScore = scoreTfIdf(terms, doc, idf);
    const locationScore = scoreLocation(terms, doc);
    const proximityScore = scoreProximity(terms, doc);

    const combined = w.tfidf * tfidfScore + w.location * locationScore + w.proximity * proximityScore;

    scored.push({ url, score: combined });
  }

  scored.sort((a, b) => b.score - a.score);
  return scored.map(s => s.url);
}

/**
 * TF-IDF score: sum over terms of tf(term, doc) * idf(term)
 */
function scoreTfIdf(terms, doc, idf) {
  let sum = 0;
  for (const t of terms) {
    const tf = (doc.termFreq.get(t) || 0);
    const idfVal = idf.get(t) || 0;
    sum += tf * idfVal;
  }
  return sum;
}

/**
 * Location score boosts matches in title/headings.
 * Simple heuristic:
 *  - +2 per distinct term in title
 *  - +1 per distinct term in any heading
 *  - +0.25 per distinct term in body (tiny nudge)
 */
function scoreLocation(terms, doc) {
  const titleTokens = new Set(doc.titleTokens || []);
  const headingTokens = new Set((doc.headingTokens || []).flat());

  let score = 0;
  for (const t of terms) {
    if (titleTokens.has(t)) score += 2;
    else if (headingTokens.has(t)) score += 1;
    else if ((doc.termFreq.get(t) || 0) > 0) score += 0.25;
  }
  return score;
}

/**
 * Proximity score (very crude):
 * - For each adjacent pair of query terms (q[i], q[i+1]), compute the minimum distance
 *   between any occurrence of q[i] and q[i+1] in the doc.
 * - Score is the inverse of the average min distance (with small smoothing).
 */
function scoreProximity(terms, doc) {
  if (terms.length < 2) return 0;

  const positions = doc.positions || new Map();
  const pairDistances = [];

  for (let i = 0; i < terms.length - 1; i++) {
    const a = positions.get(terms[i]) || [];
    const b = positions.get(terms[i + 1]) || [];
    if (a.length === 0 || b.length === 0) continue;

    // find min |ai - bj|
    let minDist = Infinity;
    let bi = 0;
    for (const ai of a) {
      while (bi < b.length && b[bi] < ai) bi++;
      if (bi < b.length) minDist = Math.min(minDist, Math.abs(ai - b[bi]));
      if (bi > 0) minDist = Math.min(minDist, Math.abs(ai - b[bi - 1]));
    }
    if (minDist !== Infinity) pairDistances.push(minDist);
  }

  if (pairDistances.length === 0) return 0;
  const avg = pairDistances.reduce((s, x) => s + x, 0) / pairDistances.length;
  // inverse with smoothing
  return 1 / (1 + avg);
}

module.exports = {
  rankSearchResults,
  scoreTfIdf, // exported for tests
  scoreLocation,
  scoreProximity,
};
