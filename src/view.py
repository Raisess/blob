import os

STATIC_PAGE_TILE = "Blob"

class View:
  def __init__(self, title: str = STATIC_PAGE_TILE):
    self._content = self._find_html("base.html")
    self._content = self._content.replace("{{TITLE}}", title)

  @property
  def content(self) -> str:
    return self._content

  @property
  def content_bytes(self) -> bytes:
    return bytes(self.content, "utf8")

  def _find_html(self, path: str) -> str:
    if not path.endswith(".html"):
      raise Exception("Invalid file format")

    file = open(path, "r")
    html = file.read()
    file.close()
    return html


class ListView(View):
  def __init__(self):
    super().__init__()

    posts = os.listdir("./posts")
    posts_tags = []
    for post in posts:
      page = post.split(".html")[0]
      posts_tags.append(f"<a href=\"./posts/{post}\">{page}</a>")

    self._content = self._content.replace("{{CONTENT}}", "<br />".join(posts_tags))


class PostView(View):
  def __init__(self, path: str):
    super().__init__()

    html = self._find_html(path)
    self._content = self._content.replace("{{CONTENT}}", html)


class ErrorView(View):
  def __init__(self, code: int, message: str):
    super().__init__(f"REQUEST ERROR {code}")

    self._content = self._content.replace("{{CONTENT}}", f"<h2>{message}</h2>")
