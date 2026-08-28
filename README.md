# Debugging Exercise: Fixing a ZeroDivisionError in a Grade Processing Script

## Problem
A script that calculates average grades for a list of students was crashing
when a student had no recorded scores.

## Original (buggy) code
```python
def calculate_average(scores):
    total = 0
    for score in scores:
        total += score
    return total / len(scores)

def process_student_grades(students):
    results = {}
    for name, scores in students.items():
        results[name] = calculate_average(scores)
    return results

data = {
    "Alice": [85, 90, 78],
    "Bob": [],
    "Charlie": [70, 88, 92]
}

print(process_student_grades(data))
```

## Traceback
```
Traceback (most recent call last):
  File "debug_demo.py", line 19, in <module>
    print(process_student_grades(data))
  File "debug_demo.py", line 10, in process_student_grades
    results[name] = calculate_average(scores)
  File "debug_demo.py", line 5, in calculate_average
    return total / len(scores)
ZeroDivisionError: division by zero
```

## Diagnosis
- Read the traceback bottom-up: the actual error is `ZeroDivisionError: division by zero`.
- It occurs in `calculate_average`, called with `scores` for `"Bob"`.
- Root cause: Bob's score list is empty, so `len(scores)` is `0`.

## Fix
Guard against the empty-list case before dividing, and use Python's `logging`
module to flag the anomaly instead of silently hiding it or crashing.

```python
import logging

logging.basicConfig(level=logging.WARNING, format="%(levelname)s: %(message)s")

def calculate_average(scores):
    if not scores:
        logging.warning("Empty scores list received — skipping average calculation")
        return None
    total = 0
    for score in scores:
        total += score
    return total / len(scores)

def process_student_grades(students):
    results = {}
    for name, scores in students.items():
        avg = calculate_average(scores)
        if avg is None:
            logging.warning(f"No scores on record for '{name}'")
        results[name] = avg
    return results

data = {
    "Alice": [85, 90, 78],
    "Bob": [],
    "Charlie": [70, 88, 92]
}

print(process_student_grades(data))
```

## Result
```
WARNING: Empty scores list received — skipping average calculation
WARNING: No scores on record for 'Bob'
{'Alice': 84.33333333333333, 'Bob': None, 'Charlie': 83.33333333333333}
```

## Takeaway
- No crash — the script completes and returns results for every student.
- `Bob`'s missing data is now surfaced as `None`, not silently defaulted to
  a misleading `0`, and it's logged so the anomaly is visible for future
  debugging.
- This mirrors real support-engineer practice: don't let bad or missing
  input crash the whole process, but don't hide the gap either — log it so
  it can be investigated.

## Resume/portfolio line
Debugged a `ZeroDivisionError` in a grade-processing script by tracing the
failing call via the traceback, identified missing input data as the root
cause, and implemented a fix using Python's `logging` module to flag
anomalies instead of crashing.
