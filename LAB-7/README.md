# LAB-7: Fuzz Testing with Hypothesis - Car Rental Rate

**SRN:** PES1UG24CS551 <br>
**Name:** Abhay Dubey H

Property-based fuzz testing of a car rental input-processing module (`processor.py`) using **Hypothesis** and **pytest**. The starter code crashed on `None` input in all three functions; the functions were then hardened until all fuzz tests passed.

- **Repo link:** [Lab 7 Repository](https://github.com/Noctowl-Abhay/L6_L7_02_car_rental_rate/tree/main/Lab%207)
- **Code (fixed):** [processor.py](processor.py)
- **Test cases:** [test_processor.py](test_processor.py)
- **Screenshots:** [Before](screenshots/before) | [After](screenshots/after)
- **Report (PDF):** [SE_PES1UG24CS551_LAB-7.pdf](SE_PES1UG24CS551_LAB-7.pdf)
- **Summary:** [LAB7_SUMMARY.txt](LAB7_SUMMARY.txt)

---

## How to Run

Requires Python 3.8+.

```bash
python3 -m venv venv
source venv/bin/activate
pip install hypothesis pytest
```

**Run the application**

```bash
python processor.py
```

**Run the fuzz tests**

```bash
python3 -m pytest test_processor.py
```

---

## Folder Structure

```
LAB-7/
├── processor.py
├── test_processor.py
├── screenshots/
│   ├── before/
│   └── after/
├── SE_PES1UG24CS551_LAB-7.pdf
├── LAB7_SUMMARY.txt
└── README.md
```

---

## Results

| Measure | Before (buggy `processor.py`) | After (fixed `processor.py`) |
|---------|-------------------------------|------------------------------|
| Tests passed | 0 of 3 | **3 of 3** |
| Tests failed | 3 of 3 | 0 |
| Failing input | `s = None` | none |

---

## What Was Done

The module has three functions: `sanitize_license_plate` (removes `-`, space, `_`, `#` and uppercases), `parse_trip_mileage` (CSV string to list of floats) and `format_rental_invoice` (`Driver:Days:Category` to invoice text). Work was done in four steps (details in [LAB7_SUMMARY.txt](LAB7_SUMMARY.txt)):

1. **Ran the buggy script** with normal input to confirm it works on the happy path.
2. **Completed `test_processor.py`** with one Hypothesis test per function, using `st.text() | st.none()` as the input strategy and `try`/`except` to check the "should not crash" property.
3. **Ran the tests on the buggy code:** all 3 failed with `AttributeError: 'NoneType' object has no attribute ...` (`strip` / `split`), and Hypothesis shrank the failing input to `None`.
4. **Fixed `processor.py`:** added `None` / non-string checks to every function, skipped bad pieces in `parse_trip_mileage`, and handled short records and non-integer days in `format_rental_invoice`. Re-running the tests gave 3 passed.

Before and after terminal output is in [screenshots](screenshots) and in the PDF report.
