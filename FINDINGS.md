# Security Code Review Report
## CodeAlpha Cybersecurity Internship — Task 3

**Project:** Secure Coding Review  
**Assessment Date:** October 29, 2026  
**Programming Language:** Python 3.14.2  
**Database:** SQLite (In-Memory)  
**Operating System:** Microsoft Windows NT 10.0.26300.0  
**Security Testing Tool:** Bandit 1.9.4  
**Testing Framework:** Python unittest  
**Assessment Type:** Manual Code Review, Static Analysis and Automated Security Testing

---

## 1. Executive Summary

This security assessment reviews a local educational Python application to identify and demonstrate SQL Injection vulnerabilities and evaluate secure coding practices.

The assessment focused on database query construction and the handling of user-controlled input in `sample_app/db.py`.

One SQL Injection vulnerability (CWE-89) was identified in the deliberately vulnerable `unsafe_lookup()` function.

A secure alternative, `safe_lookup()`, was reviewed and tested using parameterized SQL queries.

**Key Results:**

- One SQL Injection vulnerability identified.
- One Bandit B608 security finding.
- Four automated unit tests passed.
- Zero unit test failures.
- Parameterized SQL query protection verified against the tested injection input.
- No production systems or external databases were assessed.

The results demonstrate the importance of separating untrusted input from executable SQL statements.

---

## 2. Scope of Assessment

### 2.1 In-Scope Components

- `sample_app/db.py`
- SQL query construction
- User-controlled username input
- SQL Injection identification
- Parameterized SQL query implementation
- Automated regression testing
- Static code analysis using Bandit

### 2.2 Out-of-Scope Components

The following security areas were not evaluated:

- Authentication and authorization systems
- Password management
- Cryptographic security
- External database infrastructure
- Production applications
- Network security
- Third-party dependency vulnerabilities
- API security

The assessment used fabricated records stored in a local in-memory SQLite database.

---

## 3. Security Finding — SEC-001

| Property | Description |
|---|---|
| Finding ID | SEC-001 |
| Vulnerability | SQL Injection |
| CWE | CWE-89 |
| Potential Severity | High, depending on application context |
| Bandit Severity | Medium |
| Bandit Confidence | Low |
| Affected File | `sample_app/db.py` |
| Affected Function | `unsafe_lookup()` |
| Affected Line | 12 |
| Status | Confirmed in educational demonstration |

### 3.1 Vulnerability Description

The `unsafe_lookup()` function directly inserts user-controlled input into a SQL statement using Python string interpolation.

This introduces an SQL Injection vulnerability because malicious input may modify the intended SQL query structure.

### 3.2 Vulnerable Code

```python
def unsafe_lookup(conn, username):
    # VULNERABLE: untrusted input embedded directly in SQL.
    sql = f"SELECT username, role FROM users WHERE username = '{username}'"
    return conn.execute(sql).fetchall()
```

### 3.3 Root Cause

The SQL statement is constructed by combining executable SQL syntax with untrusted user input.

The application does not separate the input value from the SQL query structure.

This allows specially crafted input to influence SQL execution.

### 3.4 Proof of Concept

The following payload was tested against the local educational database:

```text
' OR 1=1 --
```

When passed to `unsafe_lookup()`, this input modifies the SQL condition and causes the query to return both fabricated user records.

The test confirms that the vulnerable function does not enforce an exact username match.

### 3.5 Potential Security Impact

In real applications, SQL Injection may cause:

1. Unauthorized disclosure of database records.
2. Exposure of confidential information.
3. Authentication or authorization bypass, depending on application design.
4. Unauthorized database modifications, depending on database permissions.

These are potential impacts. The educational demonstration only confirmed unintended retrieval of fabricated database records.

---

## 4. Secure Coding Remediation

### 4.1 Secure Implementation

The `safe_lookup()` function uses