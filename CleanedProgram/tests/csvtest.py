from CleanedProgram.lib.webscraper import *
from CleanedProgram.lib.csver import *

# import csv

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






