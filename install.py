#! /usr/bin/env python3

import os
import shutil
import site
import sys

CLI_NAME = "blob"

BIN_PATH = f"/usr/local/bin/{CLI_NAME}"
LIB_PATH = f"/usr/local/lib/{CLI_NAME}"
ETC_PATH = f"/usr/local/etc/{CLI_NAME}"

if __name__ == "__main__":
  print(f"Installing {CLI_NAME}...")

  if not os.path.isdir(f"{site.USER_SITE}/yacli"):
    os.system("""
      git clone https://github.com/Raisess/yacli
      cd yacli
      ./install.sh
    """)
    os.rmdir("yacli")

  if os.path.isdir(BIN_PATH):
    os.remove(BIN_PATH)
  shutil.copy(f"./bin/{CLI_NAME}", BIN_PATH)

  if os.path.isdir(LIB_PATH):
    shutil.rmtree(LIB_PATH)
  shutil.copytree("./src", LIB_PATH)

  if os.path.isdir("./etc"):
    if os.path.isdir(ETC_PATH):
      shutil.rmtree(ETC_PATH)
    shutil.copytree("./etc", ETC_PATH)

  print("Installed successfully!")
