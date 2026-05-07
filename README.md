# Unit Testing — Lesson Task

This repository is your starter for the lesson task on unit testing with `pytest`.

Earlier in the lesson, Bob implemented and tested the first validation helper:

```python
validate_non_negative(value)
```

Your job is to implement the second validation helper and write the tests for it yourself.

## Your Task

Implement the following function in `src/validation.py`:

```python
validate_percentage(value)
```

The function must follow these rules:

- The value must be between 0 and 100 (inclusive)
- If the value is valid, return `True`
- If the value is invalid, raise a `ValueError`

Add your tests to `tests/test_validation.py`, alongside the existing tests.

Your tests should cover:

- a valid value inside the range
- the lower boundary of the range (0)
- the upper boundary of the range (100)
- a value below the valid range
- a value above the valid range

## Project Structure

```
devops-python-lesson-task-0102-starter
│
├─ src/
│   └─ validation.py        ← add your function here
│
├─ tests/
│   └─ test_validation.py   ← add your tests here
│
└─ pytest.ini
```

## Installing Dependencies

```
python3 -m pip install pytest
```

## Running the Tests

From the project root directory, run:

```
python3 -m pytest
```

When everything is working, you should see all tests pass:

```
tests/test_validation.py .....                           [100%]

5 passed in 0.02s
```

The number of passing tests will depend on how many test cases you write.