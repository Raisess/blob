from http.server import SimpleHTTPRequestHandler
from socketserver import TCPServer

from view.view import ListView, PostView, ErrorView

class RequestHandler(SimpleHTTPRequestHandler):
  def do_GET(self) -> None:
    try:
      html = ListView() if self.path == "/blog" else PostView(f"./{self.path}")

      self.send_response(200)
      self.send_header("Content-type", "text/html")
      self.end_headers()
      self.wfile.write(html.content_bytes)
    except:
      html = ErrorView(404, "Not Found")

      self.send_response(404)
      self.send_header("Content-type", "text/html")
      self.end_headers()
      self.wfile.write(html.content_bytes)


class Server:
  def __init__(self, host: str, port: int):
    self.__host = host
    self.__port = port

  def listen(self) -> None:
    with TCPServer((self.__host, self.__port), RequestHandler) as instance:
      print(f"Running at http://{self.__host}:{self.__port}/blog")

      try:
        instance.serve_forever()
      except KeyboardInterrupt:
        instance.shutdown()
