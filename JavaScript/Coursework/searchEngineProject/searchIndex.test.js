/* eslint-env jest */

// searchIndex.test.js
const {
  createIndex,
  addPageToIndex,
  updatePageInIndex,
  removePageFromIndex,
  getPagesForKeyword,
} = require('./searchIndex');

describe('Search Index', () => {
  let index;

  beforeEach(() => {
    index = createIndex();
  });

  // Scenario 1: Adding a new page
  it('should add a new page to the index', () => {
    addPageToIndex(index, 'https://www.example.com', 'This is a sample web page about dogs');
    expect(getPagesForKeyword(index, 'dogs')).toContain('https://www.example.com');
  });

  // Scenario 2: Updating a page
  it('should update a page in the index', () => {
    addPageToIndex(index, 'https://www.example.com', 'This is a sample web page about dogs');
    updatePageInIndex(index, 'https://www.example.com', 'This is a sample web page about cats');
    expect(getPagesForKeyword(index, 'dogs')).not.toContain('https://www.example.com');
    expect(getPagesForKeyword(index, 'cats')).toContain('https://www.example.com');
  });

  // Scenario 3: Removing a page
  it('should remove a page from the index', () => {
    addPageToIndex(index, 'https://www.example.com', 'This is a sample web page about cats');
    removePageFromIndex(index, 'https://www.example.com');
    expect(getPagesForKeyword(index, 'cats')).not.toContain('https://www.example.com');
  });

  // Scenario 4: Searching for a keyword
  it('should return relevant pages for a keyword', () => {
    addPageToIndex(index, 'https://www.example.com', 'This is a sample web page about cats');
    expect(getPagesForKeyword(index, 'cats')).toContain('https://www.example.com');
  });

  // Extra coverage

  it('is case-insensitive for both content and query', () => {
    addPageToIndex(index, 'https://a.com', 'CATS are great');
    expect(getPagesForKeyword(index, 'cats')).toContain('https://a.com');
    expect(getPagesForKeyword(index, 'CATS')).toContain('https://a.com');
  });

  it('handles punctuation and extra whitespace gracefully', () => {
    addPageToIndex(index, 'https://b.com', '  Dogs, dogs!  DOGS???  ');
    const results = getPagesForKeyword(index, 'dogs');
    expect(results).toContain('https://b.com');
  });

  it('indexes multiple pages for the same keyword', () => {
    addPageToIndex(index, 'https://p1.com', 'cats and more cats');
    addPageToIndex(index, 'https://p2.com', 'cats are cool');
    const results = getPagesForKeyword(index, 'cats');
    expect(results).toEqual(expect.arrayContaining(['https://p1.com', 'https://p2.com']));
    expect(results.length).toBeGreaterThanOrEqual(2);
  });

  it('does not create duplicate entries for the same page when re-added', () => {
    addPageToIndex(index, 'https://dup.com', 'dogs');
    addPageToIndex(index, 'https://dup.com', 'dogs'); // re-adding same URL/content
    const results = getPagesForKeyword(index, 'dogs');
    // Ensure URL appears at most once
    expect(results.filter(u => u === 'https://dup.com').length).toBe(1);
  });

  it('updating a non-existent page does not throw', () => {
    expect(() =>
      updatePageInIndex(index, 'https://missing.com', 'cats')
    ).not.toThrow();
    // Implementation-dependent behavior: either no-op or add; both are acceptable for this test.
  });

  it('removing a non-existent page does not throw', () => {
    expect(() => removePageFromIndex(index, 'https://nope.com')).not.toThrow();
  });

  it('returns an empty array for unknown keywords', () => {
    addPageToIndex(index, 'https://x.com', 'about turtles');
    const results = getPagesForKeyword(index, 'unicorns');
    expect(Array.isArray(results)).toBe(true);
    expect(results).toHaveLength(0);
  });

  it('replaces old keywords with new ones on update (no stale hits)', () => {
    addPageToIndex(index, 'https://swap.com', 'parrots and birds');
    expect(getPagesForKeyword(index, 'parrots')).toContain('https://swap.com');

    updatePageInIndex(index, 'https://swap.com', 'fish and aquariums');
    expect(getPagesForKeyword(index, 'parrots')).not.toContain('https://swap.com');
    expect(getPagesForKeyword(index, 'fish')).toContain('https://swap.com');
  });

  it('handles empty content without crashing', () => {
    addPageToIndex(index, 'https://empty.com', '');
    expect(() => getPagesForKeyword(index, 'anything')).not.toThrow();
    expect(getPagesForKeyword(index, 'anything')).not.toContain('https://empty.com');
  });

  it('trims and normalizes repeated spaces in content and search terms', () => {
    addPageToIndex(index, 'https://spacey.com', 'lots     of    spaces about   cats');
    expect(getPagesForKeyword(index, 'cats')).toContain('https://spacey.com');
    // Also try spaced query (if your tokenizer normalizes query):
    expect(getPagesForKeyword(index, '   cats   ')).toContain('https://spacey.com');
  });
 });
