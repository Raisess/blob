import mistune
import os
import jinja2

from env import env

class View:
  def __init__(self, is_list: bool = False):
    theme = env.get("THEME") if env.get("THEME") != None else "default"
    page = "list.html" if is_list else "post.html"
    with open(f"/usr/local/etc/blob/themes/{theme}/{page}", "r") as theme_file:
      self.__theme_content = jinja2.Template(theme_file.read())

  def _load_html(self, path: str) -> str:
    file = open(path.replace("blog", "inputs"), "r")
    data = file.read()
    file.close()
    return data if path.endswith(".html") else mistune.html(data)

  def _render(self, data: dict[any]) -> str:
    return self.__theme_content.render({
      "TITLE": env.get("TITLE"),
      "DESCRITPION": env.get("DESCRIPTION"),
      **data,
    })

  def content(self) -> str:
    raise NotImplemented()

  def content_bytes(self) -> bytes:
    print(self.content())
    return bytes(self.content(), "utf-8")


class ListView(View):
  def __init__(self, dev = True):
    super().__init__(True)
    print("HERE")
    self.__content = []

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
      self.__content.append(post_data)

  def content(self) -> str:
    return self._render({
      "posts": self.__content,
    })


class PostView(View):
  def __init__(self, path: str):
    super().__init__()
    self.__content = self._load_html(path)

  def content(self) -> str:
    return self._render({
      "CONTENT": self.__content,
    })


class ErrorView(View):
  def __init__(self, code: int, message: str):
    super().__init__()
    self.__content = f"<h2>Error {code}: {message}</h2>"

  def content(self) -> str:
    return self._render({
      "CONTENT": self.__content,
    })
