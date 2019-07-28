from requests import get
from bs4 import BeautifulSoup as soup
from string import ascii_uppercase
import re

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
print("debug SubjectTLAs", len(SubjectTLAs))


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


print("debug GetRoom")
n = 160
print("fetching URL from ", SubjectTLAs[n])
for r in GetRoom(SubjectURLs[n]):
    if re.search("[0-9]", r):
        print(r)