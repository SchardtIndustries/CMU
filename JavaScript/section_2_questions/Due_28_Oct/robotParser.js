
export const ROBOTS_URL = 'https://www.python.org/robots.txt';

export function parseRobots(content) {
  const text = content.replace(/\r/g, '');
  const records = text
    .split(/\n\s*\n/g)
    .map(b => b.trim())
    .filter(Boolean);

  const pathToAgents = new Map();

  const addMapping = (paths, agents) => {
    if (!agents.length || !paths.length) return;
    for (const raw of paths) {
      const p = raw.trim();
      if (!p) continue; // empty Disallow means allow-all; ignore
      if (!pathToAgents.has(p)) pathToAgents.set(p, new Set());
      const set = pathToAgents.get(p);
      for (const a of agents) set.add(a);
    }
  };

  for (const record of records) {
    const lines = record
      .split('\n')
      .map(l => {
        const i = l.indexOf('#');
        return (i >= 0 ? l.slice(0, i) : l).trim();
      })
      .filter(Boolean);

    const agents = [];
    const disallows = [];

    for (const line of lines) {
      // ✅ case-insensitive directive names
      const m = /^(user-agent|disallow|allow)\s*:\s*(.*)$/i.exec(line);
      if (!m) continue;
      const key = m[1].toLowerCase();
      const value = m[2].trim();

      if (key === 'user-agent') {
        if (value) agents.push(value);
      } else if (key === 'disallow') {
        if (value) disallows.push(value);
      } else {
        // "allow" not needed for this assignment
      }
    }

    addMapping(disallows, agents);
  }

  const getAgentsForPath = (path) => pathToAgents.get(path) ?? new Set();
  const getSitewideAgents = () => new Set(getAgentsForPath('/'));

  return { pathToAgents, getAgentsForPath, getSitewideAgents };
}

export async function fetchRobots(url = ROBOTS_URL) {
  const res = await fetch(url, { redirect: 'follow' });
  if (!res.ok) throw new Error(`Failed to fetch robots: ${res.status} ${res.statusText}`);
  return await res.text();
}

export async function httpsGet(url) {
  const https = await import('node:https');
  return new Promise((resolve, reject) => {
    https.get(url, (res) => {
      if (res.statusCode && res.statusCode >= 400) {
        reject(new Error(`HTTP ${res.statusCode}`));
        return;
      }
      let data = '';
      res.setEncoding('utf8');
      res.on('data', (chunk) => (data += chunk));
      res.on('end', () => resolve(data));
    }).on('error', reject);
  });
}

import { pathToFileURL } from 'node:url';
if (import.meta.url === pathToFileURL(process.argv[1]).href) {
  (async () => {
    try {
      const robotsTxt = typeof fetch === 'function'
        ? await fetchRobots(ROBOTS_URL)
        : await httpsGet(ROBOTS_URL);

      const { getSitewideAgents } = parseRobots(robotsTxt);
      const agents = Array.from(getSitewideAgents()).sort((a, b) => a.localeCompare(b));
      for (const a of agents) console.log(a);
    } catch (err) {
      console.error('Error:', err?.message || String(err));
      process.exitCode = 1;
    }
  })();
}
