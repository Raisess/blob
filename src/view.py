import os
from env import Env

class View:
  def __init__(self):
    env = Env()
    self._content = self._find_html("base.html")
    self._content = self._content.replace("{{TITLE}}", env.get("STATIC_TITLE"))

  @property
  def content(self) -> str:
    return self._content

  @property
  def content_bytes(self) -> bytes:
    return bytes(self.content, "utf8")

  def _find_html(self, path: str) -> str:
    if not path.endswith(".html"):
      raise Exception("Invalid file format")

    path = path.replace("blog", "inputs")
    file = open(path, "r")
    html = file.read()
    file.close()
    return html


class ListView(View):
  def __init__(self):
    super().__init__()

    posts = os.listdir("./inputs")
    posts.sort()
    posts.reverse()
    posts_tags = ["<h2>Posts</h2>"]
    for post in posts:
      date = post.split("_")[0]
      year = date[0:4]
      month = date[4:6]
      day = date[6:8]

      page = post.split("_")[1].replace("-", " ").replace(".html", "")
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

    self._content = self._content.replace("{{CONTENT}}", "<br />".join(posts_tags))


class PostView(View):
  def __init__(self, path: str):
    super().__init__()

    html = self._find_html(path)
    self._content = self._content.replace("{{CONTENT}}", html)


class ErrorView(View):
  def __init__(self, code: int, message: str):
    super().__init__()

    self._content = self._content.replace("{{CONTENT}}", f"<h2>Error {code}: {message}</h2>")
