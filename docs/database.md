# Database Architecture

Document ID: DB-DOC-001

Version: 1.0

Status: Draft

---

# 1. Purpose

This document describes the complete database architecture used by Monte Carlo Football Simulator V3.

The database is designed as an analytical warehouse optimized for football analytics rather than transactional operations.

Its primary objectives are:

- Store historical football data.
- Preserve historical snapshots.
- Support feature engineering.
- Feed predictive models.
- Enable reproducible simulations.

---

# 2. Database Philosophy

The database follows four principles.

## Principle 1

Historical data is immutable.

Records are never overwritten.

Only INSERT operations are allowed for historical information.

---

## Principle 2

The database is the Single Source of Truth.

Every module reads from DuckDB.

No module communicates directly with API-Football except the Extraction Engine.

---

## Principle 3

Every entity has a unique identifier.

Never use names as identifiers.

Use:

- fixture_id
- league_id
- team_id
- player_id
- referee_id
- stadium_id

---

## Principle 4

Feature Engineering is separated from Raw Data.

RAW

↓

PROCESSED

↓

FEATURES

---

# 3. Storage Layers

## RAW

Contains the exact API responses.

Purpose:

Reproducibility.

Never modified.

Examples:

raw_fixture

raw_player

raw_statistics

raw_lineups

---

## PROCESSED

Contains normalized football entities.

Examples:

fixtures

teams

players

team_match

player_match

---

## FEATURES

Contains calculated variables.

Examples:

attack_rating

defense_rating

player_rating

fatigue

rest_days

form

---

# 4. Entity Relationship Diagram

(To be added)

---

# 5. Naming Convention

Tables

DIM\_

FACT\_

FEATURE\_

Columns

snake_case

Identifiers

\*\_id

Dates

UTC Timestamp

Percentages

Decimal

Never strings.

---

# 6. Dimensions

DIM_LEAGUE

DB-001

DIM_TEAM

DB-002

DIM_PLAYER

DB-003

DIM_REFEREE

DB-004

DIM_STADIUM

DB-005

---

# 7. Fact Tables

FACT_FIXTURE

DB-006

FACT_TEAM_MATCH

DB-007

FACT_PLAYER_MATCH

DB-008

FACT_LINEUP

DB-009

FACT_INJURIES

DB-010

FACT_ODDS

DB-011

---

# 8. Feature Tables

TEAM_FEATURES

FEATURE-001

PLAYER_FEATURES

FEATURE-002

MATCH_FEATURES

FEATURE-003

---

# 9. Update Pipeline

API

↓

RAW

↓

Validation

↓

Transformation

↓

DuckDB

↓

Feature Engineering

↓

Simulation

---

# 10. Future Extensions

Weather

Transfer Market

Manager Ratings

Expected Goals

Travel Distance

Financial Data

Training Load
