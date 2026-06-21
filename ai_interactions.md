# AI Interactions Log

> **Stretch features only.** Only fill in the sections that apply to stretch features you attempted. If you did not attempt a stretch feature, leave its section blank or delete it. This file is not required for the core project.

---

## Agent Workflow (SF8)

> Document your experience using an AI agent (e.g., Cursor Agent, Claude, Copilot) to make multi-step changes autonomously.

**What task did you give the agent?**

I asked the AI assistant to help expand the fixed Streamlit number guessing game without breaking the core game logic. The goal was to add a meaningful feature for the bonus requirement: a Best Score tracker and a structured Guess History table. I also asked the assistant to keep the reusable game logic in `logic_utils.py`, update tests, and make sure the app still passed pytest.

**What did the agent do?**

The AI suggested storing valid guesses as dictionaries instead of plain numbers so the app could show attempt number, guess, result, hint, and distance feedback in a table. It also suggested adding `best_score` to `st.session_state`, showing score metrics in the sidebar, and adding a progress bar for attempts. The files modified were `app.py`, `logic_utils.py`, `tests/test_game_logic.py`, `README.md`, and `ai_interactions.md`.

**What did you have to verify or fix manually?**

I manually verified that invalid guesses like `105` were rejected and did not count as attempts. I also checked that valid guesses appeared in the Guess History table and that a correct guess ended the game properly. I ran `python3 -m pytest tests/` and confirmed that all 15 tests passed after the feature changes.

---

## Test Generation (SF7)

> Document how you used AI to help generate or improve tests.

| Edge Case              | Prompt Used                                                                           | AI-Suggested Test                                                                                | Did It Pass? | Your Reasoning                                                                                        |
| ---------------------- | ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------ | ------------ | ----------------------------------------------------------------------------------------------------- |
| Blank input            | "Suggest edge case pytest cases for my number guessing game input parser."            | Test that `parse_guess("")` returns `False`, no guess, and an error message.                     | Yes          | A blank guess is common user behavior and should not crash the app or count as a valid attempt.       |
| Non-numeric string     | "Suggest edge case pytest cases for my number guessing game input parser."            | Test that `parse_guess("abc")` returns an error.                                                 | Yes          | Text input should be rejected clearly instead of causing a runtime error.                             |
| Negative number        | "Suggest edge case pytest cases for parser and range validation in my guessing game." | Test that `parse_guess("-5")` parses the value, then `is_guess_in_range(-5, 1, 100)` rejects it. | Yes          | The parser can convert the value, but the app should reject it because it is outside the valid range. |
| Decimal input          | "Suggest edge case pytest cases for decimal input in my guessing game."               | Test that `parse_guess("3.14")` handles decimal input without crashing.                          | Yes          | Decimal input is a realistic user mistake, so the parser should handle it predictably.                |
| Extremely large number | "Suggest edge case pytest cases for very large number input."                         | Test that `parse_guess("999999")` parses the number, then range validation rejects it.           | Yes          | Very large inputs should not crash the parser, but they should be rejected by range validation.       |

---

## Linting & Style (SF9)

> Document your use of AI for linting or code style improvements.

**Prompt used:**

```text
Review my Streamlit game code for professional documentation and PEP 8 style. Add clear docstrings to every function in logic_utils.py and suggest any formatting changes needed for readability.
```

**Linting output before:**

```text
No PEP 8 issues reported by pycodestyle for app.py, logic_utils.py, and tests/test_game_logic.py.
```

**Changes applied:**

I added professional docstrings to every function in `logic_utils.py`, including `get_range_for_difficulty()`, `parse_guess()`, `is_guess_in_range()`, `check_guess()`, `hint_for_outcome()`, `get_distance_label()`, and `update_score()`. I also organized imports in `app.py`, kept helper logic out of the UI file when possible, and used descriptive function names. I verified the style check by running `pycodestyle` and saving the result in `style_report.txt`.

---

## Model Comparison (SF11)

> Compare two AI models on the same task.

**Task given to both models:**

Fix the number guessing game bug where the hint logic gave the wrong direction after a guess. For example, if the secret is `50` and the user guesses `60`, the game should return `"Too High"` and tell the user to go lower.

|                          | Model A                                                                                                                   | Model B                                                                                                                                         |
| ------------------------ | ------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------- |
| **Model name**           | ChatGPT                                                                                                                   | VS Code AI Assistant                                                                                                                            |
| **Response summary**     | Suggested separating `check_guess()` into `logic_utils.py` and comparing the numeric guess directly to the secret number. | Suggested checking the current `check_guess()` logic and updating the Streamlit app to call the helper function.                                |
| **More Pythonic?**       | ChatGPT                                                                                                                   | ChatGPT gave the cleaner helper-function approach with simple return values like `"Win"`, `"Too High"`, and `"Too Low"`.                        |
| **Clearer explanation?** | ChatGPT                                                                                                                   | ChatGPT explained why the comparison should be based on `guess > secret` and `guess < secret`, which made the bug easier to verify with pytest. |

**Which did you prefer and why?**

I preferred ChatGPT's explanation because it connected the bug, the code-level cause, and the test case more clearly. The VS Code AI assistant was useful for workflow suggestions and applying edits, but ChatGPT's answer was easier to turn into simple pytest tests.
