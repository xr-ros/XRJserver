from xrJserver.base_class.Response import NotFoundResponse


class Router(object):
    def __init__(self, urls):
        self.__urls = urls

    def rout(self, request):

        for url in self.__urls:
            url_verify_is_success = url.verify(request.url)

            if url_verify_is_success:
                _url, fun = url_verify_is_success
                return fun(request)

        # if it didn't match to any url, return NotFoundResponse.
        return NotFoundResponse(request)



