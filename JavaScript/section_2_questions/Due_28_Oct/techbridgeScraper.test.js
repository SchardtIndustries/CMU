
import { jest } from '@jest/globals';
import {
  parseModulesFromHtml,
  extractModuleFromHeadingText,
  scrapeModules,
} from './techbridgeScraper.js';

describe('extractModuleFromHeadingText', () => {
  test('handles "Module 7: Full-Stack Integration"', () => {
    expect(extractModuleFromHeadingText('Module 7: Full-Stack Integration'))
      .toEqual(['M7', 'Full-Stack Integration']);
  });

  test('handles "module 12 -  Data Wrangling"', () => {
    expect(extractModuleFromHeadingText('module 12 -  Data Wrangling'))
      .toEqual(['M12', 'Data Wrangling']);
  });

  test('handles "M7 — Full-Stack Integration"', () => {
    expect(extractModuleFromHeadingText('M7 — Full-Stack Integration'))
      .toEqual(['M7', 'Full-Stack Integration']);
  });

  test('returns null for non-module headings', () => {
    expect(extractModuleFromHeadingText('Admissions & Financing')).toBeNull();
  });
});

describe('parseModulesFromHtml', () => {
  const SAMPLE_HTML = `
    <section>
      <h2>Module 1: Programming Basics</h2>
      <p>intro text…</p>
      <h2> M7 — Full-Stack Integration </h2>
      <h2>module 12 -  Data   Wrangling</h2>
      <h2>Frequently Asked Questions</h2>
      <h2> M 3:   Web  Foundations</h2>
      <h2>Module 10:   Back-End  APIs</h2>
    </section>
  `;

  test('builds mapping from multiple H2 variants', () => {
    const mapping = parseModulesFromHtml(SAMPLE_HTML);
    expect(mapping).toEqual({
      M1: 'Programming Basics',
      M3: 'Web Foundations',
      M7: 'Full-Stack Integration',
      M10: 'Back-End APIs',
      M12: 'Data Wrangling',
    });
  });

  test('ignores non-module H2s', () => {
    const html = `<h2>Admissions</h2><h2>Module 2: JS</h2>`;
    const mapping = parseModulesFromHtml(html);
    expect(mapping).toEqual({ M2: 'JS' });
  });
});

describe('scrapeModules (integration - mocked fetch)', () => {
  test('uses fetch and parses results', async () => {
    const fakeHtml = `
      <h2>Module 5: Databases</h2>
      <h2> M6 - DevOps </h2>
    `;

    const origFetch = global.fetch;
    global.fetch = jest.fn().mockResolvedValue({
      ok: true,
      text: async () => fakeHtml,
      status: 200,
      statusText: 'OK',
    });

    try {
      const mapping = await scrapeModules('https://example.test/');
      expect(mapping).toEqual({
        M5: 'Databases',
        M6: 'DevOps',
      });
      expect(global.fetch).toHaveBeenCalledWith('https://example.test/', { redirect: 'follow' });
    } finally {
      global.fetch = origFetch;
    }
  });
});
