const { extractLinks, normalizeUrl } = require('./spider');

describe('spider helpers', () => {
  test('extractLinks finds absolute and relative links', () => {
    const html = '<a href="/a">A</a><a href="http://x.com/b">B</a>';
    const links = extractLinks('http://site.com/', html);
    expect(links).toContain('http://site.com/a');
    expect(links).toContain('http://x.com/b');
  });

  test('normalizeUrl drops fragment', () => {
    const n = normalizeUrl('http://x.com/path#section');
    expect(n).toBe('http://x.com/path');
  });
});
