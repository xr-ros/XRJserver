import json
import os

from setting import data_url, data_container


class InstancedError(ValueError):
    def __init__(self):
        print("this base_class of xr_base cant be instanced")
        super().__init__()


class xr_base(object):
    __file_path = ""
    __data = {}
    def __init__(self):

        # Determine whether this class is the base class
        if not self.__class__.__name__ == "xr_base":
            # serialize the data
            self.__serialize(self.data)

        # if instance this base class, raise InstancedError
        else:
            raise InstancedError

    # save data
    @classmethod
    def save(cls):
        data_container[cls.__file_path] = json.dumps(cls.__data)

    @classmethod
    def get(cls):
        return cls.__data

    # set field value
    @classmethod
    def set(cls, field_name, value):
        # Judge whether the data types are consistent
        if isinstance(value, type(cls.__data[field_name])):
            cls.__data[field_name] = value
        else:
            raise TypeError

    @classmethod
    def __serialize(cls, data):
        # set data file path

        cls.__file_path = data_url + cls.__name__ + ".json"

        # if this data_class is Initialized for the first time, write json data to data_container
        if cls.__file_path not in data_container:
            cls.__data = data
            data_container[cls.__file_path] = json.dumps(obj=cls.__data)

        # if the json data exists, load it as data
        else:
            cls.__data = json.loads(data_container[cls.__file_path])
