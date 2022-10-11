#! /usr/bin/env python3

import os
import sys
from datetime import datetime
from generator import Generator
from server import Server

def init(project_name: str):
  if not os.path.isdir(f"./{project_name}"):
    os.mkdir(f"./{project_name}")
    file = open(f"./{project_name}/.env", "w")
    file.write(f"STATIC_TITLE={project_name}\n")
    file.close()

  if not os.path.isdir(f"./{project_name}/inputs"):
    os.mkdir(f"./{project_name}/inputs")
  if not os.path.isdir(f"./{project_name}/blog"):
    os.mkdir(f"./{project_name}/blog")

  print("Blog created!")
  print(f"\n\tcd {project_name}")


def post(post_name: str):
  if not os.path.isdir(f"./inputs"):
    os.mkdir(f"./inputs")

  date = datetime.now().strftime("%Y%m%d")
  file = open(f"./inputs/{date}_{post_name}.html", "w")
  post_title = post_name.replace("-", " ")
  file.write(f"<h2>{post_title}</h2>")
  file.close()

  print("Post created!")
  print(f"Start editing inputs/{post_name}")


if __name__ == "__main__":
  if len(sys.argv) < 2:
    raise Exception("Invalid command")
  elif sys.argv[1] == "init":
    init(sys.argv[2])
  elif sys.argv[1] == "post":
    post(sys.argv[2])
  elif sys.argv[1] == "serve":
    app = Server('localhost', 8000)
    app.listen()
  elif sys.argv[1] == "generate":
    Generator.Generate()
  else:
    raise Exception("Invalid command")
