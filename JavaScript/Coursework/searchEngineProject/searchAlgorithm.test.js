

// searchAlgorithm.test.js

const { createIndex, addPageToIndex } = require('./searchIndex'); 
const { search } = require('./searchAlgorithm');


describe('Search Algorithm', () => {
    let index;
    beforeEach(() => {
        index = createIndex();
        // Populate the index with some sample data for testing 
        addPageToIndex(index, 'https://www.example.com/cats', 'This is a page  about cats');
        addPageToIndex(index, 'https://www.example.com/dogs', 'This is a page  about dogs and training');
        addPageToIndex(index, 'https://www.training.com', 'This is a general  training website');
        addPageToIndex(index, 'https://www.example.com/ml', 'This is a page  about machine learning');
    });
    it('should return relevant pages for a single keyword  search', () => {
        const results = search(index, 'cats');
        expect(results).toContain('https://www.example.com/cats');
    });
    it('should return relevant pages for a multiple keyword  search', () => {
        const results = search(index, 'dogs training');
        expect(results).toContain('https://www.example.com/dogs');  // Depending on your combination logic, it might or might not include 
        'https://www.training.com'
    });
    it('should return relevant pages for a phrase search', () => {
        const results = search(index, 'machine learning');
        expect(results).toContain('https://www.example.com/ml');
    });
    // Add more test cases to cover other scenarios and edge cases 
}); 
