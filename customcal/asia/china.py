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

UTCMode = [True, 8]
weekends = [6, 7]
yearRange = None

festivalsEveryYearRepeat = {
    "New Year": [("D", 1, 1)], "Valentine's Day": [("D", 2, 14)], "Women's Day": [("D", 3, 8)], "Labour Day": [("D", 5, 1)],
    "Youth Day": [("D", 5, 4)], "Mother's Day": [("W", 5, 2, 7)], "Children's Day": [("D", 6, 1)], "Father's Day": [("W", 6, 3, 7)],
    "National Day": [("D", 10, 1)], "All Hallows' Eve": [("D", 10, 31)], "All Saints' Day": [("D", 11, 1)], "Thanksgiving": [("W", 11, 4, 4)],
    "Christmas Eve": [("D", 12, 23)], "Christmas' Day": [("D", 12, 24)]
}

festivalsEveryYearDiff = {
    2024:
    {
        "Spring Festival": [("D", 2, 10)],
        "Ching Ming Festival": [("D", 4, 4)],
        "Dragon Boat Festival": [("D", 6, 10)],
        "Mid-Autumn Festival": [("D", 9, 17)],
    }
}

holidaysEveryYearDiff = {
    2024:
    {
        "New Year": [("D", 1, 1)],
        "Spring Festival": [("D", 2, 10), ("D", 2, 11), ("D", 2, 12), ("D", 2, 13), ("D", 2, 14), ("D", 2, 15), ("D", 2, 16), ("D", 2, 17)],
        "Ching Ming Festival": [("D", 4, 4), ("D", 4, 5), ("D", 4, 6)],
        "Labour Day": [("D", 5, 1), ("D", 5, 2), ("D", 5, 3), ("D", 5, 4), ("D", 5, 5)],
        "Dragon Boat Festival": [("D", 6, 8), ("D", 6, 9), ("D", 6, 10)],
        "Mid-Autumn Festival": [("D", 9, 15), ("D", 9, 16), ("D", 9, 17)],
        "National Day": [("D", 10, 1), ("D", 10, 2), ("D", 10, 3), ("D", 10, 4), ("D", 10, 5), ("D", 10, 6), ("D", 10, 7)]
    }
}

workdaysEveryYearDiff = {
    2024:
    {
        "New Year": [],
        "Spring Festival": [("D", 2, 4), ("D", 2, 18)],
        "Ching Ming Festival": [("D", 4, 7)],
        "Labour Day": [("D", 4, 28), ("D", 5, 11)],
        "Dragon Boat Festival": [],
        "Mid-Autumn Festival": [("D", 9, 14)],
        "National Day": [("D", 9, 29), ("D", 10, 12)]
    }
}
