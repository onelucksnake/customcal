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


UTCMode = [False, 8]
"""
EN: Whether to use UTC mode; Disabled by default [using local time obtained from the system]; When UTC mode is enabled ["True"], the calculation
    of the current date will be based on UTC time plus an offset value; In most cases, it is not necessary to enable it;
    This mainly affects how to calculate today's date in the program; Default value "[False, 0]";
    Note: When creating objects using "class calendar", you can specify the option "UTCMode=" to override this definition;
    Note: For countries using daylight saving time, it is not recommended to enable this mode;
CN: 是否使用UTC模式; 默认不启用[使用系统中获取的本地时间]; 启用UTC模式时["True"], 当前日期的计算会以UTC时间加上偏移值; 大部分情况下, 不需要启用它;
    这主要影响程序中, 如何计算今天的日期; 默认值"[False, 0]";
    注意: 在使用"class calendar"创建对象时, 可以指定选项"UTCMode="覆盖本定义;
    注意: 使用夏令时的国家, 不建议启用此模式;

E.G.
- UTCMode = [Ture, 0]
- UTCMode = [Ture, 8]
"""


weekends = [6, 7]
"""
EN: In general, there are fixed rest days per week; Available values: '1, 2, 3, 4, 5, 6, 7' or 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun';
    Note: When creating objects using "class calendar", you can specify the option "weekends=" to override this definition;
CN: 一般情况下, 每周固定的休息日; 可用值: '1, 2, 3, 4, 5, 6, 7' 或 '"Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"';
    注意: 在使用"class calendar"创建对象时, 可以指定选项"weekends="覆盖本定义;

E.G.
- weekends = [6, 7]
- weekends = ["Sat", "Sun"]
- weekends = [5, 6, 7]
"""


yearRange = None
"""
EN: Control the generation range of year data; Available values: None, int, tuple; Default value: None;
    Note: When creating objects using "class calendar", you can specify the option "yearRange=" to override this definition;
    * None  : Only generate data for the current year;
    * Int   : Generate data for the specified year;
    * Tuple : Generate data within a specified year range;
CN: 控制年份数据的生成范围; 可用值: None, int, tuple; 默认值: None;
    注意: 在使用"class calendar"创建对象时, 可以指定选项"yearRange="覆盖本定义;
    * None  : 只生成当前年份的数据;
    * int   : 生成指定年份的数据;
    * tuple : 生成指定年份范围的数据;

E.G.
- yearRange = None
- yearRange = 2024
- yearRange = (2010, 2012)
"""


festivalsEveryYearRepeat = {
    "New Year": [("D", 1, 1)],
    "Labour Day": [("D", 5, 1)],
    "Mother's Day": [("W", 5, 2, 7)],
    "Thanksgiving": [("W", 11, 4, 4)],
}
"""
EN: Some festivals occur at fixed times each year according to specific rules. Defining relevant rules in this variable
    can avoid duplicate definitions of annual data in the "festivalsEveryYearDiff" variable; 
CN: 某些节日会按特定规则在每年的固定时间发生, 在本变量中定义相关规则, 可以避免在"festivalsEveryYearDiff"变量中每年数据的重复定义;

e.g.
- "New Year": [("D", 1, 1)]                     # EN: January 1st every year is definitely a new year;
- "New Year": [("D", "Jan", 1)]                 # CN: 每年的1月1日是必定是新的一年;
- "Mother's Day": [("W", 5, 2, 7)]              # EN: The second Sunday of May every year must be Mother's Day;
- "Mother's Day": [("W", "May", "2nd", "Sun")]  # CN: 每年5月的第2个的星期日必定为母亲节;
"""


