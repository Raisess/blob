from yacli import Command

from view.generator import Generator

class GenerateCommand(Command):
  def __init__(self):
    super().__init__(
      "generate",
      "Transform the files from the input folder to upload ready blog posts on the blog folder."
    )

  def handle(self, _: list[str]) -> None:
    Generator.Generate()
