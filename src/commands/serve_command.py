from yacli import Command

from server.server import Server

class ServeCommand(Command):
  def __init__(self):
    super().__init__(
      "serve",
      "Start a local server to look to results at port 8000."
    )

  def handle(self, args: list[str]) -> None:
    port = int(args[0]) if len(args) >= 1 else 8000
    app = Server("localhost", port)
    app.listen()
