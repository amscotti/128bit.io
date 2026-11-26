/* Minimal128 — Progressive terminal enhancements (CSP-safe, zero deps) */

(() => {
  'use strict';

  const THEME_KEY = 'theme';
  const root = document.documentElement;

  /* ------------------------------------------------------------------------
     1. Theme Toggle (Light / Dark)
     ------------------------------------------------------------------------ */
  const systemDark = window.matchMedia('(prefers-color-scheme: dark)');
  const themeBtn = document.querySelector('[data-theme-toggle]');

  function getActiveTheme() {
    const stored = root.dataset.theme;
    if (stored === 'dark' || stored === 'light') return stored;
    return systemDark.matches ? 'dark' : 'light';
  }

  function applyTheme(theme, persist) {
    if (theme === 'dark' || theme === 'light') {
      root.dataset.theme = theme;
      if (persist) {
        try {
          localStorage.setItem(THEME_KEY, theme);
        } catch {
          /* ignore storage quota/privacy errors */
        }
      }
    }
    updateThemeButton();
  }

  function updateThemeButton() {
    if (!themeBtn) return;
    const active = getActiveTheme();
    const next = active === 'dark' ? 'light' : 'dark';
    themeBtn.textContent = `[${next}]`;
    themeBtn.setAttribute('aria-pressed', String(active === 'light'));
    themeBtn.setAttribute('aria-label', `Switch to ${next} theme`);
  }

  try {
    const saved = localStorage.getItem(THEME_KEY);
    if (saved === 'dark' || saved === 'light') {
      root.dataset.theme = saved;
    }
  } catch {
    /* ignore storage errors */
  }
  updateThemeButton();

  if (themeBtn) {
    themeBtn.addEventListener('click', () => {
      const next = getActiveTheme() === 'dark' ? 'light' : 'dark';
      applyTheme(next, true);
    });
  }

  systemDark.addEventListener('change', () => {
    if (!root.dataset.theme) updateThemeButton();
  });

  /* ------------------------------------------------------------------------
     2. Desktop TOC Auto-Open
     ------------------------------------------------------------------------ */
  const tocPanel = document.querySelector('.toc-panel');
  if (tocPanel && window.matchMedia('(min-width: 1180px)').matches) {
    tocPanel.open = true;
  }

  /* ------------------------------------------------------------------------
     3. Code Block Language Badge & Copy Button
     ------------------------------------------------------------------------ */
  function extractLanguage(container, codeEl) {
    const sources = [container, codeEl].filter(Boolean);
    for (const el of sources) {
      for (const cls of el.classList) {
        if (cls.startsWith('language-') && cls.length > 9) {
          return cls.slice(9);
        }
        if (cls.startsWith('lang-') && cls.length > 5) {
          return cls.slice(5);
        }
      }
    }
    return 'code';
  }

  function attachCodeHeader(wrapper, codeEl) {
    if (wrapper.querySelector('.code-header')) return;
    const header = document.createElement('div');
    header.className = 'code-header';

    const lang = document.createElement('span');
    lang.className = 'code-lang';
    lang.textContent = extractLanguage(wrapper, codeEl);

    const btn = document.createElement('button');
    btn.type = 'button';
    btn.className = 'code-copy-btn';
    btn.textContent = '[copy]';
    btn.setAttribute('aria-label', 'Copy code to clipboard');

    let timerId = null;
    btn.addEventListener('click', async () => {
      const text = codeEl ? codeEl.innerText : '';
      if (!navigator.clipboard || !text) return;
      try {
        await navigator.clipboard.writeText(text);
        btn.textContent = '[copied]';
        btn.dataset.copied = 'true';
        clearTimeout(timerId);
        timerId = window.setTimeout(() => {
          btn.textContent = '[copy]';
          delete btn.dataset.copied;
        }, 1800);
      } catch {
        btn.textContent = '[failed]';
      }
    });

    header.append(lang, btn);
    wrapper.prepend(header);
  }

  document.querySelectorAll('.markdown-content .highlight').forEach((block) => {
    const codeEl = block.querySelector('td.code pre code, td.code pre, pre code, pre');
    if (codeEl) attachCodeHeader(block, codeEl);
  });

  document.querySelectorAll('.markdown-content > pre').forEach((pre) => {
    if (pre.closest('.highlight')) return;
    const codeEl = pre.querySelector('code') || pre;
    const wrapper = document.createElement('div');
    wrapper.className = 'code-block-wrapper';
    pre.parentNode.insertBefore(wrapper, pre);
    wrapper.appendChild(pre);
    attachCodeHeader(wrapper, codeEl);
  });

  /* ------------------------------------------------------------------------
     4. Terminal Search Modal (Pagefind)
     ------------------------------------------------------------------------ */
  const dialog = document.getElementById('search-dialog');
  const openBtn = document.querySelector('[data-search-open]');
  const closeBtn = document.querySelector('[data-search-close]');
  const input = document.getElementById('search-input');
  const statusEl = document.getElementById('search-status');
  const resultsEl = document.getElementById('search-results');

  let pagefind = null;
  let pagefindFailed = false;
  let debounceTimer = null;

  async function ensurePagefind() {
    if (pagefind || pagefindFailed) return pagefind;
    try {
      const mod = await import('/pagefind/pagefind.js');
      if (mod && typeof mod.init === 'function') {
        await mod.init();
      }
      pagefind = mod;
      return pagefind;
    } catch {
      pagefindFailed = true;
      if (statusEl) {
        statusEl.textContent = 'Search index unavailable (run Pagefind after build to enable search).';
      }
      return null;
    }
  }

  function renderSafeExcerpt(target, excerpt) {
    const parts = String(excerpt || '').split(/(<mark>|<\/mark>)/gi);
    let inMark = false;
    for (const part of parts) {
      const lower = part.toLowerCase();
      if (lower === '<mark>') {
        inMark = true;
        continue;
      }
      if (lower === '</mark>') {
        inMark = false;
        continue;
      }
      if (!part) continue;
      if (inMark) {
        const mark = document.createElement('mark');
        mark.textContent = part;
        target.appendChild(mark);
      } else {
        target.appendChild(document.createTextNode(part));
      }
    }
  }

  async function runSearch(query) {
    if (!resultsEl || !statusEl) return;
    const trimmed = query.trim();
    resultsEl.textContent = '';

    if (!trimmed) {
      statusEl.textContent = '';
      return;
    }

    const pf = await ensurePagefind();
    if (!pf) return;

    statusEl.textContent = 'Searching...';
    const search = await pf.search(trimmed);
    const items = await Promise.all(search.results.slice(0, 12).map((r) => r.data()));

    if (input && input.value.trim() !== trimmed) return;

    if (!items.length) {
      statusEl.textContent = `0 matches for "${trimmed}"`;
      return;
    }

    statusEl.textContent = `${search.results.length} match${search.results.length === 1 ? '' : 'es'}`;
    const frag = document.createDocumentFragment();
    for (const item of items) {
      const li = document.createElement('li');
      li.className = 'search-result-item';

      const link = document.createElement('a');
      link.className = 'search-result-link';
      link.href = item.url;

      const title = document.createElement('span');
      title.className = 'search-result-title';
      title.textContent = (item.meta && item.meta.title) || item.url;

      const excerpt = document.createElement('span');
      excerpt.className = 'search-result-excerpt';
      renderSafeExcerpt(excerpt, item.excerpt);

      link.append(title, excerpt);
      li.appendChild(link);
      frag.appendChild(li);
    }
    resultsEl.appendChild(frag);
  }

  function openSearch() {
    if (!dialog || typeof dialog.showModal !== 'function') return;
    if (!dialog.open) {
      dialog.showModal();
      ensurePagefind();
    }
    if (input) {
      input.focus();
      input.select();
    }
  }

  if (openBtn) {
    openBtn.addEventListener('click', openSearch);
  }

  if (closeBtn && dialog) {
    closeBtn.addEventListener('click', () => dialog.close());
  }

  if (dialog) {
    dialog.addEventListener('click', (event) => {
      if (event.target === dialog) dialog.close();
    });
  }

  if (input) {
    input.addEventListener('input', () => {
      clearTimeout(debounceTimer);
      debounceTimer = window.setTimeout(() => runSearch(input.value), 160);
    });
  }

  document.addEventListener('keydown', (event) => {
    const tag = event.target && event.target.tagName;
    const isTyping =
      tag === 'INPUT' ||
      tag === 'TEXTAREA' ||
      tag === 'SELECT' ||
      (event.target && event.target.isContentEditable);

    if ((event.metaKey || event.ctrlKey) && event.key.toLowerCase() === 'k') {
      event.preventDefault();
      openSearch();
      return;
    }

    if (!isTyping && event.key === '/' && !event.metaKey && !event.ctrlKey && !event.altKey) {
      event.preventDefault();
      openSearch();
    }
  });
})();
