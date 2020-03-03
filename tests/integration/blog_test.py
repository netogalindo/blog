from unittest import TestCase

from blog import Blog


class BlogTest(TestCase):
    def test_create_post(self):
        b = Blog("Test Title", "Neto")
        b.create_post("Testing New Post", "I am testing if a new post is created")
        self.assertEqual(1, len(b.posts), "The length of the list is 0, so no posts have been created")
        self.assertEqual("Testing New Post", b.posts[0].title, "The title of the post has not been created")
        self.assertEqual("I am testing if a new post is created", b.posts[0].content, "The content of the post has not"
                                                                                      "been created")

    def test_json_no_posts(self):
        b = Blog("Testing Json", "Neto")
        self.assertDictEqual({"title": "Testing Json", "author": "Neto", "posts": []}, b.json(), "The json was not"
                                                                                                 "created")

    def test_json(self):
        b = Blog("Testing Json", "Neto")
        b.create_post("Testing Post", "Testing Post Content")
        self.assertDictEqual({"title": "Testing Json", "author": "Neto", "posts": [{"title": "Testing Post",
                                                                                    "content":
                                                                                        "Testing Post Content"}]},
                                                                                    b.json(),
                                                                                    "The json was not created")
