# Contributing to Awesome Agent Safety

Thanks for contributing. This list is agent-specific and research-backed.

## Scope gate (must pass all three)

1. Agent-relevant: involves tool use, memory, multi-step autonomy, or agent protocols (MCP/A2A/ACP). Pure chat-LLM safety without agent content is out of scope.
2. High-signal: paper with taxonomy/benchmark/defense, maintained OSS tool, canonical incident report, or standards-body framework. No blog roundups, no marketing pages.
3. Verifiable: link opens today and supports your one-line description. arXiv links as `https://arxiv.org/abs/XXXX.XXXXX`. GitHub links to repo root or stable subtree.

## Format

```md
- [Name](https://example.com) (Maintainer, License) — One line: what it does for agents.
```

- One line per entry. Keep the line under ~200 chars.
- Order within a section: most established / most cited first.
- Commercial API-only tools: allowed only if no OSS exists for that function; label `(commercial API, no OSS repo)`.
- Archived or brand-new (<10 stars) repos: allowed with `(archived DATE — pin version)` or `(new — evaluate)`.

## PR checklist

- [ ] Entry is agent-relevant (tool/memory/autonomy/protocol).
- [ ] One-line description matches what the linked source actually says.
- [ ] Link checked (CI runs lychee; run it locally if you can).
- [ ] License noted for tools where visible.
- [ ] Placed in the right section; surveys go in Surveys with year + citations.

## What gets rejected

General LLM safety without agent content, dead links, hallucinated arXiv IDs, duplicate entries already covered, entries cited from search snippets without opening the source.
