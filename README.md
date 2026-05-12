# sl-elt

End-to-end transit data pipeline: ingestion, transformation (dbt), and visualization.

> [!NOTE]
> This README is a placeholder. Full documentation coming in a future unit.

## A note on AI assistance
I work with Claude (Anthropic's AI assistant) as a learning partner — for explaining concepts, suggesting approaches, and reviewing my reasoning. The dynamic is closer to "pair-programming with a patient tutor" than to "AI-generated code."

Specifically:

Commands run on real infrastructure are typed by hand, not pasted. (Documentation like this one here can be copy-pasted, if I 100% agree with the draft proposed. Most often I make edits.)
Architectural decisions are mine; Claude explains trade-offs, I choose.
Each step is verified (preview-before-apply, diff-before-commit) before anything reaches production
This is not Claude Code or any other agentic AI - Claude doesn't have access to my servers
I regularly catch Claude's mistakes and push back. I ask questions about everything, including a lot of 'why', not only 'how'. My goal is learning and understanding, not copy-pasting.
The disclosure exists because how AI is used matters more than whether it's used.

===





## Status

🚧 Phase 1 — Project scaffolding

## Secrets Management

Both this project and the `dwh` Docker Compose stack share credentials via a single
`~/.secrets/.env` file. Each project's `.env` is a symlink pointing to that one source
of truth. Thanks to that we remove redundancy and have better control over the environment.

```text
~/.secrets/.env           ← single source of truth (chmod 600)
    ↑ symlink                 ↑ symlink
~/dwh/.env                ~/sl-elt/.env
```
