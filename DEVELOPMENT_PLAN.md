# TPL Roster Database - Development Plan

## Philosophy
Build incrementally. Understand each piece before adding complexity. This is a **learning project** - focus on understanding Python concepts, not rushing to a finished product.

---

## Iteration Roadmap

### ✅ Iteration 0: Project Setup
**Goal**: Establish development environment and project structure

- [x] Create Python virtual environment
- [x] Set up project structure (src/, tests/, docs/)
- [x] Initialize Git repository
- [x] Analyze existing spreadsheet data
- [x] Define requirements (typer, rich)

**Key Learnings**:
- Python project structure
- Virtual environments
- Git basics

---

### ✅ Iteration 1: Validate Single Player ID
**Goal**: Learn string validation and basic Python functions

**Tasks**:
- [x] Write `validate_player_id()` function in `src/validators.py`
- [x] Handle edge cases (empty, wrong length, invalid characters)
- [x] Write tests with pytest (6 comprehensive tests)
- [x] Implement CLI with Typer and Rich
- [x] Add proper hex validation using int(player_id, 16)
- [x] Add documentation and docstrings

**What You'll Learn**:
- String operations in Python
- Boolean logic
- Function definitions and docstrings
- Try/except error handling
- Testing with pytest
- CLI with Typer
- Colored output with Rich

**Validation Rules**:
- Player ID must be exactly 32 characters
- Must contain only hexadecimal characters (0-9, a-f)
- Lowercase format (based on real data)

**Success Criteria**: ✅ Function correctly identifies valid/invalid player IDs
**Completed**: 2025-10-15

---

### ✅ Iteration 2: CSV Validation with ValidationReport
**Goal**: CSV parsing, data models, and validation reporting

**Tasks**:
- [x] Create `Player` model class
- [x] Create `ValidationReport` model class with computed properties
- [x] Write `validate_players()` function
- [x] Implement `read_players()` CSV reader
- [x] Store invalid players (not just IDs) for better error reporting
- [ ] Create formatters for CLI output (Rich)
- [ ] Create formatters for Discord output (future)

**What You'll Learn**:
- Class design in Python
- Type hints and annotations
- Computed properties with `@property` decorator
- CSV file parsing
- Separation of concerns (models vs. formatters)

**Architecture Decision**:
Models are UI-agnostic (no `print()` methods). Formatting is handled by separate formatter modules.

**ValidationReport Design**:
```python
class ValidationReport:
    total_count: int
    invalid_players: list[Player]

    @property
    def valid_count(self) -> int

    @property
    def invalid_count(self) -> int
```

**Success Criteria**: ✅ Can read CSV and generate validation report with full player data
**Completed**: 2025-10-19 (core models and validation)

---

### Iteration 3: CSV Import + Duplicate Detection (Single Team)
**Goal**: File I/O, CSV parsing, duplicate detection

**Tasks**:
- [ ] Read CSV file (player_id, player_name columns)
- [ ] Validate all IDs
- [ ] Detect duplicates within the file
- [ ] Generate comprehensive report
- [ ] Create simple CLI command to run validation

**What You'll Learn**:
- File I/O (`open()`, `with` statement)
- CSV module
- Sets for duplicate detection
- CLI basics with typer
- Pretty output with rich

**Output Format**:
```
Validation Report for Team: 6th
================================
Total entries:      150
Valid IDs:          148
Invalid IDs:        2
Duplicates:         3
Unique players:     145

Invalid IDs:
  - invalid_id_1
  - invalid_id_2

Duplicate IDs:
  - abc123... (appears 2 times)
  - def456... (appears 2 times)
```

**Success Criteria**: Can import a CSV and detect all issues without database

---

### Iteration 4: Database Integration + Multi-Team Validation
**Goal**: Persistence with SQLite, cross-team duplicate detection

**Tasks**:
- [ ] Design simple database schema (players table)
- [ ] Create `src/database.py` with connection handling
- [ ] Implement `init` command to create database
- [ ] Implement `import` command to add team roster
- [ ] Validate against existing database records
- [ ] Implement `list` command to view stored data

**What You'll Learn**:
- SQLite basics
- SQL CREATE, INSERT, SELECT statements
- Database connections and cursors
- UNIQUE constraints
- Transaction handling

