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
#     E.g. : "母亲节": [("W", 5, 2, 7)]
#     Note : The second Sunday of May every year must be 母亲节;
# CN: 按某月第几个星期几的计算方法("W", "w")
#     示例 : "母亲节": [("W", 5, 2, 7)]
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


import datetime

UTCMode = [True, 8]
weekends = [6, 7]
yearRange = None

festivalsEveryYearRepeat = {
    "元旦": [("D", 1, 1)], "情人节": [("D", 2, 14)], "妇女节": [("D", 3, 8)], "劳动节": [("D", 5, 1)],
    "青年节": [("D", 5, 4)], "母亲节": [("W", 5, 2, 7)], "儿童节": [("D", 6, 1)], "父亲节": [("W", 6, 3, 7)],
    "国庆节": [("D", 10, 1)], "万圣夜": [("D", 10, 31)], "万圣节": [("D", 11, 1)], "感恩节": [("W", 11, 4, 4)],
    "平安夜": [("D", 12, 23)], "圣诞节": [("D", 12, 24)]
}

festivalsEveryYearDiff = {
    2024:
    {
        "春节": [("D", 2, 10)],
        "清明": [("D", 4, 4)],
        "端五节": [("D", 6, 10)],
        "中秋节": [("D", 9, 17)],
    }
}

holidaysEveryYearDiff = {
    2024:
    {
        "元旦": [("D", 1, 1)],
        "春节": [("D", 2, 10), ("D", 2, 11), ("D", 2, 12), ("D", 2, 13), ("D", 2, 14), ("D", 2, 15), ("D", 2, 16), ("D", 2, 17)],
        "清明": [("D", 4, 4), ("D", 4, 5), ("D", 4, 6)],
        "劳动节": [("D", 5, 1), ("D", 5, 2), ("D", 5, 3), ("D", 5, 4), ("D", 5, 5)],
        "端五节": [("D", 6, 8), ("D", 6, 9), ("D", 6, 10)],
        "中秋节": [("D", 9, 15), ("D", 9, 16), ("D", 9, 17)],
        "国庆节": [("D", 10, 1), ("D", 10, 2), ("D", 10, 3), ("D", 10, 4), ("D", 10, 5), ("D", 10, 6), ("D", 10, 7)]
    }
}

workdaysEveryYearDiff = {
    2024:
    {
        "元旦": [],
        "春节": [("D", 2, 4), ("D", 2, 18)],
        "清明": [("D", 4, 7)],
        "劳动节": [("D", 4, 28), ("D", 5, 11)],
        "端五节": [],
        "中秋节": [("D", 9, 14)],
        "国庆节": [("D", 9, 29), ("D", 10, 12)]
    }
}


