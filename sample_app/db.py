"""Deliberately vulnerable demo and remediated example on an in-memory local database."""
import sqlite3

def create_demo_db():
    connection=sqlite3.connect(':memory:')
    connection.execute('CREATE TABLE users (username TEXT NOT NULL, role TEXT NOT NULL)')
    connection.executemany('INSERT INTO users VALUES (?, ?)', [('alice','admin'),('bob','user')])
    return connection

def unsafe_lookup(conn, username):
    # VULNERABLE: untrusted input embedded directly in SQL. Educational example only.
    sql = f"SELECT username, role FROM users WHERE username = '{username}'"
    return conn.execute(sql).fetchall()

def safe_lookup(conn, username):
    # FIX: placeholders separate user data from executable SQL syntax.
    return conn.execute('SELECT username, role FROM users WHERE username = ?', (username,)).fetchall()