festivalsEveryYearDiff = {
    2023:
    {
        "Spring Festival": [("D", 1, 22)],
        "Ching Ming Festival": [("D", 4, 5)]
    },
    2024:
    {
        "Spring Festival": [("D", 2, 10)],
        "Ching Ming Festival": [("D", 4, 4)]
    },
}
"""
EN: The occurrence cycle of certain festivals is not convenient to calculate, and these inconvenient festivals are explicitly
    defined in this variable; The rules in this variable, together with the rules in the "festivalsEveryYearRepeat" variable, 
    determine the festival information for that year;
CN: 某些节日发生周期并不方便计算, 这些不方便计算的节日, 显式地在本变量中定义; 本变量中的规则会与"festivalsEveryYearRepeat"变量
    中的规则, 共同决定出该年份的节日信息;

e.g.
- "Spring Festival": [("D", 1, 22)]             # EN: The Spring Festival date in China in 2023 is "January 22, 2023";
-                                               # CN: 中国2023年的春节日期是"2023-01-22";
- "Spring Festival": [("D", 2, 10)]             # EN: The Spring Festival date in China in 2024 is "February 10th, 2024";
-                                               # CN: 中国2024年的春节日期是"2024-02-10";
"""


holidaysEveryYearRepeat = {"XXX": [("D", 1, 2)]}
"""
EN: Similar to the use of "festivalsEveryYearRepeat"; The definition method is the same as "festivalsEveryYearRepeat";
CN: 类似"festivalsEveryYearRepeat"的用途; 定义方式同"festivalsEveryYearRepeat";
"""


holidaysEveryYearDiff = {
    2023:
    {
        "Spring Festival": [("D", 1, 21), ("D", 1, 22), ("D", 1, 23), ("D", 1, 24), ("D", 1, 25), ("D", 1, 26), ("D", 1, 27)],
        "Ching Ming Festival": [("D", 4, 5)],
        "Labour Day": [("D", 4, 29), ("D", 4, 30), ("D", 5, 1), ("D", 5, 2), ("D", 5, 3)]
    },
    2024:
    {
        "Spring Festival": [("D", 2, 10), ("D", 2, 11), ("D", 2, 12), ("D", 2, 13), ("D", 2, 14), ("D", 2, 15), ("D", 2, 16), ("D", 2, 17)],
        "Ching Ming Festival": [("D", 4, 4), ("D", 4, 5), ("D", 4, 6)],
        "Labour Day": [("D", 5, 1), ("D", 5, 2), ("D", 5, 3), ("D", 5, 4), ("D", 5, 5)]
    },
}
"""
EN: Holidays triggered by a certain holiday;
CN: 由于某个节日所引发的假期;

e.g.
- 2024:{"Labour Day": [("D", 5, 1), ("D", 5, 2), ("D", 5, 3), ("D", 5, 4), ("D", 5, 5)], ...}
- 2024:{"Labour Day": [("D", "May", 1), ("D", "May", 2), ("D", "May", 3), ("D", "May", 4), ("D", "May", 5)], ...}
"""


workdaysEveryYearRepeat = {"YYY": [("D", 1, 3)]}
"""
EN: Similar to the use of "festivalsEveryYearRepeat"; The definition method is the same as "festivalsEveryYearRepeat";
CN: 类似"festivalsEveryYearRepeat"的用途; 定义方式同"festivalsEveryYearRepeat";
"""


workdaysEveryYearDiff = {
    2023:
    {
        "Spring Festival": [("D", 1, 28), ("D", 1, 29)],
        "Ching Ming Festival": [],
        "Labour Day": [("D", 4, 23), ("D", 5, 6)]
    },
    2024:
    {
        "Spring Festival": [("D", 2, 4), ("D", 2, 18)],
        "Ching Ming Festival": [("D", 4, 7)],
        "Labour Day": [("D", 4, 28), ("D", 5, 11)]
    }
}
"""
EN: Workdays triggered by a certain holiday;
CN: 由于某个节日所引发的工作日;

e.g.
- 2024:{"Labour Day": [("D", 4, 28), ("D", 5, 11)], ...}
- 2024:{"Labour Day": [("D", "Apr", 28), ("D", "May", 11)], ...}
"""