# ========================================================================================================
# 计算"二十四节气"
#
# 网址 : https://www.jianshu.com/p/1f814c6bb475
# 公式 : [ Y × D + C ] - L
# 代码 : - ["小寒", "大寒", "立春", "雨水"]
#          int(year % 100 * 0.2422 + rule[1]) - int(((year % 100 - 1)/4))
#        - 其它
#          int(year % 100 * 0.2422 + rule[1]) - int(((year % 100)/4))
solarTermsRule = {
    "1901-2000": {
        "立春": (2, 4.6295, None), "雨水": (2, 19.4599, None), "惊蛰": (3, 6.3826, None),
        "春风": (3, 21.4155, None), "清明": (4, 5.59, None), "谷雨": (4, 20.888, None),
        "立夏": (5, 6.318, (1911, 1)), "小满": (5, 21.86, None), "芒种": (6, 6.5, (1902, 1)),
        "夏至": (6, 22.2, (1928, 1)), "小暑": (7, 7.928, (1925, 1)), "大暑": (7, 23.65, (1922, 1)),
        "立秋": (8, 28.35, None), "处暑": (8, 23.95, None), "白露": (9, 8.44, (1927, 1)),
        "秋分": (9, 23.822, (1942, 1)), "寒露": (10, 9.098, None), "霜降": (10, 24.218, None),
        "立冬": (11, 8.218, None), "小雪": (11, 23.08, (1987, 1)), "大雪": (12, 7.9, (1954, 1)),
        "冬至": (12, 22.6, (1918, -1)), "小寒": (1, 6.11, (1982, 1)), "大寒": (1, 20.84, (2000, 1))
    },
    "2001-2100": {
        "立春": (2, 3.87, None), "雨水": (2, 18.73, (2026, -1)), "惊蛰": (3, 5.63, None),
        "春风": (3, 20.646, (2084, 1)), "清明": (4, 4.81, None), "谷雨": (4, 20.1, None),
        "立夏": (5, 5.52, None), "小满": (5, 21.04, (2008, 1)), "芒种": (6, 5.678, None),
        "夏至": (6, 21.37, None), "小暑": (7, 7.108, (2016, 1)), "大暑": (7, 22.83, None),
        "立秋": (8, 7.5, (2002, 1)), "处暑": (8, 23.13, None), "白露": (9, 7.646, None),
        "秋分": (9, 23.043, None), "寒露": (10, 8.318, None), "霜降": (10, 23.438, (2089, 1)),
        "立冬": (11, 7.438, (2089, 1)), "小雪": (11, 22.36, None), "大雪": (12, 7.18, None),
        "冬至": (12, 21.94, (2021, -1)), "小寒": (1, 5.4055, (2019, -1)), "大寒": (1, 20.12, (2082, 1))
    }
}


def calcSolarTerms(festivalsDiff):
    x = ["小寒", "大寒", "立春", "雨水"]
    for year in festivalsDiff.keys():
        if year >= 1901 and year <= 2000:
            for name, rule in solarTermsRule["1901-2000"].items():
                if name in x:
                    day = int(year % 100 * 0.2422 + rule[1]) - int(((year % 100 - 1)/4))
                else:
                    day = int(year % 100 * 0.2422 + rule[1]) - int(((year % 100)/4))
                if rule[2] is None:
                    festivalsDiff[year][name] = [("D", rule[0], day)]
                elif rule[2][0] != year:
                    festivalsDiff[year][name] = [("D", rule[0], day)]
                else:
                    festivalsDiff[year][name] = [("D", rule[0], day + rule[2][1])]
        elif year >= 2001 and year <= 2100:
            for name, rule in solarTermsRule["2001-2100"].items():
                if name in x:
                    day = int(year % 100 * 0.2422 + rule[1]) - int(((year % 100 - 1)/4))
                else:
                    day = int(year % 100 * 0.2422 + rule[1]) - int(((year % 100)/4))
                if rule[2] is None:
                    festivalsDiff[year][name] = [("D", rule[0], day)]
                elif rule[2][0] != year:
                    festivalsDiff[year][name] = [("D", rule[0], day)]
                else:
                    festivalsDiff[year][name] = [("D", rule[0], day + rule[2][1])]
        else:
            continue


# ========================================================================================================
# 在实例化时, 实例化过程中( __init__() ), 会尝试调用"数据文体"中的"modDataUpdate()"函数, 并在调用过程中传入一个
# 列表"[UTCMode, weekends, yearRange]", 你可以利用这些值, 在实例数据生成前, 更新本模块中的各个数据的定义;
# * "[UTCMode, weekends, yearRange]"可能随核心更新而增加可用的选项;
# * 如果你的数据够完整, 你可以不需要定义他;
# * "modDataUpdate()"函数是在"calcore"核心中定义的特殊调用函数, 请别随便使用;
def modDataUpdate(opt):
    if opt[2] is None:
        calS = [datetime.datetime.today().year]
    elif isinstance(opt[2], int):
        calS = [opt[2]]
    elif isinstance(opt[2], tuple) and opt[2][0] < opt[2][1]:
        calS = list(range(opt[2][0], opt[2][1] + 1))
    else:
        return

    for year in calS:
        if year not in festivalsEveryYearDiff:
            festivalsEveryYearDiff[year] = {}
    calcSolarTerms(festivalsEveryYearDiff)
