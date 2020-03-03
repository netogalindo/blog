from unittest import TestCase
from post import Post


class PostTest(TestCase):
    def test_create_post(self):
        p = Post("Test Title", "Test content.")

        self.assertEqual("Test Title", p.title, "The title is not valid for the test") # self is TestCase
        # This is checking if the defined title is equal to p.title
        # self.assertEqual("Testx", p.title) This would make the test fail

        self.assertEqual("Test content.", p.content, "The content is not valid for the test")
        # The same, but with the content

        # This seems like an idiotic test, but, if you would change the __init__ method, this test would fail, and this
        # would remind you that you have to check other parts of your software as well, to make sure nothing is broken

        # Something else that would result in an "Test failed" would be if a programmer would have added an initial
        # value to one of the parameters

        self.assertIsInstance(p.title, str, "Test Title should be a string")
        self.assertIsInstance(p.content, str, "Test Content should be a string")

    def test_json(self):
        p = Post("Test Title", "Test content.")
        expected = {"title": "Test Title", "content": "Test content."}

        self.assertDictEqual(expected, p.json(), "The json was not created")
