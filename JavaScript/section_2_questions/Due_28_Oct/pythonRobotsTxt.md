# You must parse the robots.txt file from python.org to tell what crawlers are disallowed from all parts of the site (`disallow: /`)

- Fetch the robots file
- Create a data structure mapping disallowed paths to crawlers
- Parse the file to populate the data structure
- Print the crawlers that are disallowed site-wide

Multiple user-agents may share the same disallow directive, and one or more agents may be disallowed multiple paths.
To simplify the job of parsing, you may presume that records mapping N user-agents to M disallowed paths are separated by BLANK lines.
( i.e. follow this standard <https://www.robotstxt.org/orig.html> rather than Google's treatment of whitespace as optional)
