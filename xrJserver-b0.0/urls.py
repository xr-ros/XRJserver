import views
from xrJserver.base_class.url import url
from tool.url_tool import include

import app.urls
import ROS_nano.urls

urls = [
    url("/default/", views.default),
    include("/test", app.urls.urls),
    include("/", ROS_nano.urls.urls),
]

