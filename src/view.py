import mistune
import os
import jinja2

from env import env

class View:
  def __init__(self, page: str):
    self._content = None
    theme = env.get("THEME") if env.get("THEME") != None else "default"
    with open(f"/usr/local/etc/blob/themes/{theme}/{page}.html", "r") as theme_file:
      self.__theme_content = jinja2.Template(theme_file.read())

  def content(self) -> str:
    return self.__theme_content.render({
      "TITLE": env.get("TITLE"),
      "DESCRITPION": env.get("DESCRIPTION"),
      "CONTENT": self._content,
    })

  def content_bytes(self) -> bytes:
    return bytes(self.content(), "utf-8")


class ListView(View):
  def __init__(self, dev = True):
    super().__init__("list")
    self._content = []

    post_list = os.listdir("./inputs")
    post_list.sort()
    post_list.reverse()
    for post in post_list:
      if not dev:
        post = post.replace(".md", ".html")

      post_data = {}
      post_data["link"] = post
      post_data["name"] = post.split("_")[1].replace("-", " ").replace(".html", "").replace(".md", "")

      date = post.split("_")[0]
      post_data["date"] = {
        "year": date[0:4],
        "month": date[4:6],
        "day": date[6:8],
      }
      self._content.append(post_data)


class PostView(View):
  def __init__(self, path: str):
    super().__init__("post")
    file = open(path.replace("blog", "inputs"), "r")
    data = file.read()
    file.close()
    self._content = data if path.endswith(".html") else mistune.html(data)


class ErrorView(View):
  def __init__(self, code: int, message: str):
    super().__init__("post")
    self._content = f"<h2>Error {code}: {message}</h2>"
