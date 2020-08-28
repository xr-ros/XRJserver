from ROS_nano import views
from xrJserver.base_class.url import url

urls = [
    url("servo/arm", views.arm),
    url("servo/tilt", views.tilt),
    url("movement", views.movement),
    url("sc", views.sc),
    url("xrrobot/battery", views.battery),
]

