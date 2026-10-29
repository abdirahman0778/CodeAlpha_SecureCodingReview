import unittest
from sample_app.db import create_demo_db, unsafe_lookup, safe_lookup

class SQLSecurityTests(unittest.TestCase):
    def setUp(self):
        self.conn=create_demo_db()
    def tearDown(self):
        self.conn.close()
    def test_normal_lookup(self):
        self.assertEqual(safe_lookup(self.conn,'alice'),[('alice','admin')])
    def test_sql_injection_vulnerability_in_demo(self):
        malicious="' OR 1=1 -- "
        self.assertEqual(len(unsafe_lookup(self.conn,malicious)),2)
    def test_parameterized_query_blocks_injection(self):
        malicious="' OR 1=1 -- "
        self.assertEqual(safe_lookup(self.conn,malicious),[])
    def test_unknown_username(self):
        self.assertEqual(safe_lookup(self.conn,'nobody'),[])

if __name__=='__main__': unittest.main()
