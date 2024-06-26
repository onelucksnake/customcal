# -*- coding: UTF-8 -*-
import datetime
from customcal import calcore

print("--")
print("--")
print("--")

# print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
# print("calcore.supportCountry  =", calcore.supportCountry)
# print("calcore.countryFilePath =", calcore.countryFilePath)
# print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")

# Example = calcore.calendar(country="china")
# Example = calcore.calendar(country="chinaExt", yearRange=2024)
# Example = calcore.calendar(country="empty")
Example = calcore.calendar(country="example")
# Example = calcore.calendar(country="usefunc")
# Example = calcore.calendar(country="example", weekends=["Sat", "Sun"])
# Example = calcore.calendar(country="example", weekends=[1, 2, 3])
# Example = calcore.calendar(country="example", UTCMode=[True, 8])
# Example = calcore.calendar(country="example", yearRange=(2010, 2015))
# Example = calcore.calendar(extMode=True, extFileName="example.py", extFilePath="example.py")
# Example = calcore.calendar(extMode=True, extFileName="example.py", extFilePath="h:\\example.py")

print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
print(".festivalsData\n", Example.festivalsData)
print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
print(".holidaysData\n", Example.holidaysData)
print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
print(".workdaysData\n", Example.workdaysData)
print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
print(".anniversariesData\n", Example.anniversariesData)
print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
print(".isWorkday()  Today >>> =", Example.isWorkday())
print(".isHoliday()  Today >>> =", Example.isHoliday())
print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
print(".isWorkday(?) Mon   >>> =", Example.isWorkday(datetime.date(2024, 7, 1)))
print(".isWorkday(?) Tue   >>> =", Example.isWorkday(datetime.date(2024, 7, 2)))
print(".isWorkday(?) Wed   >>> =", Example.isWorkday(datetime.date(2024, 7, 3)))
print(".isWorkday(?) Thu   >>> =", Example.isWorkday(datetime.date(2024, 7, 4)))
print(".isWorkday(?) Fri   >>> =", Example.isWorkday(datetime.date(2024, 7, 5)))
print(".isWorkday(?) Sat   >>> =", Example.isWorkday(datetime.date(2024, 7, 6)))
print(".isWorkday(?) Sun   >>> =", Example.isWorkday(datetime.date(2024, 7, 7)))
print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
print(".getFestivalsByYear()  ThisYear\n", Example.getFestivalsByYear())
print(".getFestivalsByDay(datetime.date(2024, 5, 1))\nReturn List =", Example.getFestivalsByDay(datetime.date(2024, 5, 1)))
print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
print("Before .setAnniversaries() --> .anniversariesData\n", Example.anniversariesData)
Example.setAnniversaries({"Wedding Anniversary": "2020-12-18", "Son's Birthday": "2024-10-18"})
print("After  .setAnniversaries() --> .anniversariesData\n", Example.anniversariesData)
print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
print(".isAnniversarie(datetime.date())            \n>>> True/False =", Example.isAnniversarie())
print(".isAnniversarie(datetime.date(2024, 12, 10))\n>>> False      =", Example.isAnniversarie(datetime.date(2024, 12, 10)))
print(".isAnniversarie(datetime.date(2024, 10, 18))\n>>> True       =", Example.isAnniversarie(datetime.date(2024, 10, 18)))
print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
print("Before .addAnniToFest() --> .festivalsData\n", Example.festivalsData)
Example.addAnniToFest()
print("After  .addAnniToFest() --> .festivalsData\n", Example.festivalsData)
print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
