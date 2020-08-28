from xrJserver.base_class.Response import Response


def default(request):
    # print("data got!!")
    data = None
    return Response(request, data)
