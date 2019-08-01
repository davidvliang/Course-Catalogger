from requests import get
from bs4 import BeautifulSoup as soup
import re

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
