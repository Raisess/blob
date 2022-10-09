from http.server import SimpleHTTPRequestHandler
from socketserver import TCPServer
from env import Env
from view import ListView, PostView, ErrorView

class RequestHandler(SimpleHTTPRequestHandler):
  def do_GET(self) -> None:
    try:
      if self.path.startswith("/blog"):
        env = Env()
        if self.path == "/blog":
          html = ListView(env.get("STATIC_TITLE"))
        else:
          html = PostView(env.get("STATIC_TITLE"), f"./{self.path}")

        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(html.content_bytes)
    except FileNotFoundError:
      html = ErrorView(404, "Not Found")

      self.send_response(404)
      self.send_header("Content-type", "text/html")
      self.end_headers()
      self.wfile.write(html.content_bytes)
    except:
      html = ErrorView(500, "Internal Server Error")

      self.send_response(500)
      self.send_header("Content-type", "text/html")
      self.end_headers()
      self.wfile.write(html.content_bytes)


class Server:
  def __init__(self, host: str, port: int):
    self.host = host;
    self.port = port;

  def listen(self) -> None:
    with TCPServer((self.host, self.port), RequestHandler) as instance:
      print(f"Running at http://{self.host}:{self.port}")

      try:
        instance.serve_forever()
      except KeyboardInterrupt:
        instance.shutdown()
