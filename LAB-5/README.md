# LAB-5: Static Code Analysis - Retail POS System

**SRN:** PES1UG24CS551 <br>
**Name:** Abhay Dubey H

Static analysis of a Retail POS script (`pos_system.py`) using **Pylint**, **Flake8** and **Bandit**. Issues were identified, documented, and fixed, with a separate commit for each tool.

- **Repo link:** https://github.com/Noctowl-Abhay/LAB-5_02_retail_pos
- **Code:** [02_retail_pos](02_retail_pos)
- **Issues table and fixes:** [ISSUES.md](ISSUES.md)
- **Reports before changes:** [Pylint](REPORTS-BEFORE/pylint_report.txt) | [Flake8](REPORTS-BEFORE/flake8_report.txt) | [Bandit](REPORTS-BEFORE/bandit_report.txt)
- **Reports after changes:** [Pylint](REPORTS-AFTER/pylint_report.txt) | [Flake8](REPORTS-AFTER/flake8_report.txt) | [Bandit](REPORTS-AFTER/bandit_report.txt)
- **Summary:** [LAB5_SUMMARY.txt](LAB5_SUMMARY.txt)

---

## How to Run

Requires Python 3.10+.

```bash
python3 -m venv venv
source venv/bin/activate
pip install pylint flake8 bandit

cd 02_retail_pos
python pos_system.py
```

**Run the analysis tools**

```bash
pylint pos_system.py > pylint_report.txt
bandit -r pos_system.py > bandit_report.txt
flake8 pos_system.py > flake8_report.txt
```

---

## Folder Structure

```
LAB-5/
├── 02_retail_pos/
│   └── pos_system.py
├── REPORTS-BEFORE/
│   ├── pylint_report.txt
│   ├── flake8_report.txt
│   └── bandit_report.txt
├── REPORTS-AFTER/
│   ├── pylint_report.txt
│   ├── flake8_report.txt
│   └── bandit_report.txt
├── ISSUES.md
├── LAB5_SUMMARY.txt
└── README.md
```

---

## What Was Done

Three commits, one per tool (details in [ISSUES.md](ISSUES.md)):

1. **Bandit:** security fixes
2. **Pylint:** code quality and correctness fixes
3. **Flake8:** style and formatting fixes

Before and after output for each tool is in [REPORTS-BEFORE](REPORTS-BEFORE) and [REPORTS-AFTER](REPORTS-AFTER).
