from xrJserver.base_class.xr_base import xr_base


class Arm_servo(xr_base):
    data = {
        "servo": ['0', '0', '0', '0'],
    }


class Tilt_servo(xr_base):
    data = {
        "servo": ['0', '0'],
    }


class Movement(xr_base):
    data = {
        "direction": "stop",
    }


class Sc(xr_base):
    data = {
        "sc": 0,
        "k": 100,
        "sc_slave_is_alive": False,
        "is_update": False,
    }


class Battery(xr_base):
    data = {
        "remaining_electricity": 12.0,
    }
