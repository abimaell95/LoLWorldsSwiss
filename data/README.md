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
