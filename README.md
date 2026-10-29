# Task 3 — Secure Coding Review (Python + SQLite)

## Scope
Review a deliberately vulnerable **local demonstration application**, identify SQL injection, supply remediation and regression tests. Do not use this technique on third-party systems.

## Run tests (no external dependencies)
```bash
python3 -m unittest discover -s tests -v
```
Expected: four unit tests pass; the unsafe sample demonstrates the flaw and the secure function prevents it. Replace the expected statement with actual console output once tested.

## Static analyzer (optional)
```bash
python3 -m pip install bandit
bandit -r sample_app -f txt
```
The intentionally unsafe function may be reported. A scanner finding is not proof by itself; validate manually. Scan the remediated function and keep a record of the scope and tool version.

## Audit deliverables
See [FINDINGS.md](FINDINGS.md) for vulnerability, root cause, risk, remediation, and validation. Screenshot your test execution and record tool results.
