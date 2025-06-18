import os
import shutil

from view import ListView, PostView

class Generator:
  def Generate() -> None:
    if not os.path.isdir("./blog"):
      os.mkdir("./blog")

    with open("./blog/index.html", "w") as list_file:
      view = ListView(replace_md_with_html=True)
      list_file.write(view.content())

    files = os.listdir("./inputs")
    for file in files:
      path = f"./blog/{file}"
      if path.endswith(".html") or path.endswith(".md"):
        with open(path.replace(".md", ".html"), "w") as f:
          view = PostView(path)
          f.write(view.content())
      else:
        shutil.copy(f"./inputs/{file}", f"./blog/{file}")
