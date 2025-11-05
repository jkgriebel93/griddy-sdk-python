# TODO Comments Report

Generated: 2025-11-04

This report lists all TODO comments found in the codebase (excluding venv/).

---

## Summary

**Total TODOs**: 27

### By Category:
- **Pydantic Model Issues**: 11
- **Code Organization**: 3
- **Enums/Type Definitions**: 4
- **Documentation**: 3
- **API Implementation**: 4
- **Refactoring/Cleanup**: 2

---

## 1. Pydantic Model Issues (11 TODOs)

These are related to broken or incomplete Pydantic models that need fixing.

### 1.1 Broken Model Schemas

**File**: `src/griddy/nfl/endpoints/pro/stats/receiving.py:10`
```python
# TODO: All the requests in this file have broken Pydantic models
```
**Priority**: HIGH
**Impact**: Affects all receiving stats endpoints

---

**File**: `src/griddy/nfl/endpoints/pro/stats/passing.py:119`
```python
# TODO: Another borked schema
```
**Priority**: HIGH
**Impact**: Affects specific passing stats endpoint

---

**File**: `src/griddy/nfl/endpoints/pro/stats/passing.py:356`
```python
# TODO: Another bad model schema
```
**Priority**: HIGH
**Impact**: Affects specific passing stats endpoint

---

**File**: `src/griddy/nfl/endpoints/pro/stats/rushing.py:10`
```python
# TODO: All the requests in this file have broken Pydantic models
```
**Priority**: HIGH
**Impact**: Affects all rushing stats endpoints

---

**File**: `src/griddy/nfl/endpoints/pro/stats/defense.py:10`
```python
# TODO: All the requests in this file have broken Pydantic models
```
**Priority**: HIGH
**Impact**: Affects all defense stats endpoints

---

### 1.2 Unmarshaling Issues

**File**: `src/griddy/nfl/endpoints/pro/stats/team_offense.py:591`
```python
# TODO: Fix unmarshaling
```
**Context**: Season overview stats
**Priority**: MEDIUM

---

**File**: `src/griddy/nfl/endpoints/pro/stats/team_offense.py:705`
```python
# TODO: Fix unmarshaling
```
**Context**: Async season overview stats
**Priority**: MEDIUM

---

**File**: `src/griddy/nfl/endpoints/pro/stats/team_offense.py:821`
```python
# TODO: Fix unmarshaling
```
**Context**: Weekly overview stats
**Priority**: MEDIUM

---

**File**: `src/griddy/nfl/endpoints/pro/stats/team_offense.py:937`
```python
# TODO: Fix unmarshaling
```
**Context**: Async weekly overview stats
**Priority**: MEDIUM

---

**File**: `src/griddy/nfl/endpoints/pro/content.py:267`
```python
# TODO: unmarshal is borked. Fix pydantic model
```
**Priority**: MEDIUM

---

**File**: `src/griddy/nfl/endpoints/pro/mixins.py:654`
```python
# TODO: The model is busted, so unmarshaling returns an empty dict
```
**Priority**: HIGH
**Impact**: Returns empty dict instead of proper data

---

## 2. Missing/Incomplete Response Models (2 TODOs)

**File**: `src/griddy/nfl/endpoints/pro/games.py:177`
```python
# TODO: Implement the pydantic models for PlayList & related response
```
**Priority**: HIGH
**Impact**: PlayList endpoint returns unstructured data

---

**File**: `src/griddy/nfl/endpoints/pro/players.py:87`
```python
# TODO: Something is being lost in the unmarshaling process. Fix it.
```
**Priority**: HIGH
**Impact**: Data loss during unmarshaling

---

## 3. Enum/Type Definitions (4 TODOs)

**File**: `src/griddy/nfl/models/getdefensivenearestdefenderstatsbyseasonop.py:23`
```python
# TODO: Add the rest of these
```
**Context**: Sort key enum is incomplete
**Priority**: MEDIUM

---

**File**: `src/griddy/nfl/models/getdefensivenearestdefenderstatsbyweekop.py:23`
```python
# TODO: Add the rest of these
```
**Context**: Sort key enum is incomplete
**Priority**: MEDIUM

---

**File**: `src/griddy/nfl/models/getteamdefensestatsbyweekop.py:14`
```python
# TODO: Move this to an enum module
```
**Context**: Sort keys should be in separate enum file
**Priority**: LOW
**Impact**: Code organization

---

**File**: `src/griddy/nfl/models/getteamdefensestatsbyweekop.py:53`
```python
# TODO: Move this to an enum module
```
**Context**: Split enum should be in separate file
**Priority**: LOW
**Impact**: Code organization

---

**File**: `src/griddy/nfl/models/teamoffenserushstatsresponse.py:21`
```python
# TODO: Need to add enum for this
```
**Priority**: MEDIUM

