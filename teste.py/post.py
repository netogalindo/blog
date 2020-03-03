class Post:
    def __init__(self, title: str, content: str):
        self.title = title
        self.content = content

    def json(self):
        return {
            "title": self.title,
            "content": self.content, # It's good practice to add a comma to the end of the dictionary, because, if you
            # add something to this dictionary, you'll not be altering the last line that already existed
        }
