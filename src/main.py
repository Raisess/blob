#! /usr/bin/env python3

import os
import sys
from server import Server

if __name__ == "__main__":
  if not os.path.isdir("./public/posts"):
    os.mkdir("./public/posts")

  if len(sys.argv) < 2 or sys.argv[1] == "serve":
    app = Server('localhost', 8000)
    app.listen()
  elif sys.argv[1] == "generate":
    print("TODO: Generate html files")
  else:
    raise Exception("Invalid command")
