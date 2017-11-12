import unittest
from SI507project5_code import *

class test_cacheFiles(unittest.TestCase):
    def setUp(self):
        self.data = open("cache_contents.json",'r')
        self.creds = open("creds.json",'r')

    def test_cacheExistence(self):
        self.assertTrue(self.data.read(), "No cached data.")
        self.assertTrue(self.creds.read(), "No creds data.")

    def tearDown(self):
        self.data.close()
        self.creds.close()

class test_csvFiles(unittest.TestCase):
    def setUp(self):
        self.colorful = open("colorfulgradients.csv",'r')
        self.paintings = open("ifpaintingscouldtext.csv",'r')

    def test_csvExistence(self):
        self.assertTrue(self.colorful.read(), "No data in colorfulgradients.csv!")
        self.assertTrue(self.paintings.read(), "No data in ifpaintingscouldtext.csv!")

    def tearDown(self):
        self.colorful.close()
        self.paintings.close()

class test_classBlog(unittest.TestCase):
    sample = getBlog("thefandometrics")
    claBlog = Blog(sample['response'])
    claPost = Post(claBlog.postList[0])
    blogPostlist = claBlog.orderPosts()

    def test_classBlog_type(self):
        self.assertIsInstance(self.claBlog, Blog, "classBlog is not class Blog!")

    def test_classBlog_constructor(self):
        self.assertIsInstance(self.claBlog.title, str, "Title is not a string!")
        self.assertIsInstance(self.claBlog.totalPosts, int, "Total Posts is not an integer!")
        self.assertIsInstance(self.claBlog.postList, list, "postList is not a list!")

class test_classPost(unittest.TestCase):
    sample = getBlog("thefandometrics")
    claBlog = Blog(sample['response'])
    claPost = Post(claBlog.postList[0])
    blogPostlist = claBlog.orderPosts()

    def test_classPost_constructor(self):
         self.assertIsInstance(self.claPost.type, str, "Title is not a string!")
         self.assertIsInstance(self.claPost.date, str, "Title is not a string!")
         self.assertIsInstance(self.claPost.notes, int, "Title is not an integer!")
         self.assertIsInstance(self.claPost.url, str, "Title is not a string!")
         self.assertIsInstance(self.claPost.summary, str, "Title is not a string!")

if __name__ == "__main__":
    unittest.main(verbosity=2)
