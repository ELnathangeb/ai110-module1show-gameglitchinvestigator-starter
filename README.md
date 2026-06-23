# 🎮 Game Glitch Investigator: The Impossible Guesser

## 🚨 The Situation

You asked an AI to build a simple "Number Guessing Game" using Streamlit.
It wrote the code, ran away, and now the game is unplayable. 

- You can't win.
- The hints lie to you.
- The secret number seems to have commitment issues.

## 🛠️ Setup

1. Install dependencies: `pip install -r requirements.txt`
2. Run the broken app: `python -m streamlit run app.py`

## 🕵️‍♂️ Your Mission

1. **Play the game.** Open the "Developer Debug Info" tab in the app to see the secret number. Try to win.
2. **Find the State Bug.** Why does the secret number change every time you click "Submit"? Ask ChatGPT: *"How do I keep a variable from resetting in Streamlit when I click a button?"*
3. **Fix the Logic.** The hints ("Higher/Lower") are wrong. Fix them.
4. **Refactor & Test.** - Move the logic into `logic_utils.py`.
   - Run `pytest` in your terminal.
   - Keep fixing until all tests pass!

## 📝 Document Your Experience

- [ ] Describe the game's purpose.
The purpose of the game is to let the user guess a secret number between 1 and 100. After each guess, the game gives a hint telling the user to go higher or lower until they find the correct number.
- [ ] Detail which bugs you found.
I found that the hint logic was reversed. When the guess was too high, the game told the user to go higher, and when the guess was too low, it told the user to go lower. I also found that out-of-range guesses like 1000 were not being rejected correctly. The New Game button also did not reset the game correctly at first.

- [ ] Explain what fixes you applied.
I fixed the high/low hint logic so the game gives the correct message. I added validation so guesses outside 1 to 100 are rejected. I also fixed the New Game button so it resets the secret number and game state correctly. Finally, I added pytest tests and confirmed that all 6 tests passed.

## 📸 Demo Walkthrough

Describe your fixed game in numbered steps so a reader can follow along without watching a video:

1. User starts a new game.
2. User enters 20.
3. Game returns "Go HIGHER".
4. User enters 50.
5. Game returns "Go LOWER".
6. User enters the correct number.
7. Game displays a win message.

**Screenshot** *(optional)*: <!-- Insert a screenshot of your fixed, winning game here -->

## 🧪 Test Results

```
platform darwin -- Python 3.9.13, pytest-8.4.2, pluggy-1.6.0
rootdir: /Users/elnathangebrekristos/Desktop/IC/ai110-module1show-gameglitchinvestigator-starter
collected 6 items                                                                                                                                                                                                                

tests/test_game_logic.py ......                                                                                                                                                                                            [100%]

======================================================================================================= 6 passed in 0.02s ========================================================================================================
```

## 🚀 Stretch Features

- [ ] [If you choose to complete Challenge 4, describe the Enhanced UI changes here — a screenshot is optional]
