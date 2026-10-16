# Issues found in pos_system.py

| Issue | Type | Line(s) | Description | Fix Approach |
|-------|------|---------|-------------|--------------|
| `eval()` on user input | Security — HIGH (Bandit B307) | 33–37 | Anything typed at the promo prompt is executed as Python code. | Replace eval with a safe conditional parser. |
| Mutable default argument `receipts=[]` | Bug — MEDIUM (Pylint W0102) | 10 | Default list is shared across all calls. | Default to None, create the list inside the function. |
| Bare `except:` | Quality/Bug — MEDIUM (Pylint W0702) | 16, 39 | Swallows every error and hides logic bugs. | Use explicit key checks and `.get()` lookups. |
| File resource leak | Resource bug — MEDIUM (Pylint W1514) | 43 | `open()` without `close()` or context manager. | Use `with open(..., "a", encoding="utf-8")`. |
| Unused imports | Code smell — LOW (Flake8 F401) | 1–2 | `json` and `logging` imported but never used. | Remove unused imports. |
| Non-PEP 8 naming (`printSales`) | Style — CONVENTION (Pylint C0103) | 7 | Function name uses camelCase instead of snake_case. | Rename function to `print_sales`. |
| Missing docstrings | Style — CONVENTION (Pylint C0114, C0116) | Module / All | Module and functions lack descriptive docstrings. | Add clear docstrings to module and all functions. |
| Missing execution guard | Style — CONVENTION | Bottom | `main()` is executed directly on import rather than safely guarded. | Wrap execution in `if __name__ == "__main__":`. |
