import json
from json import JSONDecodeError


class Request(object):
    def __init__(self, connect, addr, content):
        self.connect = connect
        self.addr = addr
        self.content = content
        self.keep_alive = False

        try:
            json_content = json.loads(content)
            self.version = json_content["version"]
            self.data = json_content["data"]
            self.method = json_content["method"]
            self.url = json_content["url"]
            self.keep_alive = json_content["keep_alive"]

        # if input not a json string, return a error
        except Exception:
            self.data = None
