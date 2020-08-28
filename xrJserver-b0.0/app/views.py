from app.model import default_model
from xrJserver.base_class.Response import Response


def test1(request):
    if request.method == "post":
        my_model = default_model()
        my_model.set("sc", request.data["sc"])
        my_model.save()
        data = my_model.get()
        print(data)
        return Response(request, data)

    elif request.method == "get":
        my_model = default_model()
        data = my_model.get()
        return Response(request, data)


def test2(request):
    pass


def test3(request):
    pass


def test(request):
    pass
