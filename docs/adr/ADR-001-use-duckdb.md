# ADR-001 — Use DuckDB as Primary Database

- **Status:** Accepted
- **Date:** 2026-06-29

---

# Context

Monte Carlo Football Simulator V3 requires a database capable of storing large volumes of football data while remaining lightweight, portable and optimized for analytical workloads.

The platform will store:

- Multiple leagues
- Multiple seasons
- Teams
- Players
- Match statistics
- Historical features
- Predictions
- Betting data

The solution must also support SQL queries, Parquet integration and local execution without requiring a server.

---

# Decision

DuckDB has been selected as the primary database engine.

The architecture will follow three storage layers:

RAW → PROCESSED → FEATURES

DuckDB will be responsible for:

- Historical storage
- Feature storage
- Model input
- Analytical queries

---

# Alternatives Considered

## SQLite

Advantages

- Extremely lightweight

Disadvantages

- Worse analytical performance
- Poor Parquet integration

Rejected.

---

## PostgreSQL

Advantages

- Enterprise ready

Disadvantages

- Requires server administration
- Unnecessary complexity for local analytical workflows

Rejected.

---

## DuckDB

Advantages

- Native analytical engine
- Excellent Parquet support
- Extremely fast
- SQL compatible
- Single file database

Selected.

---

# Consequences

Positive

- High analytical performance
- Portable database
- Easy backups
- Excellent Python integration

Negative

- Not intended for multi-user concurrent writes

This limitation is acceptable because Monte Carlo V3 is an offline analytical platform.
