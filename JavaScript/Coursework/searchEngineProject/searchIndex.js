/**
 * searchIndex.js
 * 
 * A simple in-memory search index implementation.
 * 
 * Each keyword maps to a set of URLs whose page content contains that keyword.
 * The index supports adding, updating, removing, and retrieving pages
 * based on the words found in their content.
 */

/**
 * Creates a new empty index.
 * @returns {Map<string, Set<string>>} A Map where keys are keywords and values are Sets of URLs.
 */
function createIndex() {
  // The main data structure: Map<keyword, Set<URL>>
  return new Map();
}

/**
 * Adds a page’s content to the index.
 * Splits the content into keywords, normalizes them,
 * and associates each keyword with the given URL.
 *
 * @param {Map<string, Set<string>>} index - The current search index.
 * @param {string} URL - The page URL being indexed.
 * @param {string} pageContent - The text content of the page.
 */
function addPageToIndex(index, URL, pageContent) {
  const keywords = extractKeywords(pageContent);

  for (const keyword of keywords) {
    // If keyword not present, initialize an empty Set
    if (!index.has(keyword)) {
      index.set(keyword, new Set());
    }
    // Add the URL to the keyword’s set
    index.get(keyword).add(URL);
  }
}

/**
 * Updates a page’s content in the index.
 * Effectively removes the old version of the page (to prevent stale keywords)
 * and then re-adds it with the new content.
 *
 * @param {Map<string, Set<string>>} index - The search index.
 * @param {string} URL - The URL of the page to update.
 * @param {string} newContent - The updated page content.
 */
function updatePageInIndex(index, URL, newContent) {
  removePageFromIndex(index, URL);
  addPageToIndex(index, URL, newContent);
}

/**
 * Removes all references to a page (by URL) from the index.
 * If a keyword no longer has any URLs after removal, it is deleted entirely.
 *
 * @param {Map<string, Set<string>>} index - The search index.
 * @param {string} URL - The page URL to remove.
 */
function removePageFromIndex(index, URL) {
  for (const [keyword, urls] of index.entries()) {
    if (urls.has(URL)) {
      urls.delete(URL);
      // Clean up empty keyword entries
      if (urls.size === 0) {
        index.delete(keyword);
      }
    }
  }
}

/**
 * Retrieves all page URLs that contain a given keyword.
 * Trims and lowercases the keyword to ensure case-insensitive matching.
 *
 * @param {Map<string, Set<string>>} index - The search index.
 * @param {string} keyword - The search keyword.
 * @returns {string[]} An array of URLs containing that keyword.
 */
function getPagesForKeyword(index, keyword) {
  const normalized = String(keyword).trim().toLowerCase();
  if (normalized.length === 0) return [];

  if (index.has(normalized)) {
    // Return the URLs as a normal array
    return Array.from(index.get(normalized));
  }
  return [];
}

/**
 * Extracts keywords from a page’s text content.
 * Converts all words to lowercase and filters out punctuation and duplicates.
 *
 * @param {string} pageContent - The full text content of a page.
 * @returns {Set<string>} A Set of lowercase keywords.
 */
function extractKeywords(pageContent) {
  if (!pageContent) return new Set();
  const words = pageContent.toLowerCase().match(/\b\w+\b/g) || [];
  return new Set(words);
}

// Export all public functions
module.exports = {
  createIndex,
  addPageToIndex,
  updatePageInIndex,
  removePageFromIndex,
  getPagesForKeyword,
  extractKeywords,
};
