# LoL Worlds Swiss Stage Effectiveness Analysis (2023-2025)

This repository contains a Python script and analysis of the League of Legends World Championship Swiss Stage format used from 2023 to 2025.

The goal of this analysis is to evaluate the effectiveness and fairness of the Swiss system by moving beyond simple Win/Loss records. It introduces a custom **Strength of Schedule (SoS) Metric** to provide a more nuanced understanding of each team's performance based on the quality of their opponents.

## The "Strength of Schedule" (SoS) Metric

The core of this analysis is a custom metric that calculates a team's score. This score is composed of two parts: a **Main Score** and a **Collateral Score**.

### 1. Main Score
This is a team's basic win/loss record, expressed as a single number:
* **+1** for every win
* **-1** for every loss

*(Example: A 3-2 team has a Main Score of +1. A 2-3 team has a Main Score of -1.)*

### 2. Collateral Score (SoS Adjustment)
This is where the metric reveals true strength. A team's score is continuously adjusted based on the **future performance of its past opponents**.

This logic is applied cumulatively after every match:

* **If you WIN against an Opponent:**
    * ...and that Opponent **WINS** a future match $\rightarrow$ **+1 to your score**. This validates your win; you beat a strong, winning team.
    * ...and that Opponent **LOSES** a future match $\rightarrow$ **+0 to your score**.

* **If you LOSE against an Opponent:**
    * ...and that Opponent **WINS** a future match $\rightarrow$ **+0 to your score**. Your loss is "justified" as you lost to a strong team.
    * ...and that Opponent **LOSES** a future match $\rightarrow$ **-1 to your score**. This penalizes your loss; you lost to a weak, losing team.

This system rewards teams that win difficult matches and penalizes teams that lose easy ones, providing a "true" performance score.

## Data Format

The Python script (`calculate_metric.py` or similar) expects a `.csv` file with a precise structure. The data must contain one row per match.

**Required Columns:**

* `Round`: The integer representing the Swiss round (1, 2, 3, 4, or 5).
* `Team 1`: The string name of the first team.
* `Team 2`: The string name of the second team.
* `Pool`: (Informational) The match-up pool (e.g., "0-0", "2-1").
* `WIN`: The string name of the team that won the match.

**Example:**
```csv
Round,Team 1,Team 2,Pool,WIN
1,T1,TL,0-0,T1
1,C9,MAD,0-0,C9
2,C9,LNG,1-0,LNG
2,GEN,T1,1-0,GEN
