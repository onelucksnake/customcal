# -*- coding: UTF-8 -*-
class calendarError(Exception):
    pass


class UnSupportCountry(calendarError):
    """
    Raised when your country is not supported .
    """


class WrongCalcMethod(calendarError):
    """
    Raised when wrong definition of date calculation method .
    """
