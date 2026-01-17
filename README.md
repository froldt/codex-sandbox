# Dice Game Sandbox

This repository is a minimal sandbox that documents a simple dice game. The game is built around
rolling two six-sided dice and comparing the total to a target value to determine a win or loss.
The sections below explain the full mechanism so that the rules are clear without reading any code.

## Game Mechanism

1. **Setup**
   - The player chooses a target number between **2** and **12** (inclusive).
   - The game uses **two standard six-sided dice** (values 1 through 6).

2. **Rolling the Dice**
   - Each die is rolled once per round.
   - The values are added together to produce a **total** between **2** and **12**.

3. **Win/Loss Resolution**
   - If the total **matches the chosen target**, the player wins the round.
   - If the total **does not match**, the player loses the round.

4. **Odds and Feedback**
   - The game can optionally show the odds of rolling the chosen target. For example:
     - **7** is the most likely total (6 ways to roll it).
     - **2** and **12** are the least likely totals (1 way each).
   - This makes the game a mix of luck (random rolls) and strategy (choosing a target with
     different probabilities).

## Example Round

- The player selects **9** as the target.
- The dice are rolled: **4** and **5**.
- The total is **9**, so the player wins.

## Why This Mechanism Matters

The core of the game is the probability distribution of two dice. Totals in the middle of the
range (like 6, 7, 8) are more likely than totals on the edges (2 or 12). Choosing a target is a
risk/reward decision: harder targets pay off less often, while safer targets hit more frequently.

## Repository Contents

- `README.md`: Explains the dice game rules and mechanics.
- `PROJECT_OVERVIEW.txt`: A concise outline of the project structure and intent.
