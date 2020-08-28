import sys

from xrJserver.middleware.building_middleware import illegal_request_middleware

version = "b0.0"

request_middleware = [illegal_request_middleware, ]
response_middleware = []

data_url = sys.path[0] + "/xrJserver/data/"

data_container = {}
