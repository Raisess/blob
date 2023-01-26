import os
from datetime import datetime

from yacli import Command

class PostCommand(Command):
  def __init__(self):
    super().__init__("post", "Create a new post. E.g.: blob post markdown post-name", args_len=2)
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

    with open(path, "w") as file:
      file.write(content)

    print("Post created!")
    print(f"Start editing {path}")
