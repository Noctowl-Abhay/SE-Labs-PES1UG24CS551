# Lab 5: Reflection — Static Code Analysis

## 1. How did static analysis tools (Pylint, Bandit, Flake8) help identify hidden bugs and security vulnerabilities?
Static analysis tools inspected code without execution to instantly flag architectural and security flaws that manual testing might miss.

## 2. What was the most critical security or quality issue found, and how did you remediate it?
The most critical security issue was the use of Python's `eval()` function on user input, which we replaced with a secure conditional parser.

## 3. How does maintaining a high Pylint score (>9.5) and adhering to PEP 8 improve code maintainability and team collaboration?
It ensures code readability, standardizes formatting, and reduces technical debt across team members.

## 4. What are the limitations of static analysis tools compared to dynamic analysis or manual code review?
Static analysis tools can generate false positives and may not catch complex runtime logic bugs that only appear during live execution.
