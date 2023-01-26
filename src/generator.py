import os

from view import ListView, PostView

class Generator:
  def Generate() -> None:
    if not os.path.isdir("./blog"):
      os.mkdir("./blog")

    with open("./blog/index.html", "w") as list_file:
      view = ListView(replace_md_with_html=True)
      list_file.write(view.content())

    posts = os.listdir("./inputs")
    for post in posts:
      path = f"./blog/{post}"
      with open(path.replace(".md", ".html"), "w") as post_file:
        view = PostView(path)
        post_file.write(view.content())
