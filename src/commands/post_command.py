import os
from datetime import datetime

from yacli import Command

class PostCommand(Command):
  def __init__(self):
    super().__init__("post", "Create new html post.", args_len=2)
    self.__valid_post_types = ["html", "markdown"]

  def handle(self, args: list[str]) -> None:
    post_type = args[0]
    post_name = args[1]
    self.__valid_post_types.index(post_type)

    if not os.path.isdir(f"./inputs"):
      os.mkdir(f"./inputs")

    date = datetime.now().strftime("%Y%m%d")
    path = f"./inputs/{date}_{post_name}.html"
    post_title = post_name.replace("-", " ")
    content = f"<h2>{post_title}</h2>"
    if post_type == "markdown":
      path = path.replace(".html", ".md")
      content = f"## {post_title}"

    file = open(path, "w")
    file.write(content)
    file.close()

    print("Post created!")
    print(f"Start editing {path}")
