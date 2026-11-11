# LAB-6: Code and Branch Coverage Analysis - Car Rental Rate

**SRN:** PES1UG24CS551 <br>
**Name:** Abhay Dubey H

Coverage analysis of a car rental module (`car_rental_rate.py`) using **coverage** and **pytest**. Starting from a single example test, more test cases were written to reach **100% line coverage** and **100% branch coverage**.

- **Repo link:** [Lab-6](https://github.com/Noctowl-Abhay/L6_L7_02_car_rental_rate/Lab 6)
- **Code:** [car_rental_rate.py](car_rental_rate.py)
- **Test cases:** [test_car_rental.py](test_car_rental.py)
- **Screenshots (code coverage):** [Before](screenshots/code-coverage-before.png) | [After](screenshots/code-coverage-after.png)
- **Screenshots (branch coverage):** [Before](screenshots/branch-coverage-before.png) | [After](screenshots/branch-coverage-after.png)
- **Summary:** [LAB6_SUMMARY.txt](LAB6_SUMMARY.txt)

---

## How to Run

Requires Python 3.x.

```bash
python3 -m venv venv
source venv/bin/activate
pip install coverage pytest
```

**Code (line) coverage**

```bash
coverage run -m pytest test_car_rental.py
coverage report -m
```

**Branch coverage**

```bash
coverage run --branch --source=car_rental_rate -m pytest test_car_rental.py
coverage report -m
```

---

## Folder Structure

```
LAB-6/
├── car_rental_rate.py
├── test_car_rental.py
├── screenshots/
│   ├── code-coverage-before.png
│   ├── code-coverage-after.png
│   ├── branch-coverage-before.png
│   └── branch-coverage-after.png
├── LAB6_SUMMARY.txt
└── README.md
```

---

## Results

| Measure | Before (1 test) | After (19 tests) |
|---------|-----------------|------------------|
| Line coverage (`car_rental_rate.py`) | 47% (27 of 51 statements missed) | **100%** |
| Branch coverage (`car_rental_rate.py`) | 44% (10 partial branches, 36 total) | **100%** |

---

## What Was Done

The module has two functions: `process_rental_fleet` (pricing, risk flags, audit status) and `check_fleet_telematics` (consecutive speeding detection). The starter file had one test. Tests were added in two stages (details in [LAB6_SUMMARY.txt](LAB6_SUMMARY.txt)):

1. **Code coverage:** tests so that every statement runs at least once (invalid arguments, unconfirmed rentals, each vehicle type, young driver surcharges, long trips, empty batch, all telematics outcomes).
2. **Branch coverage:** tests so that every `if`/`elif`/loop decision takes both its True and False outcome (negative miles, trips over 300 miles for young and adult drivers, `HIGH_RISK_AUDIT`, speeding streak reset, multiple vehicles).

Before and after terminal output for both measures is in [screenshots](screenshots).
