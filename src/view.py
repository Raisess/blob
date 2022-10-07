class View:
  def __init__(self, title: str, path: str):
    base_html = self._find_html("base.html")
    self._content = base_html.replace("{{TITLE}}", title)
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
    super().__init__(f"Blob Error {code}", "error.html")

    self._content = self._content.replace("{{CODE}}", str(code))
    self._content = self._content.replace("{{MESSAGE}}", message)
