# 🎮 Game Glitch Investigator: The Impossible Guesser

## 🚨 The Situation

You asked an AI to build a simple "Number Guessing Game" using Streamlit.
It wrote the code, ran away, and now the game is unplayable.

* You can't win.
* The hints lie to you.
* The secret number seems to have commitment issues.

## 🛠️ Setup

1. Install dependencies: `pip install -r requirements.txt`
2. Run the app: `python -m streamlit run app.py`
3. Run tests: `python3 -m pytest tests/`

## 🕵️‍♂️ Your Mission

1. **Play the game.** Open the "Developer Debug Info" tab in the app to see the secret number and test different guesses.
2. **Find the State Bug.** I checked how the secret number, attempts, score, and history behaved when the app reran after clicking buttons.
3. **Fix the Logic.** The hints were wrong, so I fixed the comparison logic for "Too High" and "Too Low."
4. **Refactor & Test.**

   * Moved the game logic into `logic_utils.py`.
   * Updated `app.py` to use the functions from `logic_utils.py`.
   * Added pytest tests in `tests/test_game_logic.py`.
   * Ran pytest until all tests passed.

## 📝 Document Your Experience

* [x] Describe the game's purpose.
* [x] Detail which bugs you found.
* [x] Explain what fixes you applied.

The purpose of this game is to let the user guess a secret number within a limited number of attempts. The app should give feedback after each valid guess, telling the user whether the guess is too high, too low, or correct. When I first tested the game, I found that the hint logic was misleading, invalid guesses like `105` could affect the game, and some of the main logic was not properly moved into `logic_utils.py`.

I fixed the game by refactoring the core logic into `logic_utils.py`, including the difficulty range, input parsing, guess checking, hint messages, score updates, range validation, and distance labels. I also fixed the higher/lower comparison so guesses above the secret return `"Too High"` and guesses below the secret return `"Too Low"`. Finally, I added validation so out-of-range guesses are rejected and do not count as attempts. After making these changes, I tested the game manually in Streamlit and verified the logic with pytest.

## 📸 Demo Walkthrough

Describe your fixed game in numbered steps so a reader can follow along without watching a video:

1. The user starts the app by running `python -m streamlit run app.py`.
2. The game opens in the browser and shows the title, difficulty setting, guess input box, submit button, new game button, sidebar score metrics, progress bar, and Developer Debug Info panel.
3. In Normal mode, the game asks the user to guess a number between 1 and 100 with 8 attempts.
4. During testing, the user opens Developer Debug Info and sees the secret number. For example, the secret number is `75`.
5. If the user enters `105`, the app rejects the guess and shows: `Enter a number between 1 and 100.` The invalid guess does not count as an attempt.
6. If the user enters `79` when the secret number is `75`, the app correctly says the guess is too high and tells the user to go lower.
7. If the user enters `74` when the secret number is `75`, the app correctly says the guess is too low and tells the user to go higher.
8. The app also shows a hot/cold distance label such as `🔥 Very close`, `🌡️ Warm`, `🧊 Cold`, or `🥶 Very cold`.
9. When the user enters `75`, the app shows the correct message and displays the winning result.
10. The history, attempts, score, and best score update correctly for valid guesses.
11. The Guess History table shows each valid attempt with the attempt number, guess, result, hint, and distance label.

**Screenshot** *(optional)*: The fixed game was manually tested in the browser using the Developer Debug Info section.

## 🧪 Test Results

```text
python3 -m pytest tests/
====================================== test session starts ======================================
platform darwin -- Python 3.12.4, pytest-9.1.1, pluggy-1.6.0
rootdir: /Users/musharafkhanpathan/codepath101/ai110-module1show-gameglitchinvestigator-starter
plugins: anyio-4.14.0
collected 15 items

tests/test_game_logic.py ...............                                                 [100%]

======================================= 15 passed in 0.02s =======================================
```

## 🚀 Stretch Features

* [x] **Advanced Edge-Case Testing:** Added pytest cases for blank input, non-numeric strings, negative numbers, decimal input, extremely large numbers, and range validation.
* [x] **Feature Expansion via Agent Mode:** Added a Best Score tracker and a structured Guess History table.
* [x] **Professional Documentation and Style:** Added professional docstrings to all functions in `logic_utils.py` and checked style with `pycodestyle`.
* [x] **Enhanced Game UI and Formatting:** Added hot/cold distance labels, sidebar score metrics, a progress bar, and a structured Guess History table.
* [x] **AI Model or Prompt Comparison:** Documented a comparison between ChatGPT and the VS Code AI assistant in `ai_interactions.md`.

## Enhanced UI Notes

The UI enhancements are implemented mainly in `app.py` and supported by helper functions in `logic_utils.py`.

* `st.sidebar.metric()` displays Current Score and Best Score.
* `st.progress()` shows progress through the allowed attempts.
* `st.table()` displays the structured Guess History table.
* `get_distance_label()` in `logic_utils.py` returns hot/cold feedback such as `🔥 Very close`, `🌡️ Warm`, and `🥶 Very cold`.
* `hint_for_outcome()` in `logic_utils.py` returns clear user-facing hint messages.