---

**File**: `src/griddy/nfl/models/teamoffenserushstatsresponse.py:40`
```python
# TODO: Need to add enum for this
```
**Priority**: MEDIUM

---

## 4. Code Organization/Architecture (3 TODOs)

**File**: `src/griddy/nfl/team_offense_pass_statistics.py:11`
```python
# TODO: DELETE
```
**Priority**: HIGH
**Impact**: File should be removed (likely superseded)

---

**File**: `src/griddy/nfl/betting.py:11`
```python
# TODO: Not sure where to put this module
```
**Priority**: LOW
**Impact**: Module needs proper organization

---

**File**: `src/griddy/nfl/endpoints/pro/content.py:387`
```python
# TODO: Consider how this method signature might be cleaned up
```
**Priority**: LOW
**Impact**: API design improvement

---

## 5. Documentation/Implementation Notes (3 TODOs)

**File**: `src/griddy/nfl/endpoints/pro/content.py:433`
```python
# TODO: Note that the actual video file itself is acquired by:
```
**Type**: Documentation note
**Priority**: LOW

---

**File**: `src/griddy/nfl/endpoints/pro/content.py:802`
```python
# TODO: Note that the game_id used in this request
```
**Type**: Documentation note
**Priority**: LOW

---

**File**: `src/griddy/nfl/endpoints/pro/players.py:71`
```python
# TODO: What utility do hooks really provide for us?
```
**Type**: Architecture question
**Priority**: LOW

---

## 6. Type System Improvements (1 TODO)

**File**: `src/griddy/nfl/core/base_client.py:78`
```python
# TODO: Create a TypeVar for this return type.
```
**Priority**: LOW
**Impact**: Better type hints

---

## 7. Data Model Issues (1 TODO)

**File**: `src/griddy/nfl/endpoints/pro/stats/passing.py:30`
```python
# TODO: It turns out the NFL includes both traditional and
```
**Type**: Incomplete comment (needs investigation)
**Priority**: MEDIUM
**Note**: Comment appears to be cut off

---

## Priority Breakdown

### HIGH Priority (8 TODOs)
1. Fix broken Pydantic models in receiving.py
2. Fix broken Pydantic models in rushing.py
3. Fix broken Pydantic models in defense.py
4. Fix busted model in mixins.py (returns empty dict)
5. Implement PlayList Pydantic models
6. Fix unmarshaling data loss in players.py
7. Delete obsolete team_offense_pass_statistics.py file
8. Fix borked schema issues in passing.py (2 instances)

### MEDIUM Priority (10 TODOs)
1. Fix unmarshaling in team_offense.py (4 instances)
2. Fix borked unmarshal in content.py
3. Complete sort key enums (2 instances)
4. Add missing enums in teamoffenserushstatsresponse.py (2 instances)
5. Investigate incomplete comment in passing.py

### LOW Priority (9 TODOs)
1. Move enums to separate modules (2 instances)
2. Organize betting.py module location
3. Clean up method signature in content.py
4. Document video file acquisition
5. Document game_id usage
6. Evaluate hooks utility
7. Create TypeVar for base_client.py

---

## Recommended Actions

### Immediate (High Priority)
1. **Audit all Pydantic models** - Systematic review of all model schemas
2. **Fix critical unmarshaling issues** - Especially models returning empty dicts
3. **Remove obsolete code** - Delete team_offense_pass_statistics.py
4. **Implement missing models** - PlayList and related response models

### Short-term (Medium Priority)
1. **Complete enum definitions** - Add missing sort keys
2. **Fix unmarshaling** - Team offense stats endpoints
3. **Add missing enums** - Rush stats response models

### Long-term (Low Priority)
1. **Code organization** - Move enums to dedicated modules
2. **API design** - Clean up method signatures
3. **Documentation** - Add implementation notes
4. **Type system** - Improve type hints with TypeVars

---

## Statistics by File

| File | TODO Count | Category |
|------|------------|----------|
| endpoints/pro/stats/team_offense.py | 4 | Unmarshaling |
| endpoints/pro/content.py | 4 | Mixed |
| endpoints/pro/stats/passing.py | 3 | Models |
| getteamdefensestatsbyweekop.py | 2 | Enums |
| teamoffenserushstatsresponse.py | 2 | Enums |
| endpoints/pro/players.py | 2 | Mixed |
| endpoints/pro/stats/receiving.py | 1 | Models |
| endpoints/pro/stats/rushing.py | 1 | Models |
| endpoints/pro/stats/defense.py | 1 | Models |
| Other files | 7 | Various |

---

## Notes

- Many TODOs are related to Pydantic model schemas suggesting a systematic issue with model generation or validation
- Unmarshaling issues appear concentrated in stats endpoints
- Several enum definitions are incomplete or need reorganization
- One file is marked for deletion but still present in codebase
