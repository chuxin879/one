
import unittest


import requests


class TestBaidu(unittest.TestCase):


   

    def test_baidu(self):
        code = requests.get("http://www.baidu.com").status_code
        self.assertEqual(200, code)


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()