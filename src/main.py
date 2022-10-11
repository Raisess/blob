#! /usr/bin/env python3

import os
import sys
from generator import Generator
from server import Server

def init(project_name: str):
  if not os.path.isdir(f"./{project_name}"):
    os.mkdir(f"./{project_name}")
    file = open(f"./{project_name}/.env", "w")
    file.write(f"STATIC_TITLE={project_name}")
    file.close()

  if not os.path.isdir(f"./{project_name}/inputs"):
    os.mkdir(f"./{project_name}/inputs")
  if not os.path.isdir(f"./{project_name}/blog"):
    os.mkdir(f"./{project_name}/blog")

  print("Blog created!")
  print(f"\n\tcd {project_name}")


if __name__ == "__main__":
  if len(sys.argv) < 2:
    raise Exception("Invalid command")
  elif sys.argv[1] == "init":
    init(sys.argv[2])
  elif sys.argv[1] == "serve":
    app = Server('localhost', 8000)
    app.listen()
  elif sys.argv[1] == "generate":
    Generator.Generate()
  else:
    raise Exception("Invalid command")
