# Decision Making Tool

A simple command-line Python program to help compare options using weighted criteria.

---

## How It Works

1. Enter the **decision name**.  
2. Enter the **options** you are choosing between.  
3. Enter **criteria** and assign a **weight** to each (1–10).  
4. For each option, assign a **score** (0–10) for every criterion.  
5. The program calculates a **weighted score** for each option and shows:  
   - Best option  
   - Total score  
   - Breakdown per option

---

## Requirements

- Python 3  
- No extra libraries

---

## Usage

Run the program:

```bash
python decision_making.py
Example input/output:

markdown
Copy code
Write the Decision Name:
> Should I take the new job?

How many options do you have?:
> 2

Enter option 1:
> Current Job
Enter option 2:
> New Job

How many criteria will you use?:
> 3

Enter criteria 1:
> Salary
Weight (1–10):
> 8

Enter criteria 2:
> Stress
Weight (1–10):
> 5

Enter criteria 3:
> Career Growth
Weight (1–10):
> 9

------ Points for Current Job --------
Salary score (0-10):
> 6
Stress score (0-10):
> 7
Career Growth score (0-10):
> 5

------ Points for New Job --------
Salary score (0-10):
> 9
Stress score (0-10):
> 4
Career Growth score (0-10):
> 8
Output:

yaml
Copy code
Decision: Should I take the new job

Result:
Best Option: New Job
Total Score: 164

Breakdown for Current Job:
Salary: 6 × 8 = 48
Stress: 7 × 5 = 35
Career Growth: 5 × 9 = 45
Total = 128

Breakdown for New Job:
Salary: 9 × 8 = 72
Stress: 4 × 5 = 20
Career Growth: 8 × 9 = 72
Total = 164
Notes
Scores and weights must be numbers in the given range.

Totals are automatically calculated.

The program works entirely in the terminal.