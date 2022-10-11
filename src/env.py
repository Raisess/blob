from typing import Optional

class EnvParser:
  def parse() -> dict[str]:
    try:
      file = open("./.env", "r")
      content = file.read()
      file.close()

      lines = content.split("\n")
      lines.pop()

      env: dict[str] = {}
      for line in lines:
        (key, value) = line.split("=")
        env[key] = value

      return env
    except:
      return {}


class Env:
  def __init__(self):
    self._data = EnvParser.parse()

  def get(self, key: str) -> Optional[str]:
    return self._data.get(key)

env = Env()
