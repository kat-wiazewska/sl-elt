# sl-elt

> End-to-end ELT data pipeline for Stockholm public transport — using APIs from [Trafiklab](https://trafiklab.se).

### Status
> Phase 1 (static GTFS pipeline for Stockholm) is live.
> Phase 2 (Stockholm realtime data, delay analysis): in development.
> Planned: extension to Helsinki & Vienna.

### What
`sl-elt` ingests Stockholm public transit (GTFS) data into a self-hosted PostgreSQL data warehouse, transforms it with dbt, and surfaces operational metrics in Grafana. The entire stack runs on a single Hetzner VPS, automated daily via cron, and is set up with attention to detail, conscious architectural choices, good security practices, and observability from day one.

A longer-term arc extends this to three cities — Stockholm, Helsinki, and Vienna — each demonstrating a distinct ingestion pattern: scheduled protobuf pull, MQTT push streaming, and REST API pull. One unified dbt project sits downstream, enabling cross-city comparison of metrics such as delays — the difference between the static timetable and the real-time state of things.

### Why
While the main objectives here are my own development and a satisfying portfolio piece, I hope that at a later stage it may also serve as a small case study presenting three distinct architectures used to describe the same kind of living — and very literally moving — system.

### A note on AI assistance
I work with Claude (Anthropic's AI assistant) as a learning partner — for explaining concepts, suggesting approaches, and reviewing my reasoning. The dynamic is closer to "pair-programming with a patient tutor" than to "AI-generated code."

Specifically:
Commands run on real infrastructure are typed by hand, not pasted. (Documentation like this one here can be copy-pasted, if I 100% agree with the draft proposed. Most often I make edits.)
Architectural decisions are mine; Claude explains trade-offs, I choose.
Each step is verified (preview-before-apply, diff-before-commit) before anything reaches production
This is not Claude Code or any other agentic AI - Claude doesn't have access to my servers
I regularly catch Claude's mistakes and push back. I ask questions about everything, including a lot of 'why', not only 'how'. My goal is learning and understanding, not copy-pasting.
The disclosure exists because how AI is used matters more than whether it's used.



===

### Secrets Management

Both this project and the `dwh` Docker Compose stack share credentials via a single
`~/.secrets/.env` file. Each project's `.env` is a symlink pointing to that one source
of truth. Thanks to that we remove redundancy and have better control over the environment.

```text
~/.secrets/.env           ← single source of truth (chmod 600)
    ↑ symlink                 ↑ symlink
~/dwh/.env                ~/sl-elt/.env
```
