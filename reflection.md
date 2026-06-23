# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").
I noticed that the hint logic was reversed. When the secret number was 30 and I guessed 50, the game told me "Go HIGHER!" even though 50 is already higher than 30. It should have told me to go lower.I also noticed the same issue in the other direction. When the secret number was 30 and I guessed 20, the game told me "Go LOWER!" even though 20 is lower than 30. It should have told me to go higher.Invalid text input worked correctly. When I entered "abc", the game told me it was not a number instead of crashing. A large out-of-range number also behaved incorrectly. When I entered 1000, the game told me to go higher, even though 1000 is outside the allowed range of 1 to 100.

**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

| Input | Expected Behavior | Actual Behavior | Console Output / Error |
|-------|-------------------|-----------------|------------------------|
| 50|when secret number was 30 |Game should say "Go LOWER!" |Game said "Go HIGHER!" |none |
| 20|When the secrenymber was 30 |Game should say "go Higher" | game asid go lower | none
| 1000| game should reject it as out of range or say it must be be between 1 and 100 |game said "go higher" | |

---

## 2. How did you use AI as a teammate?

I used Claude Code on this project. One correct suggestion was identifying that the hint logic was reversed. Claude helped me find the comparison that was causing the game to give the wrong hints. I verified the fix by running the game and testing guesses above and below the secret number.

One misleading suggestion was making larger code changes than necessary for a simple bug fix. Before accepting the changes, I reviewed the code and focused only on the parts related to the bug. This showed me that AI suggestions should always be reviewed carefully before applying them.

---

## 3. Debugging and testing your fixes

I decided a bug was fixed by running the game and testing the same inputs that originally caused problems. For example, when the secret number was 30, a guess of 50 correctly showed "Go LOWER" and a guess of 20 correctly showed "Go HIGHER."

I also ran pytest to test the game logic. All six tests passed successfully, which confirmed that the fixes were working correctly. Claude Code helped me create and understand some of the test cases.

---

## 4. What did you learn about Streamlit and state?

I learned that Streamlit reruns the app whenever a user interacts with it. Session state is used to save information such as the secret number, score, and attempts so that the game does not reset every time the app reruns.

---

## 5. Looking ahead: your developer habits

One habit I want to reuse is testing bugs before and after making changes to make sure they are actually fixed. Next time, I will spend more time reviewing AI suggestions before accepting them.

This project showed me that AI-generated code can be helpful, but it can also contain bugs. Developers should always test and verify AI-generated code before trusting it.
