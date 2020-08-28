from copy import deepcopy
from os import system

from ROS_nano.model import Arm_servo, Tilt_servo, Movement, Battery, Sc
from xrJserver.base_class.Response import Response, DataErrorResponse, MethodNotSupportResponse


def arm(request):
    # while method is get
    if request.method == "get":
        arm_servo = Arm_servo()
        data = arm_servo.get()
        print("read arm", data)
        return Response(request, data)

    # while method is post
    if request.method == "post":
        if "servo" in request.data:
            if len(request.data["servo"]) == 4:

                # get arm servo parm
                arm_servo = Arm_servo()
                data = arm_servo.get()
                for i in range(4):
                    angel_is_not_empty = request.data["servo"][i]
                    if angel_is_not_empty:
                        data["servo"][i] = angel_is_not_empty

                # update arm servo
                arm_servo.set("servo", data["servo"])
                arm_servo.save()
                print("operating arm", data)
                return Response(request)

#         while request no servo data or servo data'lenth not 4, this is an error data
        return DataErrorResponse(request)
    # while request'method is not get or post
    return MethodNotSupportResponse(request)


def tilt(request):
    # while method is get
    if request.method == "get":
        tilt_servo = Tilt_servo()
        data = tilt_servo.get()
        print("read tilt")
        return Response(request, data)

    # while method is post
    if request.method == "post":
        if "servo" in request.data:
            if len(request.data["servo"]) == 2:

                # get arm servo parm
                tilt_servo = Tilt_servo()
                data = tilt_servo.get()
                for i in range(2):
                    angel_is_not_empty = request.data["servo"][i]
                    if angel_is_not_empty:
                        data["servo"][i] = angel_is_not_empty

                # update arm servo
                tilt_servo.set("servo", data["servo"])
                tilt_servo.save()
                print("operating tilt", tilt_servo.get())
                return Response(request)

        #         while request no servo data or servo data'lenth not 2, this is an error data
        return DataErrorResponse(request)
    # while request'method is not get or post
    return MethodNotSupportResponse(request)


def movement(request):
    # if method is post
    if request.method == "post":
        if "direction" in request.data:
            current_movement = Movement()

            # save movement data
            current_movement.set("direction", request.data["direction"])
            current_movement.save()

            # feedback operation result
            data = {"msg": "operate success"}
            print("moving")
            return Response(request, data=data)
        return DataErrorResponse(request)

    # if method is get
    elif request.method == "get":
        # get movement data
        current_movement = Movement()
        data = deepcopy(current_movement.get())

        return Response(request, data=data)

    # while request'method is not post
    return MethodNotSupportResponse(request)


def sc(request):
    if request.method == "get":
        sc_data = Sc()
        data = sc_data.get()

        system("echo 'get sc' >> ../log/main.log")
        print("get sc", data)
        return Response(request, data=data)

    if request.method == "post":
        sc_data = Sc()
        if "sc" in request.data:
            target_scc = request.data["sc"]
            sc_data.set("sc", target_scc)

        if "k" in request.data:
            target_k = request.data["k"]
            sc_data.set("k", target_k)

        if "sc_slave_is_alive" in request.data:
            sc_data.set("sc_slave_is_alive", request.data["sc_slave_is_alive"])

        if "is_update" in request.data:
            sc_data.set("is_update", request.data["is_update"])

        sc_data.save()
        system("echo 'post sc' >> ../log/main.log")
        print("post data")
        return Response(request)

    # while request'method is not post
    return MethodNotSupportResponse(request)


def battery(request):
    if request.method == "get":
        current_battery = Battery()
        data = current_battery.get()
        print("feedback battery", data)
        system("echo 'feedback battery' >> ../log/main.log")
        return Response(request, data=data)

    elif request.method == "post":
        current_battery = Battery()
        if "remaining_electricity" in request.data:
            target_battery = request.data["remaining_electricity"]
            # print(target_battery)
            # print(type(target_battery))
            current_battery.set("remaining_electricity", target_battery)
            current_battery.save()
            print("get battery")
            return Response(request)

        return DataErrorResponse(request)

    # while request'method is not post
    return MethodNotSupportResponse(request)
