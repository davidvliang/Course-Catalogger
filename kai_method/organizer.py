from requests import get
from bs4 import BeautifulSoup as soup
import re

import csv

print("DEBUG organizer.py")

# URLs
BaseURL = "https://www.sis.hawaii.edu/uhdad"
BaseExtension = "/avail.classes?i=MAN&t=202010"

AllSubjects = soup(get(BaseURL+BaseExtension).content, 'html.parser')
AllLinks = AllSubjects.find_all('a', href=True)

SubjectURLs = []
for Link in AllLinks:
  if "/avail.classes?i=MAN&t=202010&s=" in Link['href'][1:]:
    SubjectURLs.append(BaseURL+Link['href'][1:])
# SubjectURLs = list(set(SubjectURLs))
SubjectURLs = list(dict.fromkeys(SubjectURLs))

# print("debug SubjectURLs", len(SubjectURLs))

SubjectTLAs = []
for Link in SubjectURLs:
    SubjectTLAs.append(Link.partition('&s=')[2])
# print("debug SubjectTLAs", len(SubjectTLAs))


"""
function GetRoom
* retrieve room information from url
@params: str SubjectURL
@return: list ClassRooms
"""
def GetRoom( SubjectURL ):
  PageContents = soup(get(SubjectURL).content, 'html.parser')
  RoomNumbers = PageContents.find_all('span', title=re.compile("Room"))
  ClassRooms = []

  for Index, Room in zip(range(len(RoomNumbers)), RoomNumbers):
    ClassRooms.append(Room.get_text())

  return ClassRooms

# print("debug GetRoom")
# n = 1
# count = 1
# print("fetching URL from ", SubjectTLAs[n])
# for r in GetRoom(SubjectURLs[n]):
#   print(count, end=' ')
#   print(r)
#   count += 1

"""
function GetTime
* retrieve time slot information from url
@params: str SubjectURL
@return: list TimeSlot
"""
def GetTime( SubjectURL ):
  PageContents = soup(get(SubjectURL).content, 'html.parser')
  TimeInfo = PageContents.find_all('td', {'class': 'default'})
  TimeSlots = []

  for Time in TimeInfo:
    if bool(re.search("\d\d\d\d-\d\d\d\d[a-z]", Time.get_text())):
      TimeSlots.append(Time.get_text())
  return TimeSlots

# print("debug GetTime")
# n = 1
# count = 1
# print("fetching URL from ", SubjectTLAs[n])
# tol = GetTime(SubjectURLs[n])
# for t in range(len(tol)):
#   print(t, end=' ')
#   print(tol[t])
# print(len(tol))


"""
function GetDay
* retrieve days information from url
@parms: str SubjectURL
@return: list Days
"""
def GetDay( SubjectURL ):
  PageContents = soup(get(SubjectURL).content, 'html.parser')
  ClassChunk = PageContents.find('table').find_all('tr')
  BetterChunk = []
  Days = []
  for tr in range(0, len(ClassChunk)):
    TdArr = []
    for td in ClassChunk[tr].find_all('td', {'class': 'default'}):
      TdArr.append(td.get_text())
    BetterChunk.append(TdArr)
  for i in BetterChunk[1:]:
    if i[-4] != 'TBA':
     Days.append(i[-4])
  return Days
#
# print("debug GetDay")
# n = 1
# print("fetching URL from ", SubjectTLAs[n])
# Days = GetDay(SubjectURLs[n])
# print(len(Days))
#

# print("DEBUG TIME!!")
# count = 1
# n = 151
# print("fetching URL from ", SubjectTLAs[n])
# for r,t,d in zip(GetRoom(SubjectURLs[n]),GetTime(SubjectURLs[n]), GetDay(SubjectURLs[n])):
#   print(count, end='\t')
#   print(r + '\t\t' + t + '\t\t' + d)
#   count+= 1


'''
function ClassroomInfo
* Given Classroom, determine time and days open
@parms: str RoomName
@return: 
'''
