import socket
import json
import time
import threading

import rospy
from riki_msgs.msg import Battery
from geometry_msgs.msg import Twist
from sensor_msgs.msg import JointState


def send_msg():
    while app_is_run:
        try:
            robot_socket.connect(("127.0.0.1", 11322))

            while app_is_run:
                if send_bytes:
                    # 	xrJson = {
                    # 		"version": "b0.0",
                    # 		"keep_alive": True,
                    # 		"url": "/default/",
                    # 		"method": "get",
                    # 		"data": {},
                    # 	}
                    # 	send_bytes.append(json.dumps(xrJson).encode("utf-8"))
                    # continue

                    robot_socket.send(send_bytes.pop())
                    time.sleep(0.01)

                xrJson = {
                    "version": "b0.0",
                    "keep_alive": True,
                    "url": "/movement",
                    "method": "get",
                    "data": {},
                }

                tem_data = json.dumps(xrJson).encode("utf-8")
                robot_socket.send(tem_data)

            recv = robot_socket.recv(500)
            recv = json.loads(recv)
            if "direction" in recv.data:
                pub_movement(recv.data["direction"])

            time.sleep(0.01)

        except Exception as e:
            print(e)
            time.sleep(0.5)


def pub_movement(movement):
    if not isinstance(movement, type("")):
        return False

    move_msg = Twist()
    if movement == "stop":
        move_msg.angular = 0
        move_msg.linear = 0

    elif movement == "left":
        move_msg.angular = -robot_speed * 0.5
        move_msg.linear = 0

    elif movement == "right":
        move_msg.angular = robot_speed * 0.5
        move_msg.linear = 0

    elif movement == "forward":
        move_msg.angular = 0
        move_msg.linear = robot_speed

    elif movement == "backward":
        move_msg.angular = 0
        move_msg.linear = -robot_speed

    movement_pub.publish()


def battery_callback(msg):
    global send_bytes
    remaining_electricity = msg.battery
    print(msg.battery)

    xrJson = {
        "version": "b0.0",
        "keep_alive": True,
        "url": "/xrrobot/battery",
        "method": "post",
        "data": {"remaining_electricity": float(remaining_electricity)},
    }

    send_bytes.append(json.dumps(xrJson).encode("utf-8"))


send_bytes = []

robot_speed = 1

robot_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
robot_thread = threading.Thread(target=send_msg)

battery_msg = Battery()
POWER_SUB = rospy.Subscriber('battery', Battery, battery_callback)

servo = JointState()
servo_pub = rospy.Publisher('joint_states', JointState, queue_size=10)
movement_pub = rospy.Publisher('cmd_vel', Twist, queue_size=10)

rospy.init_node('robot_status_interaction')

rospy.loginfo('robot_status_interaction node is running!')

app_is_run = True
robot_thread.start()

rospy.spin()

app_is_run = False
robot_socket.close()
robot_thread.join()