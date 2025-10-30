
function createIndex() {
  // The main data structure: Map<keyword, Set<URL>>
  return new Map();
}


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

function updatePageInIndex(index, URL, newContent) {
  removePageFromIndex(index, URL);
  addPageToIndex(index, URL, newContent);
}

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


function getPagesForKeyword(index, keyword) {
  const normalized = String(keyword).trim().toLowerCase();
  if (normalized.length === 0) return [];

  if (index.has(normalized)) {
    // Return the URLs as a normal array
    return Array.from(index.get(normalized));
  }
  return [];
}

// Replace your extractKeywords with this version
function extractKeywords(pageContent) {
  if (!pageContent) return new Set();

  const STOPWORDS = new Set([
    'a','an','the','and','or','but','if','then','else','of','for','on','in','to','from','by',
    'with','about','as','at','into','like','through','after','over','between','out','against',
    'during','without','before','under','around','among','is','are','was','were','be','been',
    'being','do','does','did','doing','have','has','had','having','i','you','he','she','it',
    'we','they','me','him','her','them','my','your','his','their','our','mine','yours','ours',
  ]);

  const words = String(pageContent).toLowerCase().match(/\b\w+\b/g) || [];

  const stem = (w) => {
    // super naive: strip trailing 's' or 'es'
    if (w.endsWith('ies') && w.length > 3) return w.slice(0, -3) + 'y'; // "stories" -> "story"
    if (w.endsWith('es') && w.length > 2) return w.slice(0, -2);        // "classes" -> "class"
    if (w.endsWith('s') && w.length > 1)  return w.slice(0, -1);        // "cats" -> "cat"
    return w;
  };

  const set = new Set();
  for (const raw of words) {
    if (STOPWORDS.has(raw)) continue;
    const s = stem(raw);
    if (s) set.add(s);
  }
  return set;
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
