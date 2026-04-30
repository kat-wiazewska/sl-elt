# sl-elt

End-to-end transit data pipeline: ingestion, transformation (dbt), and visualization.

> [!NOTE]
> This README is a placeholder. Full documentation coming in a future unit.

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
