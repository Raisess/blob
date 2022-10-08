import os
from env import Env
from view import ListView, PostView

class Generator:
  def __init__(self, post: str):
    self._post = post

  def generate(self):
    env = Env()
    if not os.path.isdir("./blog"):
      os.mkdir("./blog")

    if self._post == "index":
      view = ListView(env.get("STATIC_TITLE"))
      file = open("./blog/index.html", "w")
      file.write(view.content)
      file.close()
    else:
      path = f"./blog/{self._post}.html"
      view = PostView(env.get("STATIC_TITLE"), path)
      file = open(path, "w")
      file.write(view.content)
      file.close()
