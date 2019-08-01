import csv

'''
function SortData
* Given Classroom, determine time and days open
@parms: str RoomName
@return: 
'''
def SortData(Room, Time, Day):
    with open("bigdata.csv", "w") as bigfile:
        employee_writer = csv.writer(bigfile)

        employee_writer.writerow(Room)

    return 1

def urlmaker(urls):
    with open("subjecturls", 'w') as urlfile:
        url_writer = csv.writer(urlfile)
        url_writer.writerow(urls)

    return 1

def urlreader():
    with open ('subjecturls', 'r') as urlfile:
        url_reader = csv.reader(urlfile)
        savedlist = list(url_reader)
    return savedlist