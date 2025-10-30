
import { parseRobots } from './robotParser.js';

const SAMPLE = `
# Directions for robots. See: http://www.robotstxt.org/robotstxt.html

User-agent: HTTrack
User-agent: puf
User-agent: MSIECrawler
Disallow: /

# The Krugle web crawler is OK.
User-agent: Krugle
Allow: /
Disallow: /~guido/orlijn/
Disallow: /webstats/

# No one should be crawling us with Nutch.
User-agent: Nutch
Disallow: /

# Generic record
User-agent: *
Disallow: /~guido/orlijn/
Disallow: /webstats/
`;

describe('robots parser (blank-line separated records)', () => {
  test('maps disallowed paths to user-agents', () => {
    const { pathToAgents, getAgentsForPath } = parseRobots(SAMPLE);

    expect(Array.from(pathToAgents.keys()).sort()).toEqual(
      ['/', '/webstats/', '/~guido/orlijn/'].sort()
    );

    const sitewide = Array.from(getAgentsForPath('/'));
    expect(new Set(sitewide)).toEqual(
      new Set(['HTTrack', 'puf', 'MSIECrawler', 'Nutch'])
    );

    const webstats = Array.from(getAgentsForPath('/webstats/'));
    expect(new Set(webstats)).toEqual(new Set(['Krugle', '*']));

    const guido = Array.from(getAgentsForPath('/~guido/orlijn/'));
    expect(new Set(guido)).toEqual(new Set(['Krugle', '*']));
  });

  test('ignores empty Disallow (allow-all lines)', () => {
    const sample = `
User-agent: Foo
Disallow: 

User-agent: Bar
Disallow: /
`;
    const { pathToAgents, getAgentsForPath } = parseRobots(sample);
    expect(pathToAgents.has('')).toBe(false);
    expect(Array.from(getAgentsForPath('/'))).toEqual(['Bar']);
  });

  test('directive names are case-insensitive', () => {
    const sample = `
uSeR-aGeNt: Xbot
dIsAlLoW: /
`;
    const { getAgentsForPath } = parseRobots(sample);
    expect(Array.from(getAgentsForPath('/'))).toEqual(['Xbot']);
  });
});
