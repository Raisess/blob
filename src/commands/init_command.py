import os

from yacli import Command

class InitCommand(Command):
  def __init__(self):
    super().__init__("init", "Start a new blog.", args_len=1)

  def handle(self, args: list[str]) -> None:
    project_name = args[0]
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
    print(f"cd {project_name}")
