#! /usr/bin/env python3

import os
import sys
from datetime import datetime
from generator import Generator
from server import Server

def init(project_name: str) -> None:
  if not os.path.isdir(f"./{project_name}"):
    os.mkdir(f"./{project_name}")
  if not os.path.isdir(f"./{project_name}/inputs"):
    os.mkdir(f"./{project_name}/inputs")
  if not os.path.isdir(f"./{project_name}/blog"):
    os.mkdir(f"./{project_name}/blog")

  if not os.path.isfile(f"./{project_name}/.env"):
    with open(f"./{project_name}/.env", "w") as file:
      file.write(f"TITLE={project_name}\nDESCRIPTION={project_name}\n")
      file.close()

  print("Blog created!")
  print(f"\n\tcd {project_name}")


def post(post_name: str, markdown = False) -> None:
  if not os.path.isdir(f"./inputs"):
    os.mkdir(f"./inputs")

  date = datetime.now().strftime("%Y%m%d")
  path = f"./inputs/{date}_{post_name}.html"
  post_title = post_name.replace("-", " ")
  content = f"<h2>{post_title}</h2>"
  if markdown:
    path = path.replace(".html", ".md")
    content = f"## {post_title}"

  file = open(path, "w")
  file.write(content)
  file.close()

  print("Post created!")
  print(f"Start editing {path}")


if __name__ == "__main__":
  if len(sys.argv) < 2:
    raise Exception("Invalid command")
  elif sys.argv[1] == "init":
    init(sys.argv[2])
  elif sys.argv[1] == "post":
    post(sys.argv[2])
  elif sys.argv[1] == "post-md":
    post(sys.argv[2], True)
  elif sys.argv[1] == "serve":
    app = Server('localhost', 8000)
    app.listen()
  elif sys.argv[1] == "generate":
    Generator.Generate()
  elif sys.argv[1] == "help":
    print("init: start's a new blog")
    print("post: create a new html post")
    print("post-md: create a new markdown post")
    print("serve: start's a local server to look to results at port 8000")
    print("generate: transform the files from the input folder to upload ready blog posts on the blog folder")
    print("\nThanks for using blob @ Raisess")
  else:
    raise Exception("Invalid command")
