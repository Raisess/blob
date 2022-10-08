import os

STATIC_TITLE = "Blob"

class View:
  def __init__(self, title: str = STATIC_TITLE):
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

    path = path.replace("posts", "inputs")
    file = open(path, "r")
    html = file.read()
    file.close()
    return html


class ListView(View):
  def __init__(self, title: str):
    super().__init__(title)

    posts = os.listdir("./inputs")
    posts_tags = ["<h2>Posts</h2>"]
    for post in posts:
      page = post.split(".html")[0].replace("-", " ")
      posts_tags.append(f"<h4><a href=\"./posts/{post}\">{page}</a></h4>")

    self._content = self._content.replace("{{CONTENT}}", "<br />".join(posts_tags))


class PostView(View):
  def __init__(self, title: str, path: str):
    super().__init__(title)

    html = self._find_html(path)
    self._content = self._content.replace("{{CONTENT}}", html)


class ErrorView(View):
  def __init__(self, code: int, message: str):
    super().__init__(f"REQUEST ERROR {code}")

    self._content = self._content.replace("{{CONTENT}}", f"<h2>{message}</h2>")
