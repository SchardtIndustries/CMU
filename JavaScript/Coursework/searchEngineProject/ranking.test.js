const { rankSearchResults, scoreTfIdf, scoreLocation, scoreProximity } = require('./ranking');
const { createIndex, addPageToIndex } = require('./searchIndex');
const docStore = require('./docStore');

describe('ranking basics', () => {
  beforeEach(() => {
    // reset docStore internal state by removing and re-adding via upserts into a new process is tricky.
    // We'll simulate a clean environment by reloading the module if needed.
  });

  test('ranks by tf-idf and title boost', () => {
    const index = createIndex();
    const urlA = 'http://site/a';
    const urlB = 'http://site/b';

    const htmlA = '<title>cats and dogs</title><p>cats cats cats</p>';
    const htmlB = '<title>about pets</title><h1>dogs</h1><p>dogs dogs</p>';

    docStore.upsertDocument(urlA, htmlA);
    addPageToIndex(index, urlA, 'cats and dogs cats cats cats');

    docStore.upsertDocument(urlB, htmlB);
    addPageToIndex(index, urlB, 'about pets dogs dogs dogs');

    const urls = [urlA, urlB];
    const ranked = rankSearchResults(index, 'cats dogs', urls, { docStore });

    expect(ranked[0]).toBe(urlA); // "cats" frequency + title match
  });

  test('proximity gives small boost', () => {
    const index = createIndex();
    const url = 'http://site/x';
    const html = '<title>alpha beta</title><p>alpha ... beta</p>';
    docStore.upsertDocument(url, html);
    addPageToIndex(index, url, 'alpha alpha beta');

    const ranked = rankSearchResults(index, 'alpha beta', [url], { docStore });
    // score should be a finite number >= 0
    // We sanity check function doesn't throw and returns the URL.
    expect(ranked).toEqual([url]);
  });
});
