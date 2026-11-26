<?xml version="1.0" encoding="utf-8"?>
<xsl:stylesheet version="1.0"
  xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
  xmlns:atom="http://www.w3.org/2005/Atom">
  <xsl:output method="html" version="1.0" encoding="UTF-8" indent="yes"/>
  <xsl:template match="/">
    <html lang="en">
      <head>
        <meta charset="utf-8"/>
        <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
        <title><xsl:value-of select="/atom:feed/atom:title"/> :: Atom Feed</title>
        <style>
          :root {
            color-scheme: dark;
            --bg: #0d1117;
            --surface: #161b22;
            --border: #30363d;
            --text: #e6edf3;
            --muted: #9198a1;
            --accent: #a78bfa;
            --link: #58a6ff;
          }
          * { box-sizing: border-box; }
          body {
            margin: 0;
            padding: 2rem 1.25rem 4rem;
            background: var(--bg);
            color: var(--text);
            font-family: 'JetBrains Mono', 'SF Mono', ui-monospace, 'Cascadia Mono', 'Fira Code', Menlo, Consolas, monospace;
            font-size: 15px;
            line-height: 1.65;
          }
          .container {
            max-width: 780px;
            margin: 0 auto;
          }
          .prompt {
            color: var(--accent);
            font-weight: 600;
            margin-bottom: 1.5rem;
            word-break: break-word;
          }
          .prompt a {
            color: inherit;
            text-decoration: none;
          }
          .prompt a:hover {
            text-decoration: underline;
          }
          .notice {
            background: var(--surface);
            border: 1px solid var(--border);
            border-left: 3px solid var(--accent);
            border-radius: 6px;
            padding: 1rem 1.25rem;
            margin-bottom: 2rem;
          }
          .notice h1 {
            margin: 0 0 0.5rem;
            font-size: 1.15rem;
            color: var(--text);
          }
          .notice p {
            margin: 0.4rem 0;
            color: var(--muted);
            font-size: 0.92rem;
          }
          .feed-url {
            display: inline-block;
            margin-top: 0.5rem;
            padding: 0.25rem 0.5rem;
            background: var(--bg);
            border: 1px solid var(--border);
            border-radius: 4px;
            color: var(--accent);
            font-size: 0.88rem;
            word-break: break-all;
          }
          .section-heading {
            color: var(--muted);
            font-size: 0.9rem;
            text-transform: uppercase;
            letter-spacing: 0.06em;
            margin: 0 0 1rem;
            padding-bottom: 0.5rem;
            border-bottom: 1px solid var(--border);
          }
          .entries {
            list-style: none;
            margin: 0;
            padding: 0;
          }
          .entry {
            padding: 1rem 0;
            border-bottom: 1px solid var(--border);
          }
          .entry:last-child {
            border-bottom: none;
          }
          .entry-title {
            margin: 0 0 0.35rem;
            font-size: 1.05rem;
          }
          .entry-title a {
            color: var(--link);
            text-decoration: none;
          }
          .entry-title a:hover {
            text-decoration: underline;
          }
          .entry-meta {
            color: var(--muted);
            font-size: 0.85rem;
            margin-bottom: 0.5rem;
          }
          .entry-tags {
            display: inline;
            margin-left: 0.75rem;
            color: var(--accent);
          }
          .entry-summary {
            margin: 0;
            color: var(--text);
            font-size: 0.92rem;
            opacity: 0.9;
          }
          footer {
            margin-top: 2.5rem;
            padding-top: 1rem;
            border-top: 1px solid var(--border);
            color: var(--muted);
            font-size: 0.85rem;
          }
          footer a {
            color: var(--accent);
            text-decoration: none;
          }
          footer a:hover {
            text-decoration: underline;
          }
        </style>
      </head>
      <body>
        <div class="container">
          <div class="prompt">
            <a>
              <xsl:attribute name="href">
                <xsl:value-of select="/atom:feed/atom:link[@rel='alternate']/@href"/>
              </xsl:attribute>
              [amscotti@128bit.io ~]#
            </a>
            <span> cat index.xml</span>
          </div>

          <section class="notice">
            <h1><xsl:value-of select="/atom:feed/atom:title"/> — Atom Web Feed</h1>
            <p>
              This is an Atom syndication feed. Copy the URL from your browser's address bar and paste it into your RSS/Atom reader (NetNewsWire, Feedbin, Miniflux, Reeder, etc.) to subscribe to new posts.
            </p>
            <xsl:if test="/atom:feed/atom:link[@rel='self']/@href">
              <div class="feed-url">
                <xsl:value-of select="/atom:feed/atom:link[@rel='self']/@href"/>
              </div>
            </xsl:if>
          </section>

          <h2 class="section-heading">
            Recent Posts (<xsl:value-of select="count(/atom:feed/atom:entry)"/>)
          </h2>

          <ul class="entries">
            <xsl:for-each select="/atom:feed/atom:entry">
              <li class="entry">
                <h3 class="entry-title">
                  <a>
                    <xsl:attribute name="href">
                      <xsl:value-of select="atom:link[@rel='alternate']/@href"/>
                    </xsl:attribute>
                    <xsl:value-of select="atom:title"/>
                  </a>
                </h3>
                <div class="entry-meta">
                  <xsl:value-of select="substring(atom:published, 1, 10)"/>
                  <xsl:if test="atom:category">
                    <span class="entry-tags">
                      <xsl:for-each select="atom:category">
                        <xsl:text>[</xsl:text>
                        <xsl:value-of select="@term"/>
                        <xsl:text>] </xsl:text>
                      </xsl:for-each>
                    </span>
                  </xsl:if>
                </div>
                <xsl:if test="atom:summary">
                  <p class="entry-summary">
                    <xsl:choose>
                      <xsl:when test="starts-with(atom:summary, '&lt;p&gt;') and contains(atom:summary, '&lt;/p&gt;')">
                        <xsl:value-of select="substring-before(substring-after(atom:summary, '&lt;p&gt;'), '&lt;/p&gt;')"/>
                      </xsl:when>
                      <xsl:otherwise>
                        <xsl:value-of select="atom:summary"/>
                      </xsl:otherwise>
                    </xsl:choose>
                  </p>
                </xsl:if>
              </li>
            </xsl:for-each>
          </ul>

          <footer>
            <a>
              <xsl:attribute name="href">
                <xsl:value-of select="/atom:feed/atom:link[@rel='alternate']/@href"/>
              </xsl:attribute>
              &lt;= cd ~ (back to <xsl:value-of select="/atom:feed/atom:title"/>)
            </a>
          </footer>
        </div>
      </body>
    </html>
  </xsl:template>
</xsl:stylesheet>
