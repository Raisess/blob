import atexit
import traceback

from http.server import SimpleHTTPRequestHandler
from socketserver import TCPServer

from view import ListView, PostView, ErrorView

class RequestHandler(SimpleHTTPRequestHandler):
  def do_GET(self) -> None:
    try:
      if self.path == "/blog" or self.path.endswith(".html") or self.path.endswith(".md"):
        html = ListView() if self.path == "/blog" else PostView(f"./{self.path}")

        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(html.content_bytes())
      else:
        path = self.path.replace("blog", "inputs")
        content = bytes()
        with open(f"./{path}", "rb") as file:
          content = file.read()

        self.send_response(200)
        self.send_header("Content-type", "image/png")
        self.end_headers()
        self.wfile.write(content)
    except FileNotFoundError:
      html = ErrorView(404, "Not Found")

      self.send_response(404)
      self.send_header("Content-type", "text/html")
      self.end_headers()
      self.wfile.write(html.content_bytes())
    except:
      trace = traceback.format_exc()
      print(trace)
      html = ErrorView(500, trace)

      self.send_response(500)
      self.send_header("Content-type", "text/html")
      self.end_headers()
      self.wfile.write(html.content_bytes())


class Server:
  def __init__(self, host: str, port: int):
    self.__host = host
    self.__port = port

  def listen(self) -> None:
    with TCPServer((self.__host, self.__port), RequestHandler) as instance:
      def close() -> None:
        instance.server_close()
        instance.shutdown()

      atexit.register(close)

      print(f"Running at http://{self.__host}:{self.__port}/blog")

      try:
        instance.serve_forever()
      except KeyboardInterrupt:
        close()
