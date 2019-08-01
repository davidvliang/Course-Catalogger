from CleanedProgram.lib.collect import *
from CleanedProgram.lib.webscraper import *
from CleanedProgram.lib.csver import *

# prompt user for input
print("Would you like to update database?", end='  ')
Response = input()
SubjectURLs = UpdateData(Response)
print(SubjectURLs)
print("Hello, what room would you like to know more about")
# a = input()
print("Well, that's too bad!")
rooms = GetRoom(SubjectURLs[1])
times = GetTime(SubjectURLs[1])
days = GetDay(SubjectURLs[1])
print(rooms, times, days)
print("here?")
a = SortData(rooms, times, days)
