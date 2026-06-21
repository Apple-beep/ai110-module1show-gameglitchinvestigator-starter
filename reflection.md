# 💭 Reflection: Game Glitch Investigator

**Date:** June 20, 2026

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- Answer: The first time I ran the game, it looked like a normal Streamlit number guessing game with a title, difficulty setting, guess input box, submit button, new game button, and a Developer Debug Info section. The debug panel showed the secret number, attempts, score, difficulty, and guess history, which helped me compare what the game was saying against the actual secret. I noticed that the hint logic was wrong because the game seemed to give feedback based around 100 instead of the real secret number. I also noticed that guesses outside the allowed range, such as 105, could still appear in the guess history, which should not happen in a game that says the range is 1 to 100.
- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").

**Bug Reproduction Log**

**Bug 1:**
- Input: Secret was 57, guessed 50
- Expected Behavior: Since 50 is lower than 57, the game should tell me to guess higher.
- Actual Behavior: The game gave misleading feedback and acted like guesses below 100 should go lower.
- Console Output / Error: none

**Bug 2:**
- Input: Secret was 57, guessed 56
- Expected Behavior: Since 56 is lower than 57, the game should tell me to guess higher.
- Actual Behavior: The hint was still incorrect even though the guess was very close to the secret number.
- Console Output / Error: none

**Bug 3:**
- Input: Secret was 57, guessed 100
- Expected Behavior: Since 100 is higher than 57, the game should tell me to guess lower.
- Actual Behavior: The feedback appeared to use the wrong comparison logic instead of comparing the guess to the secret number.
- Console Output / Error: none

**Bug 4:**
- Input: Secret was 57, guessed 105
- Expected Behavior: The game should reject 105 because the allowed range is 1 to 100.
- Actual Behavior: The game accepted 105 into the history and counted it as part of the game flow.
- Console Output / Error: none
---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).

- Answer: I used ChatGPT as my AI teammate to help me understand what the assignment was asking for and to organize my debugging process step by step. A correct suggestion from AI was to use the Developer Debug Info section to compare the visible secret number with the hints shown after each guess. I verified that suggestion by opening the debug panel, checking that the secret was 57, and then testing guesses like 50, 56, 100, and 105. One misleading suggestion was assuming too early that the secret number definitely changed every time I clicked submit, but my actual test run showed that the more obvious bug was the broken hint and range logic, so I corrected my notes based on what I personally observed.

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?

- Answer: I decided a bug was really fixed only when the same inputs that failed before started producing the correct behavior. For example, if the secret number is 57, a guess of 50 should return a “too low” message, a guess of 100 should return a “too high” message, and a guess of 105 should be rejected as outside the valid range. I used manual testing first because it helped me clearly see the broken behavior in the live Streamlit app before changing the code. AI helped me turn those manual cases into test ideas by identifying what each test should compare: the guess, the secret number, and the expected result.

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

- Answer: I learned that Streamlit reruns the Python script from top to bottom whenever the user interacts with the app, such as clicking a button or submitting input. This means normal variables can reset unless they are stored somewhere persistent. st.session_state is important because it lets the app remember values like the secret number, score, attempts, and game history across reruns. I would explain it to a friend by saying Streamlit forgets regular variables after every click unless you put them in session state, which acts like the app’s memory.
---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.

- Answer: One habit I want to reuse in future projects is writing down the exact input, expected behavior, and actual behavior before trying to fix anything. This made the debugging process more organized and stopped me from guessing randomly at the code, which is usually how bugs multiply like unpaid internships. Next time I work with AI on a coding task, I would give it the actual bug reproduction table first instead of asking a broad question. This project changed the way I think about AI-generated code because I saw that AI can produce code that looks polished but still has broken logic, so I need to test and verify everything instead of trusting it automatically.
