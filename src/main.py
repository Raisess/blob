#! /usr/bin/env python3

import os
import sys
from generator import Generator
from server import Server

if __name__ == "__main__":
  if not os.path.isdir("./inputs"):
    os.mkdir("./inputs")

  if len(sys.argv) < 2 or sys.argv[1] == "serve":
    app = Server('localhost', 8000)
    app.listen()
  elif sys.argv[1] == "generate":
    generator = Generator(sys.argv[2])
    generator.generate()
  else:
    raise Exception("Invalid command")
