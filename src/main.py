#! /usr/bin/env python3

from yacli import CLI

from commands.generate_command import GenerateCommand
from commands.init_command import InitCommand
from commands.post_command import PostCommand
from commands.serve_command import ServeCommand

if __name__ == "__main__":
  cli = CLI("blob", [
    InitCommand(),
    PostCommand(),
    ServeCommand(),
    GenerateCommand()
  ])
  cli.handle()
