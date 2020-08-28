from xrJserver.base_class.url import url
from app import views

urls = [
    url(r"/test1", views.test1),
    url(r"/test2", views.test2),
    url(r"/test3", views.test3),
    url(r"/", views.test),
]