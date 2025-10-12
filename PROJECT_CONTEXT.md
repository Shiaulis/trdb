# TPL Roster Database (TRDB) - Project Context

## Overview
A CLI application (future Discord bot) to manage and validate team rosters for The Premier League (TPL) of Hell Let Loose.

## Core Purpose
Track player IDs across all teams and enforce the fundamental rule: **Each player can only be rostered on ONE team per season.**

## Key Requirements

### 1. Player Management
- **Player ID**: Primary unique identifier (console player ID, not Steam ID)
- **Uniqueness**: System must prevent duplicate player IDs across all teams
- **Validation**: Ensure all player IDs are valid format

### 2. Team Roster Management
- Maximum roster size: 150 players per team
- No minimum enforcement (app stores up to 150)
- Track which team each player belongs to

### 3. Transfer System (Article 12.0 Rules)
- Players can transfer **once per season** between teams
- Transfer window: Opens at Week 1 start, closes after Week 1 ends
- After roster lock: No transfers allowed
- Track transfer history per player per season

### 4. Validation Rules
The app must validate:
- ✅ Player ID is not already rostered on another team
- ✅ Player has not exceeded transfer limit (1 per season)
- ✅ Team roster does not exceed 150 players
- ✅ Player ID format is valid

### 5. Division Information (Reference)
TPL has 9 divisions with different player counts per match:
- Division I-IV: 49v49 (max 49 players on field)
- Division V: 40v40 (max 40 players on field)
- Division VI-VII: 35v35 (max 35 players on field)
- Division VIII-IX: 30v30 (max 30 players on field)

**Note**: App doesn't enforce match-day limits, only roster size (150 max)

## Season Structure
- Regular season: 5-6 weeks depending on division
- Transfer window: Week 1 only
- Roster lock: After Week 1, full lock at playoffs
- Playoffs: 3 rounds (Quarterfinals, Semifinals, Finals)

## Technical Notes
- Primary identifier: Player ID (string)
- Need to track: Player ID, Team, Transfer history, Season
- CLI first, Discord bot later
- Reference document: `tpl-rulebook.pdf`

## Technology Stack
- **Language**: Python (learning project)
- **Database**: SQLite (local, built-in)
- **CLI Framework**: TBD (click/typer)
- **Future**: discord.py for bot
- **Editor**: Neovim

## Development Approach
**IMPORTANT**: This is a learning project for Python.
- User will write all code
- Claude acts as guide/reviewer only
- Verify approach and suggest corrections
- Explain concepts as needed

## Development Strategy
**Incremental, iteration-based approach** - Build understanding before adding complexity.

See `DEVELOPMENT_PLAN.md` for detailed iteration breakdown.

## Current Status
- ✅ Project structure initialized
- ✅ Git version control set up
- ✅ Dependencies identified (typer, rich)
- ✅ Spreadsheet data analyzed (66 sheets, ~5,753 players)
- 🔄 **Current**: Iteration 1 - Single ID validation
- Environment: Python 3.13, Neovim, macOS
