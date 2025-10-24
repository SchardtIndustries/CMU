function createIndex(){
    const index = new Map();
    return index;
}

function addPageToIndex(index, URL, pageContent) {
    const keywords = extractKeywords(pageContent);
    for (const keyword of keywords) {
        if (!index.has(keyword)) {
            index.set(keyword, new Set());
        }
        index.get(keyword).add(URL);  // keyword, (url, )
    }
}

function updatePageToIndex(index, URL, newContent) {
    removePageFromIndex(index, URL);
    addPageToIndex(index, URL, newContent);
}

function removePageFromIndex(index, URL) {
    for (const [keyword, urls] of index.entries()) {
        if (urls.has(URL)) {
            urls.delete(URL);
            if (urls.size === 0) {
                index.delete(keyword);
            }
        }
    }
}

function getPagesForKeyword(index, keyword) {
    if (index.has(keyword)) {
        return Array.from(index.get(keyword));
    }
    return [];
}
function extractKeywords(pageContent) {
    const words = pageContent.toLowerCase().match(/\b\w+\b/g);
    const keywords = new Set(words);
    return keywords;
}

module.exports = {
    createIndex,
    addPageToIndex,
    updatePageToIndex,
    removePageFromIndex,
    getPagesForKeyword,
    extractKeywords,
};