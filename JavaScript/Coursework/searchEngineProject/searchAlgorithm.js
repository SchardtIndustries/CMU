const { getPagesForKeyword, extractKeywords } = require('./searchIndex');

/**
 * Searches the index for pages matching one or more keywords (OR semantics).
 * @param {Map<string, Set<string>>} index
 * @param {string} query
 * @returns {string[]} unique URLs
 */
function search(index, query) {
  if (!query || typeof query !== 'string' || !query.trim()) return [];

  const keywords = extractKeywords(String(query)); // ensure string
  const results = new Set();

  for (const keyword of keywords) {
    const urls = getPagesForKeyword(index, keyword);
    for (const url of urls) results.add(url);
  }

  return Array.from(results);
}

module.exports = { search };
