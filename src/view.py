import mistune
import os
import jinja2

from env import env

class View:
  def __init__(self):
    theme = env.get("THEME") if env.get("THEME") != None else "default.html"
    with open(f"/usr/local/etc/blob/themes/{theme}", "r") as theme_file:
      self.__theme_content = jinja2.Template(theme_file.read())
      theme_file.close()

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
    return bytes(self.content(), "utf-8")


class ListView(View):
  def __init__(self, dev = True):
    super().__init__()

    posts = os.listdir("./inputs")
    posts.sort()
    posts.reverse()
    posts_tags = ["<h2>Posts</h2>"]
    for post in posts:
      if not dev:
        post = post.replace(".md", ".html")

      date = post.split("_")[0]
      year = date[0:4]
      month = date[4:6]
      day = date[6:8]

      page = post.split("_")[1].replace("-", " ").replace(".html", "").replace(".md", "")
      posts_tags.append(f"""
        <div>
          <time style="color: #888888 !important; font-size: 0.9rem !important;">
            {year}-{month}-{day}
          </time>
          <h4>
            <a href=\"/blog/{post}\">{page}</a>
          </h4>
        </div>
      """)

    self.__content = "<br />".join(posts_tags)

  def content(self) -> str:
    return self._render({
      "CONTENT": self.__content,
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
