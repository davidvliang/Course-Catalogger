from CleanedProgram.lib.webscraper import *
# from .csver import *

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


# print("debug GetRoom")
# n = 1
# count = 1
# print("fetching URL from ", SubjectTLAs[n])
# for r in GetRoom(SubjectURLs[n]):
#   print(count, end=' ')
#   print(r)
#   count += 1

# print("debug GetTime")
# n = 1
# count = 1
# print("fetching URL from ", SubjectTLAs[n])
# tol = GetTime(SubjectURLs[n])
# for t in range(len(tol)):
#   print(t, end=' ')
#   print(tol[t])
# print(len(tol))

#
# print("debug GetDay")
# n = 1
# print("fetching URL from ", SubjectTLAs[n])
# Days = GetDay(SubjectURLs[n])
# print(len(Days))
#

print("DEBUG TIME!!")
count = 1
n = 151
print("fetching URL from ", SubjectTLAs[n])
for r,t,d in zip(GetRoom(SubjectURLs[n]),GetTime(SubjectURLs[n]), GetDay(SubjectURLs[n])):
  print(count, end='\t')
  print(r + '\t\t' + t + '\t\t' + d)
  count+= 1
