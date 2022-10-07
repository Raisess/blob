from http import server
import socketserver

class RequestHandler(server.SimpleHTTPRequestHandler):
  def do_GET(self) -> None:
    base_html = self._find_html("base.html")

    try:
      page = "index.html" if self.path == "/" else f"posts{self.path}.html"
      current_html = self._find_html(page)

      html = base_html.replace("{{TITLE}}", "BLOB")
      html = html.replace("{{POST}}", current_html)

      self.send_response(200)
      self.send_header("Content-type", "text/html")
      self.end_headers()
      self.wfile.write(bytes(html, "utf-8"))
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

  def _find_html(self, path: str) -> str:
    if not path.endswith(".html"):
      raise Exception("Invalid file format")

    file = open("public/" + path, "r")
    html = file.read()
    file.close()
    return html

class Server:
  def __init__(self, host: str, port: int):
    self.host = host;
    self.port = port;

  def listen(self) -> None:
    with socketserver.TCPServer((self.host, self.port), RequestHandler) as instance:
      print(f"Running at http://{self.host}:{self.port}")
      instance.serve_forever()
