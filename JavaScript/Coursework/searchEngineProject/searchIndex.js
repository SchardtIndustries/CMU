function createIndex(){
    const index = new Map();
    return index;
}

const index = createIndex();
console.log(index);
// addPageToIndex(indexedDB, URL, pageContent)
// updatePageToIndex(indexedDB, URL, newContent)
// removePageFromIndex(indexedDB, URL)
// getPagesForKeyword(indexedDB, keyword)
// extractKeywords(pageContent)
