from blog import Blog
from post import Post

# This is a constant
MENU_PMT = "Enter 'c' to create a blog, 'l' to list blogs, 'r' to read a blog, 'p' to create a post, or 'q' to quit: "
blogs = dict()



def print_blogs():
    # Print available blogs
    for key, blog in blogs.items():
        print(f"- {blog}")


def ask_create_blog():
    input_title = input("Enter the title of your blog: ")
    input_author = input("Enter your name: ")
    blogs[input_title] = Blog(input_title, input_author)


def teste():
    input_title = input("Enter the title of your blog: ")
    input_author = input("Enter your name: ")
    blogs[input_title] = Blog(input_title, input_author)


def ask_read_blog():
    input_title = input("Enter the title of your blog: ")
    print_posts(blogs[input_title])


def print_posts(blog):
    for post in blog.posts:
        print_post(post)


def print_post(post):
    print(f"Title: {post.title}, Content: {post.content}")


def ask_create_post():
    input_blog_name = input("Enter the blog you want to create a post in: ")
    input_title = input("Enter the title of your post: ")
    input_content = input("Enter the content of your post: ")
    blogs[input_blog_name].create_post(input_title, input_content)


def menu():
    # Show the user available blogs
    # Let the user make a choice
    # Do something with that choice
    # Eventually, exit
    print_blogs()
    selection = input(MENU_PMT)
    while selection != "q":
        if selection == "c":
            ask_create_blog()
        elif selection == "l":
            print_blogs()
        elif selection == "r":
            ask_read_blog()
        elif selection == "p":
            ask_create_post()
        selection = input(MENU_PMT)
