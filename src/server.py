from http import server
import socketserver
from view import View

class RequestHandler(server.SimpleHTTPRequestHandler):
  def do_GET(self) -> None:
    try:
      page = "index.html" if self.path == "/" else f"posts{self.path}.html"
      html = View("BLOB", page)

      self.send_response(200)
      self.send_header("Content-type", "text/html")
      self.end_headers()
      self.wfile.write(bytes(html.content, "utf-8"))
    except FileNotFoundError:
      self.send_response(404)
      self.send_header("Content-type", "text/html")
      self.end_headers()
      self.wfile.write(bytes("<h1>NOT FOUND<h1/>", "utf-8"))
    except:
      self.send_response(500)
      self.send_header("Content-type", "text/html")
      self.end_headers()
      self.wfile.write(bytes("<h1>INTERNAL SERVER ERROR<h1/>", "utf-8"))

class Server:
  def __init__(self, host: str, port: int):
    self.host = host;
    self.port = port;

  def listen(self) -> None:
    with socketserver.TCPServer((self.host, self.port), RequestHandler) as instance:
      print(f"Running at http://{self.host}:{self.port}")
      instance.serve_forever()
