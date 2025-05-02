# 🧩 Puzzle Solver — Problem & Solutions

This repository contains multiple attempts to solve a visually presented logic puzzle (initially found on LinkedIn). The problem involves assigning values or placements under certain constraints, and I’ve documented the journey of solving it through different approaches and languages.

---

## 🗂️ Repository Contents

### ✅ `check2.py`  
**Final working solution.**  
This is the main file containing the cleanest and most efficient implementation of the puzzle-solving logic using recursion and backtracking.

---

### ⚙️ `check1.py`  
**Initial non-recursive attempt (Python).**  
Tried solving the puzzle using a non-recursive method. However, the logic became overly complex due to too many conditional checks and variables. Ultimately, this approach was abandoned.

---

### 💻 `game.cpp`  
**First attempt (C++).**  
Initially approached the problem in C++, inspired by the classic **N-Queens Problem**. I assumed this puzzle could be solved by adding a few constraints to that logic. But later, it turned out that a different strategy was needed.

---

## 🎥 Demo
Press the below youtube link for a demo recording of the project.

[![YouTube](https://img.shields.io/badge/YouTube-API-red?logo=youtube)](https://youtu.be/IxvgiTc6Gro?si=5V3teykY8EVlXGpy)

## 🖼️ Visual References

| File                     | Description                                                  |
|--------------------------|--------------------------------------------------------------|
| `problem_hard.jpg`       | 🔍 Original puzzle image (from LinkedIn).                    |
| `problem_hard_numeric.jpg` | 🔢 Puzzle with blocks numbered by me for easier tracking.    |
| `solution_hard.jpg`      | ✅ My hand-solved version shared on LinkedIn.                |
| `solution2_hard.jpg`     | 🧠 Another valid solution obtained by dry-running my code.   |

> **Note:** This puzzle may have multiple valid solutions.

---
### ⏳ `Time Complexity`  
**O(N! * N)**  
We don't really need to worry about it, because here N value is always small.

---

## 📌 Notes

- This repository captures the problem-solving **evolution** — from brute-force attempts to optimized recursion.
- If you're trying to solve a similar puzzle, feel free to explore and modify the code!
- Feedback and improvements are always welcome 😊
