class View:
  def __init__(self, title: str, path: str):
    base_html = self._find_html("base.html")
    self._content = base_html.replace("{{TITLE}}", title)
    html = self._find_html(path)
    self._content = self._content.replace("{{POST}}", html)

  @property
  def content(self):
    return self._content

  def _find_html(self, path: str) -> str:
    if not path.endswith(".html"):
      raise Exception("Invalid file format")

    file = open("public/" + path, "r")
    html = file.read()
    file.close()
    return html
