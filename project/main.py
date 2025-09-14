from test.test_all import TestAll
import unittest

if __name__ == "__main__":
    test_suite = unittest.TestSuite()
    test_suite.addTest(TestAll('testcase'))
    runner = unittest.TextTestRunner()
    runner.run(test_suite)

