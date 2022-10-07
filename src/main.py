#! /usr/bin/env python3

import os
from server import Server

def get_print():
  print("TEST")

if __name__ == "__main__":
  if not os.path.isdir("./public/posts"):
    os.mkdir("./public/posts")

  app = Server('localhost', 8000)
  app.listen()