**Database Schema**:
```sql
CREATE TABLE players (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    player_id TEXT NOT NULL UNIQUE,
    player_name TEXT,
    team_name TEXT,
    added_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

**Commands**:
- `trdb init` - Initialize database
- `trdb import <csv_file> --team <team_name>` - Import roster
- `trdb list --team <team_name>` - List team roster
- `trdb validate <csv_file>` - Check for duplicates without importing

**Success Criteria**: Can store rosters and prevent duplicate players across teams

---

## Future Iterations (Post-MVP)

### Iteration 5: Enhanced Data Model
- Separate teams table
- Proper foreign key relationships
- Division tracking

### Iteration 6: Transfer System
- Transfers table
- Transfer validation (1 per season limit)
- Transfer history tracking

### Iteration 7: Season Management
- Multiple seasons support
- Season-specific validation
- Historical data

### Iteration 8: Discord Bot Integration
**Goal**: Add Discord interface using the same core validation logic

**Tasks**:
- [ ] Create `src/bot/` directory for Discord-specific code
- [ ] Implement Discord bot with discord.py
- [ ] Create `bot/formatters.py` for Discord message formatting
- [ ] Add file upload handling for CSV rosters
- [ ] Implement bot commands (validate, help)
- [ ] Deploy bot to server

**Architecture**:
Reuse `src/core/` validation logic. Only formatting differs between CLI and Discord.

**Note**: Both CLI and Discord bot will be supported as different interfaces to the same validation engine.

---

## Key Decisions Log

### Architecture: Layered Structure (2025-10-19)
**Decision**: Use layered architecture in single repository

**Structure**:
```
trdb/
├── src/
│   ├── core/          # Business logic (UI-agnostic)
│   │   ├── models.py
│   │   ├── validators.py
│   │   └── database.py
│   ├── cli/           # CLI interface
│   │   ├── commands.py
│   │   └── formatters.py
│   └── bot/           # Discord interface (future)
│       ├── discord_bot.py
│       └── formatters.py
├── main_cli.py
└── main_bot.py
```

**Rationale**:
- Core validation logic is reusable between CLI and Discord
- Easy to develop both in same codebase
- Clean separation of concerns
- Models are UI-agnostic (no print methods)
- Each interface has its own formatter

### Dual Interface: CLI + Discord Bot (2025-10-19)
**Decision**: Support both CLI and Discord bot interfaces

**Why both?**
- CLI: Perfect for league admins, power users, automation, local testing
- Discord: Perfect for teams, less technical users, interactive experience
- Both use the same core validation engine
- Provides flexibility for different use cases

**Development approach**:
- Build CLI first (easier to test during development)
- Add Discord bot later using same core logic
- Keep both maintained as separate interfaces

### Package Management: pip over Poetry (2025-10-19)
**Decision**: Migrate from Poetry to pip

**Rationale**:
- Simpler for learning project
- Standard Python tooling
- No version constraints in requirements.txt (always latest)
- Less tooling overhead
- Easy to understand for Python beginners

**Trade-off**: Builds aren't reproducible, but acceptable for learning project

### Why start without database?
- Easier to test and debug
- Focus on core logic first
- Learn Python basics before SQL
- Can validate approach with real data quickly

### Why single season for MVP?
- Reduces complexity significantly
- Can add season support later
- Current need is single-season validation

### Why typer over argparse/click?
- Modern, type-hint based
- Great for learning
- Excellent documentation
- Built on click (can migrate if needed)

### Why SQLite?
- Built into Python
- No setup required
- Perfect for local CLI tool
- Can migrate to PostgreSQL later if needed

---

## Testing Strategy

**Iterations 1-3**: Manual testing
- Run functions with sample data
- Print outputs, verify correctness
- Focus on understanding, not test frameworks

**Iteration 4+**: Introduce pytest
- Once comfortable with Python basics
- Test database operations
- Test validation logic
- Test CLI commands

---

## Resources & References

- Python CSV module: https://docs.python.org/3/library/csv.html
- SQLite in Python: https://docs.python.org/3/library/sqlite3.html
- Typer documentation: https://typer.tiangolo.com/
- Rich documentation: https://rich.readthedocs.io/

---

**Last Updated**: 2025-10-19
**Current Iteration**: 2 (CSV validation with ValidationReport - core models complete)
**Next Milestone**: Create formatters and test validation with real CSV data
**Architecture**: Layered structure with support for both CLI and Discord bot interfaces
