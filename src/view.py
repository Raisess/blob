STATIC_PAGE_TILE = "Blob"

class View:
  def __init__(self, path: str, title: str = STATIC_PAGE_TILE):
    if path == "base.html":
      self._content = self._find_html("base.html")
      self._content = self._content.replace("{{TITLE}}", title)
    else:
      self._content = self._find_html("base.html")
      self._content = self._content.replace("{{TITLE}}", title)
      html = self._find_html(path)
      self._content = self._content.replace("{{CONTENT}}", html)

  @property
  def content(self) -> str:
    return self._content

  @property
  def content_bytes(self) -> bytes:
    return bytes(self.content, "utf8")

  def _find_html(self, path: str) -> str:
    if not path.endswith(".html"):
      raise Exception("Invalid file format")

    file = open("public/" + path, "r")
    html = file.read()
    file.close()
    return html

class ErrorView(View):
  def __init__(self, code: int, message: str):
    super().__init__("base.html", f"Blob Error {code}")

    self._content = self._content.replace("{{CONTENT_TITLE}}", f"REQUEST ERROR {code}")
    self._content = self._content.replace("{{CONTENT}}", f"<h2>{message}</h2>")
