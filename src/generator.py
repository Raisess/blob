import os
from view import ListView, PostView

class Generator:
  def __init__(self, post: str):
    self._post = post

  def generate(self):
    if self._post == "index":
      view = ListView()
      file = open("index.html", "w")
      file.write(view.content)
      file.close()
    else:
      if not os.path.isdir("./posts"):
        os.mkdir("./posts")

      path = f"./posts/{self._post}.html"
      view = PostView(path)
      file = open(path, "w")
      file.write(view.content)
      file.close()
