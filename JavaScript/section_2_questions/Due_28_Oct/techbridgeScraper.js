
/**
 * Extract { M# : "Description" } from a single H2 text.
 * Supports variants like:
 *  - "Module 7: Full-Stack Integration"
 *  - "module 12 -  Data Wrangling"
 *  - "M7 — Full-Stack Integration"
 *  - "M 3:  Some Title"
 * Returns [key, description] or null if not a module heading.
 */
export function extractModuleFromHeadingText(text) {
  if (!text) return null;

  // Normalize whitespace
  const t = text.replace(/\s+/g, ' ').trim();

  // Try to detect "Module N" or "M N" (case-insensitive), then capture the rest as description.
  // Accept separators: :, -, — (em dash), – (en dash)
  // Examples matched:
  //  - "Module 7: Full-Stack Integration"
  //  - "module 12 - Data Wrangling"
  //  - "M7 — Full-Stack Integration"
  //  - "M 3: Some Title"
  const m =
    /^(?:module\s*|m\s*)(\d+)\s*(?:[:\-–—]\s*)?(.*)$/i.exec(t);

  if (!m) return null;

  const num = m[1];
  // The part after the separator (if present) is the description. If empty, fallback to full text.
  const desc = (m[2] || '').trim() || t;

  return [`M${num}`, desc];
}

/**
 * Very light HTML-to-text for <h2> inner HTML:
 * - strips tags
 * - decodes a few common entities
 * We keep it simple since whitespace “noise” is allowed.
 */
function htmlToText(html) {
  const noTags = html.replace(/<[^>]*>/g, ' ');
  return noTags
    .replace(/&nbsp;/gi, ' ')
    .replace(/&amp;/gi, '&')
    .replace(/&lt;/gi, '<')
    .replace(/&gt;/gi, '>')
    .replace(/\s+/g, ' ')
    .trim();
}

/**
 * Parse all <h2> elements from the HTML and build the { M# : "Desc" } object.
 */
export function parseModulesFromHtml(html) {
  const out = {};
  // Grab all H2 blocks (case-insensitive, dotall)
  const h2Regex = /<h2\b[^>]*>([\s\S]*?)<\/h2>/gi;
  let match;
  while ((match = h2Regex.exec(html)) !== null) {
    const inner = match[1] ?? '';
    const text = htmlToText(inner);
    const kv = extractModuleFromHeadingText(text);
    if (kv) {
      const [key, desc] = kv;
      out[key] = desc; // last one wins if duplicates
    }
  }
  return out;
}

/**
 * Fetch page and return the { M# : "Desc" } mapping.
 */
export async function scrapeModules(url = 'https://bootcamps.cs.cmu.edu/coding-bootcamp/') {
  const res = await fetch(url, { redirect: 'follow' });
  if (!res.ok) {
    throw new Error(`Failed to fetch page: ${res.status} ${res.statusText}`);
  }
  const html = await res.text();
  return parseModulesFromHtml(html);
}

// CLI entry: `node Due_28_Oct/techbridgeScraper.js`
import { pathToFileURL } from 'node:url';
if (import.meta.url === pathToFileURL(process.argv[1]).href) {
  (async () => {
    try {
      const mapping = await scrapeModules();
      // Print as pretty JSON
      console.log(JSON.stringify(mapping, null, 2));
    } catch (err) {
      console.error('Error:', err?.message || String(err));
      process.exitCode = 1;
    }
  })();
}
