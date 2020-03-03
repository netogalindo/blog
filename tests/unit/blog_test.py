from unittest import TestCase
from blog import Blog


class BlogTest(TestCase):
    def test_create_blog(self):
        b = Blog("Test Title", "Test Author")
        self.assertEqual("Test Title", b.title, "The title is not valid for the test")
        self.assertEqual("Test Author", b.author, "The author is not valid for the test")
        self.assertListEqual([], b.posts, "The list is not valid for the test")

        self.assertIsInstance(b.title, str, "Title should be a string")
        self.assertIsInstance(b.author, str, "Author should be a string")
        self.assertIsInstance(b.posts, list, "Posts should be a list")

    def test_repr(self):
        b = Blog("Test Title", "Test Author")
        b2 = Blog("How my life has been", "Neto")
        self.assertEqual("Test Title, by Test Author (0 posts)", b.__repr__(), "The result of the method is not"
                                                                               "correct")
        # This is the base of what TDD is: It's to create a test that will fail, but that sort of conveys what you want
        # to do (In case you create this test before implementing the method).
        self.assertEqual("How my life has been, by Neto (0 posts)", b2.__repr__(), "The result of the method is not"
                                                                                   "correct")
        b3 = Blog("Testing 3 posts", "Neto")
        b3.posts = ["Testing", "Multiple", "Posts"]
        self.assertEqual("Testing 3 posts, by Neto (3 posts)", b3.__repr__(), "The result of the method is not correct")
