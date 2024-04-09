# -*- coding: UTF-8 -*-
from . import calerror
import importlib.util
import datetime
import os


_monthTag = {"Jan": 1, "Feb": 2, "Mar": 3, "Apr": 4, "May": 5, "Jun": 6, "Jul": 7, "Aug": 8, "Sep": 9, "Oct": 10, "Nov": 11, "Dec": 12}
_weekTag = {"Mon": 1, "Tue": 2, "Wed": 3, "Thu": 4, "Fri": 5, "Sat": 6, "Sun": 7}
_cycleTag = {"1st": 1, "2nd": 2, "3th": 3, "4th": 4, "5th": 5}
_allTag = {**_monthTag, **_weekTag, **_cycleTag}


def _checkSupportCountry():
    spctr = {}
    ctrpm = {}
    libPath = os.path.dirname(os.path.abspath(__file__))
    for mainland in os.listdir(libPath):
        mainlandPath = os.path.join(libPath, mainland)
        if os.path.isdir(mainlandPath) and not mainland.startswith("_"):
            spctr[mainland] = []
            for cn in os.listdir(mainlandPath):
                ctrPath = os.path.join(libPath, mainland, cn)
                if os.path.isfile(ctrPath) and cn.endswith(".py") and not cn.startswith("_"):
                    ctrName, _ = os.path.splitext(cn)
                    ctrpm[ctrName] = ctrPath
                    spctr[mainland].append(ctrName)
    return spctr, ctrpm


supportCountry, countryFilePath = _checkSupportCountry()


