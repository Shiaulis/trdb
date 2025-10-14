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

### 🔄 Iteration 1: Validate Single Player ID
**Goal**: Learn string validation and basic Python functions

**Tasks**:
- [ ] Write `validate_player_id()` function in `src/validators.py`
- [ ] Handle edge cases (empty, wrong length, invalid characters)
- [ ] Write basic tests manually (no test framework yet)

**What You'll Learn**:
- String operations in Python
- Boolean logic
- Function definitions and docstrings
- Regex (optional, for hex validation)

**Validation Rules**:
- Player ID must be exactly 32 characters
- Must contain only hexadecimal characters (0-9, a-f)
- Lowercase format (based on real data)

**Success Criteria**: Function correctly identifies valid/invalid player IDs

---

### Iteration 2: Validate List of IDs
**Goal**: Work with collections and aggregation

**Tasks**:
- [ ] Write `validate_player_ids()` function
- [ ] Return a validation report (dict with counts)
- [ ] Handle empty lists, None values

**What You'll Learn**:
- Lists and iteration
- Dictionaries for structured data
- List comprehensions (optional)
- Counting and aggregation

**Output Format**:
```python
{
    "total": 150,
    "valid": 148,
    "invalid": 2,
    "invalid_ids": ["bad_id_1", "bad_id_2"]
}
```

**Success Criteria**: Can process a list and return accurate counts

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
- discord.py integration
- Bot commands mirror CLI
- Role-based permissions

---

## Key Decisions Log

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

**Last Updated**: 2025-10-12
**Current Iteration**: 1
**Next Milestone**: Single ID validation function
