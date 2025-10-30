const ds = require('./docStore');

describe('docStore', () => {
  test('tokenizes and stores positions', () => {
    const url = 'http://example.com/1';
    ds.upsertDocument(url, '<title>Hello World</title><h1>World</h1><p>Hello again, world.</p>');

    const doc = ds.getDocument(url);
    expect(doc).toBeTruthy();
    expect(doc.termFreq.get('hello')).toBeGreaterThan(0);
    expect(doc.positions.get('world').length).toBeGreaterThan(0);
  });

  test('doc frequency increases and decreases', () => {
    const url = 'http://example.com/2';
    ds.upsertDocument(url, '<title>Foo Bar</title><p>foo baz</p>');
    const dfBefore = ds.getDocFreq('foo');
    expect(dfBefore).toBeGreaterThan(0);
    ds.removeDocument(url);
    const dfAfter = ds.getDocFreq('foo');
    expect(dfAfter).toBe(0);
  });
});
