import json
from setting import version


class Response(object):
    def __init__(self, requests, data={}, status=200):
        self.data = data
        response = {
            "version": version,
            "status": status,
            "data": data,
        }
        self.response = json.dumps(response).encode(encoding="utf-8")


class DataErrorResponse(Response):
    def __init__(self, requests):
        self.data = {"msg": "the data you send  is wrongful"}
        response = {
            "version": version,
            "status": 406,
            "data": self.data,
        }
        self.response = json.dumps(response).encode(encoding="utf-8")


class NotFoundResponse(Response):
    def __init__(self, requests):
        self.data = {"msg": "this Api not found"}
        response = {
            "version": version,
            "status": 404,
            "data": self.data,
        }
        self.response = json.dumps(response).encode(encoding="utf-8")


class MethodNotSupportResponse(Response):
    def __init__(self, requests):
        self.data = {"msg": "this method is not supported"}
        response = {
            "version": version,
            "status": 405,
            "data": self.data,
        }
        self.response = json.dumps(response).encode(encoding="utf-8")


class IllegalRequestResponse(Response):
    def __init__(self, requests):
        self.data = {"msg": "your request is illegal"}
        response = {
            "version": version,
            "status": 400,
            "data": self.data,
        }
        self.response = json.dumps(response).encode(encoding="utf-8")