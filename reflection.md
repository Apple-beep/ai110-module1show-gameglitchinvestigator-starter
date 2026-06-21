# 💭 Reflection: Game Glitch Investigator

**Date:** June 20, 2026

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

The first time I ran the game, it looked like a normal Streamlit number guessing game with a title, difficulty setting, guess input box, submit button, new game button, and a Developer Debug Info section. The debug panel showed the secret number, attempts, score, difficulty, and guess history, which helped me compare what the game was saying against the actual secret. I noticed that the hint logic was wrong because the game seemed to give feedback based around 100 instead of the real secret number. I also noticed that guesses outside the allowed range, such as 105, could still appear in the guess history, which should not happen in a game that says the range is 1 to 100.

**Bug Reproduction Log**

| Input                      | Expected Behavior                                                    | Actual Behavior                                                                                              | Console Output / Error |
| -------------------------- | -------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------ | ---------------------- |
| Secret was 57, guessed 50  | Since 50 is lower than 57, the game should tell me to guess higher.  | The game gave misleading feedback and acted like guesses below 100 should go lower.                          | none                   |
| Secret was 57, guessed 56  | Since 56 is lower than 57, the game should tell me to guess higher.  | The hint was still incorrect even though the guess was very close to the secret number.                      | none                   |
| Secret was 57, guessed 100 | Since 100 is higher than 57, the game should tell me to guess lower. | The feedback appeared to use the wrong comparison logic instead of comparing the guess to the secret number. | none                   |
| Secret was 57, guessed 105 | The game should reject 105 because the allowed range is 1 to 100.    | The game accepted 105 into the history and counted it as part of the game flow.                              | none                   |

---

## 2. How did you use AI as a teammate?

I used ChatGPT and the AI assistant in VS Code to help me understand the assignment, plan the fixes, and organize the debugging steps. A correct AI suggestion was to use the Developer Debug Info section to compare the real secret number with the hints shown after each guess. I verified that by opening the debug panel and testing guesses like 50, 56, 100, and 105 when the secret number was 57. One incorrect or misleading suggestion was writing tests that checked `result[0]`, assuming `check_guess()` returned a tuple, but my function returned a string, so the tests compared only the first character like `"W"` or `"T"`; I verified the problem by reading the pytest failure output and fixed the tests to compare the full returned string.

---

## 3. Debugging and testing your fixes

I decided a bug was fixed only when the same inputs that failed before started producing the correct behavior. For example, I manually tested that a guess below the secret told the user to go higher, a guess above the secret told the user to go lower, and an invalid guess like 105 was rejected without counting as an attempt. I also ran `python3 -m pytest tests/` and confirmed that all 7 tests passed. AI helped me design the tests by turning my manual bug cases into simple checks for `check_guess()`, `parse_guess()`, and `get_range_for_difficulty()`.

---

## 4. What did you learn about Streamlit and state?

I learned that Streamlit reruns the Python script from top to bottom whenever the user interacts with the app, such as clicking a button or submitting input. This means normal variables can reset unless they are stored somewhere persistent. `st.session_state` is important because it lets the app remember values like the secret number, score, attempts, and game history across reruns. I would explain it to a friend by saying Streamlit forgets regular variables after every click unless you put them in session state, which acts like the app’s memory.

---

## 5. Looking ahead: your developer habits

One habit I want to reuse in future projects is writing down the exact input, expected behavior, and actual behavior before trying to fix anything. This made the debugging process more organized and stopped me from randomly guessing where the bug was. Next time I work with AI on a coding task, I would give it the actual bug reproduction table first instead of asking a broad question. This project changed the way I think about AI-generated code because I saw that AI can produce code that looks polished but still has broken logic, so I need to test and verify everything instead of trusting it automatically.
