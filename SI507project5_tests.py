import unittest
from SI507project5_code import *

class test_cacheFiles(unittest.TestCase):
    def setUp(self):
        self.data = open("cache_contents.json",'r')
        self.creds = open("creds.json",'r')

    def test_existence(self):
        self.assertTrue(self.data.read())
        self.assertTrue(self.creds.read())

    def tearDown(self):
        self.data.close()
        self.creds.close()

class test_csvFiles(unittest.TestCase):
    def setUp(self):
        self.colorful = open("colorful.csv",'r')
        self.paintings = open("paintings.csv",'r')

    def test_existence(self):
        self.assertTrue(self.colorful.read())
        self.assertTrue(self.paintings.read())

    def tearDown(self):
        self.colorful.close()
        self.paintings.close()

if __name__ == "__main__":
    unittest.main(verbosity=2)
