# -*- coding: UTF-8 -*-

# -------------------------------------------------------------------------------
# {"Jan": 1, "Feb": 2, "Mar": 3, "Apr": 4, "May": 5, "Jun": 6, "Jul": 7, "Aug": 8, "Sep": 9, "Oct": 10, "Nov": 11, "Dec": 12}
# {"Mon": 1, "Tue": 2, "Wed": 3, "Thu": 4, "Fri": 5, "Sat": 6, "Sun": 7}
# {"1st": 1, "2nd": 2, "3th": 3, "4th": 4, "5th": 5}
# -------------------------------------------------------------------------------
# EN: Definition of mapping between TAG and INT;
# CN: 标识与数字的映射定义;


# -------------------------------------------------------------------------------
# ("D", 2, 1)
#   ┃   ┃  ┗━ Which Day   : "1, 2, 3, ..."
#   ┃   ┗━━━━ Which Month : "1, 2, 3, ..." OR "Jan, Feb, Mar, ..."
#   ┗━━━━━━━━ Method Key  : "D", "d"
# -------------------------------------------------------------------------------
# EN: Using the calculation method based on year, month, and day ("D", "d");
# CN: 使用按年月日的计算方法("D", "d");


# -------------------------------------------------------------------------------
# ("W", 5, 2, 7)
#   ┃   ┃  ┃  ┗━ Which day of the week : "1, 2, 3, ..." OR "Mon, Tue, Wed, ..."
#   ┃   ┃  ┗━━━━ Which week            : "1, 2, 3, ..." OR "1st, 2nd, 3th, ..."
#   ┃   ┗━━━━━━━ Which Month           : "1, 2, 3, ..." OR "Jan, Feb, Mar, ..."
#   ┗━━━━━━━━━━━ Method Key            : "W", "w"
# -------------------------------------------------------------------------------
# EN: Calculation method based on the day of the week in a certain month ("W", "w")
#     E.g. : "Mother's Day": [("W", 5, 2, 7)]
#     Note : The second Sunday of May every year must be Mother's Day;
# CN: 按某月第几个星期几的计算方法("W", "w")
#     示例 : "Mother's Day": [("W", 5, 2, 7)]
#     说明 : 每年5月的第2个的星期日必定为母亲节;


# UTCMode = [False, 8]               | * Default Value When Undefined : [False, 8]
# weekends = [6, 7]                  | * Default Value When Undefined : [6, 7]
# yearRange = None                   | * Default Value When Undefined : None
# festivalsEveryYearRepeat = {}      | * Default Value When Undefined : { this year : {}}
# festivalsEveryYearDiff = {}        | * Default Value When Undefined : --
# holidaysEveryYearRepeat = {}       | * Default Value When Undefined : { this year : {}}
# holidaysEveryYearDiff = {}         | * Default Value When Undefined : --
# workdaysEveryYearRepeat = {}       | * Default Value When Undefined : { this year : {}}
# workdaysEveryYearDiff = {}         | * Default Value When Undefined : --

def myCalcMethodA():
    return ("D", 1, 1)


def myCalcMethodB():
    return ("D", 1, 2)


def myCalcMethodC():
    return ("W", 7, 3, 1)


UTCMode = [True, 8]
weekends = [5, 6, 7]
festivalsEveryYearRepeat = {"OOXX Day": [myCalcMethodA()]}
holidaysEveryYearRepeat = {"OOXX Day": [myCalcMethodB()]}
workdaysEveryYearRepeat = {"OOXX Day": [myCalcMethodC()]}
