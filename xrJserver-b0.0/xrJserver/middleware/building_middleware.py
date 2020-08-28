import json
from json import JSONDecodeError

from xrJserver.base_class import Response


def illegal_request_middleware(request):
    try:
        json_content = json.loads(request.content)
        version = json_content["version"]
        data = json_content["data"]
        method = json_content["method"]
        url = json_content["url"]
        keep_alive = json_content["keep_alive"]
    except JSONDecodeError:
        print("input is'nt a json string")
        print(request.content)
        return Response.IllegalRequestResponse(request)
    except KeyError:
        print("input is'nt a xrJson string")
        return Response.IllegalRequestResponse(request)


