from enum import Enum
from socket import gethostname, gethostbyname
from datetime import datetime


class Status(Enum):
    Active = 1
    Modified = 2
    Passive = 3


class BaseEntity:
    def __init__(self):
        self.__status = ''
        self.__created_date = ''
        self.__machine_name = ''
        self.__ip_address = ''

    def set_values(self):
        self.__status = Status.Active.name
        self.__created_date = datetime.now()
        self.__machine_name = gethostname()
        self.__ip_address = gethostbyname(gethostname())


class Category(BaseEntity):
    def __init__(self, name, description):
        super().__init__()
        self.description = description
        self.name = name
        super().set_values()