class calendar:
    """
    EN: Create the class instance.
    CN: 日历类；

    E.G.
    - Example = calcore.calendar(country="china")
    - Example = calcore.calendar(country="example", weekends=["Sat", "Sun"])
    - Example = calcore.calendar(country="example", weekends=[1, 2, 3])
    - Example = calcore.calendar(country="example", UTCMode=[True, 8])
    - Example = calcore.calendar(country="example", yearRange=(2010, 2015))
    - Example = calcore.calendar(extMode=True, extFileName="example.py", extFilePath="example.py")
    - Example = calcore.calendar(extMode=True, extFileName="example.py", extFilePath="h:\\example.py")

    Args (**args: ):
        extMode (bool):
            EN: Whether to enable extended mode, default to "False"; After enabling this mode, it is allowed
                to manually specify the "data file" to be imported, and both "extFileName" and "extFilePath"
                need to be defined at the same time;
            CN: 是否启用扩展模式, 默认"False"; 启用本模式后, 允许手动指定要导入的"数据文件", 需要同时定义
                "extFileName"与"extFilePath";

        extFileName (str):
            EN: The name of the external file; Only valid when "extMode = True";
            CN: 外部文件的名称; 仅在"extMode = True"时有效;

        extFilePath (str):
            EN: The path of external files; Only valid when "extMode = True";
            CN: 外部文件的路径; 仅在"extMode = True"时有效;

        country (str):
            EN: The name of the country. This definition is meaningless when "extMode = True";
            CN: 国家名称; 在"extMode = True"时此定义无意义;

        yearRange ([None, int ,tuple(int, int)]):
            EN: Control the generation range of year data; Default value: None;
                Note: When create "class calendar", you can use "yearRange=" to override this definition;
                -- None  : Only generate data for the current year;
                -- Int   : Generate data for the specified year;
                -- Tuple : Generate data within a specified year range;
            CN: 控制年份数据的生成范围; 可用值: None, int, tuple; 默认值: None;
                注意: 在使用"class calendar"创建对象时, 可以指定选项"yearRange="覆盖本定义;
                -- None  : 只生成当前年份的数据;
                -- int   : 生成指定年份的数据;
                -- tuple : 生成指定年份范围的数据;

        UTCMode (lsit[bool, int]):
            EN: Whether to use UTC mode; Disabled by default [using local time obtained from the system];
                When UTC mode is enabled ["True"], the calculation of the current date will be based on UTC time
                plus an offset value; This mainly affects how to calculate today's date in the program;
                Default value "[False, 0]";
                Note: When create "class calendar", you can use "UTCMode=" to override this definition;
                Note: For countries using daylight saving time, it is not recommended to enable this mode;
            CN: 是否使用UTC模式; 默认不启用[使用系统中获取的本地时间]; 启用UTC模式时["True"], 当前日期的计算会以UTC时间
                加上偏移值; 这主要影响程序中, 如何计算今天的日期; 默认值"[False, 0]";
                注意: 在使用"class calendar"创建对象时, 可以指定选项"UTCMode="覆盖本定义;
                注意: 使用夏令时的国家, 不建议启用此模式;

        weekends (list[int]):
            EN: Definition of weekends [rest days]; Default value is "[6,7]";
                Note: When create "class calendar", you can use "weekends=" to override this definition;
            CN: 周末定义[休息日]; 默认值: "[6, 7]";
                注意: 在使用"class calendar"创建对象时, 可以指定选项"weekends="覆盖本定义;

    Attributes:
        festivalsData (dict[int, dict[str, list[str]]]):
            EN: Festivals data; Can be modified in real-time and affect the calculation results of the program;
            CN: 节日数据;

        holidaysData (dict[int, list[str]]):
            EN: Holidays data; Can be modified in real-time and affect the calculation results of the program;
            CN: 假日数据;

        workdaysData (dict[int, list[str]]):
            EN: Workdays data;
            CN: 工作日数据; Can be modified in real-time and affect the calculation results of the program;

        anniversariesData (dict[str, str]):
            EN: Anniversaries data; Can be modified in real-time and affect the calculation results of the program;
            CN: 纪念日数据;

        UTCMode (lsit[bool, int]):
            EN: UTC mode; Can be modified in real-time and affect the calculation results of the program;
            CN: UTC模式; 可以实时修改并影响程序的计算结果;

        weekends (list[int]):
            EN: Definition of weekends; Can be modified in real-time and affect the calculation results of the program;
            CN: 周末定义[休息日]; 可以实时修改并影响程序的计算结果;
    """

    def _calcToday(self) -> datetime.date:
        if self.UTCMode[0]:
            today = (datetime.datetime.now(datetime.timezone.utc) + datetime.timedelta(hours=self.UTCMode[1])).date()
        else:
            today = datetime.datetime.today().date()
        return today

    def _listCompress(self, ls) -> list:
        newls = []
        for x in ls:
            if x not in newls:
                newls.append(x)
        return newls

    def _toInt(self, param) -> int:
        if isinstance(param, int):
            return param
        elif isinstance(param, str):
            return _allTag[param]

    def _calcDate(self, year, datelist) -> list:
        datels = []
        for daterule in datelist:
            if daterule[0] == "D" or daterule[0] == "d":
                date = "{}-{}-{}".format(str(year), str(self._toInt(daterule[1])).zfill(2), str(daterule[2]).zfill(2))

                datels.append(date)
            elif daterule[0] == "W" or daterule[0] == "w":
                month_1st = datetime.date(year, self._toInt(daterule[1]), 1)
                datetmp = month_1st + datetime.timedelta(days=((self._toInt(daterule[3]) - month_1st.isoweekday()) % 7))
                date = datetmp + datetime.timedelta(weeks=self._toInt(daterule[2]) - 1)
                datels.append(date.strftime("%Y-%m-%d"))
            else:
                raise calerror.WrongCalcMethod
        return datels

    def _calendarScope(self, sc) -> list:
        if sc is None or isinstance(sc, int):
            calS = [self._calcToday().year]
        elif isinstance(sc, tuple) and sc[0] < sc[1]:
            calS = list(range(sc[0], sc[1] + 1))
        else:
            raise ValueError("'yearRange' parameter error.")
        return calS

    def _genFestivalsData(self, data):
        if len(data) == 0:
            return
        for year, datadict in data.items():
            if year not in self.festivalsData:
                continue
            for name, datelist in datadict.items():
                self.festivalsData[year][name] = self._listCompress(self._calcDate(year, datelist))

    def _addFestivalsEveryYearRepeat(self, data):
        if len(data) == 0:
            return
        for year in self.festivalsData:
            for name, datelist in data.items():
                if name in self.festivalsData[year]:
                    self.festivalsData[year][name] += self._calcDate(year, datelist)
                    self.festivalsData[year][name] = self._listCompress(self.festivalsData[year][name])
                else:
                    self.festivalsData[year][name] = self._calcDate(year, datelist)
                    self.festivalsData[year][name] = self._listCompress(self.festivalsData[year][name])

    def _genHolidaysData(self, data):
        if len(data) == 0:
            return
        for year, datadict in data.items():
            if year not in self.holidaysData:
                continue
            for datelist in datadict.values():
                self.holidaysData[year] += self._calcDate(year, datelist)
            self.holidaysData[year] = self._listCompress(self.holidaysData[year])

    def _addHolidaysEveryYearRepeat(self, data):
        if len(data) == 0:
            return
        for year in self.holidaysData:
            for datelist in data.values():
                self.holidaysData[year] += self._calcDate(year, datelist)
            self.holidaysData[year] = self._listCompress(self.holidaysData[year])

    def _genWorkdaysData(self, data):
        if len(data) == 0:
            return
        for year, datadict in data.items():
            if year not in self.workdaysData:
                continue
            for datelist in datadict.values():
                self.workdaysData[year] += self._calcDate(year, datelist)
            self.workdaysData[year] = self._listCompress(self.workdaysData[year])

    def _addWorkdaysEveryYearRepeat(self, data):
        if len(data) == 0:
            return
        for year in self.workdaysData:
            for datelist in data.values():
                self.workdaysData[year] += self._calcDate(year, datelist)
            self.workdaysData[year] = self._listCompress(self.workdaysData[year])

    def isWorkday(self, date=None) -> bool:
        if date is None:
            date = self._calcToday()
        datestr = date.strftime("%Y-%m-%d")
        if date.year in self.workdaysData:
            if datestr in self.workdaysData[date.year]:
                return True
        if date.year in self.holidaysData:
            if datestr in self.holidaysData[date.year]:
                return False
        if date.isoweekday() in self.weekends:
            return False
        else:
            return True

    def isHoliday(self, date=None) -> bool:
        if date is None:
            date = self._calcToday()
        result = self.isWorkday(date)
        return not result

    def setAnniversaries(self, data):
        self.anniversariesData = data

    def addAnniToFest(self):
        for name, datestr in self.anniversariesData.items():
            d = datetime.datetime.strptime(datestr, "%Y-%m-%d")
            for year, datadict in self.festivalsData.items():
                if year >= d.year:
                    adddate = datetime.date(year, d.month, d.day).strftime("%Y-%m-%d")
                    if name in datadict:
                        self.festivalsData[year][name].append(adddate)
                    else:
                        self.festivalsData[year][name] = [adddate]

    def isAnniversarie(self, date=None) -> bool:
        if date is None:
            date = self._calcToday()
        for datestr in self.anniversariesData.values():
            d = datetime.datetime.strptime(datestr, "%Y-%m-%d")
            if date.year >= d.year and date.month == d.month and date.day == d.day:
                return True
        return False

    def getFestivalsByYear(self, year=None) -> list:
        result = []
        if year is None:
            year = self._calcToday().year
        if year in self.festivalsData:
            for festival in self.festivalsData[year].keys():
                result.append(festival)
        return result

    def getFestivalsByDay(self, date=None) -> list:
        result = []
        if date is None:
            date = self._calcToday()
        datestr = date.strftime("%Y-%m-%d")
        if date.year in self.festivalsData:
            for name, ls in self.festivalsData[date.year].items():
                for x in ls:
                    if x == datestr:
                        result.append(name)
        return result

    def cfgInfo(self):
        print("========== Config Info ==========")
        print("- extMode      =", self._extMode[0])
        print("- extFileName  =", self._extFileName[0])
        print("- extFilePath  =", self._extFilePath[0])
        print("- country      =", self._country[0])
        print("- yearRange    =", self._yearRange[0])
        print("+ UTCMode      =", self.UTCMode)
        print("+ weekends     =", self.weekends)
        print("=================================")

    def __init__(self, **args):
        self._extMode = (args.get("extMode", False),)
        self._extFileName = (args.get("extFileName", None),)
        self._extFilePath = (args.get("extFilePath", None),)
        self._country = (None if self._extMode[0] else args.get("country", None),)

        if self._extMode[0]:
            execrule = importlib.util.spec_from_file_location(self._extFileName[0], self._extFilePath[0])
        elif self._country[0] not in countryFilePath:
            raise calerror.UnSupportCountry
        else:
            execrule = importlib.util.spec_from_file_location(self._country[0], countryFilePath[self._country[0]])
        mod = importlib.util.module_from_spec(execrule)
        execrule.loader.exec_module(mod)

        self.UTCMode = args.get("UTCMode", getattr(mod, 'UTCMode', [False, 0]))
        self.weekends = args.get("weekends", getattr(mod, 'weekends', [6, 7]))
        self._yearRange = (args.get("yearRange", getattr(mod, 'yearRange', None)),)

        self.festivalsData = {}
        self.holidaysData = {}
        self.workdaysData = {}
        self.anniversariesData = {}
        for value in self._calendarScope(self._yearRange[0]):
            self.festivalsData[value] = {}
            self.holidaysData[value] = []
            self.workdaysData[value] = []

        for index, value in enumerate(self.weekends):
            self.weekends[index] = self._toInt(value)

        if hasattr(mod, 'festivalsEveryYearDiff'):
            self._genFestivalsData(mod.festivalsEveryYearDiff)
        if hasattr(mod, 'festivalsEveryYearRepeat'):
            self._addFestivalsEveryYearRepeat(mod.festivalsEveryYearRepeat)

        if hasattr(mod, 'holidaysEveryYearDiff'):
            self._genHolidaysData(mod.holidaysEveryYearDiff)
        if hasattr(mod, 'holidaysEveryYearRepeat'):
            self._addHolidaysEveryYearRepeat(mod.holidaysEveryYearRepeat)

        if hasattr(mod, 'workdaysEveryYearDiff'):
            self._genWorkdaysData(mod.workdaysEveryYearDiff)
        if hasattr(mod, 'workdaysEveryYearRepeat'):
            self._addWorkdaysEveryYearRepeat(mod.workdaysEveryYearRepeat)

        self.cfgInfo()


if __name__ == "__main__":
    pass
