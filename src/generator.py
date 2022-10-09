import os
from env import Env
from view import ListView, PostView

class Generator:
  def generate():
    if not os.path.isdir("./blog"):
      os.mkdir("./blog")

    view = ListView()
    file = open("./blog/index.html", "w")
    file.write(view.content)
    file.close()

    posts = os.listdir("./inputs")
    for post in posts:
      path = f"./blog/{post}"
      view = PostView(path)
      file = open(path, "w")
      file.write(view.content)
      file.close()
