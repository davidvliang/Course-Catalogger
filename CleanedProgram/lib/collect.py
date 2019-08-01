from bs4 import BeautifulSoup as soup
from requests import get
from CleanedProgram.lib.csver import urlmaker, urlreader

'''
function UpdateData
* given response from user (y/n), will update SubjectURLs
@params userinput (y/n)
@return list of subject urls
'''


def UpdateData(userinput):
    # URLs
    BaseURL = "https://www.sis.hawaii.edu/uhdad"
    BaseExtension = "/avail.classes?i=MAN&t=202010"

    if userinput == 'y':
        AllSubjects = soup(get(BaseURL + BaseExtension).content, 'html.parser')
        AllLinks = AllSubjects.find_all('a', href=True)

        SubjectURLs = []
        for Link in AllLinks:
            if "/avail.classes?i=MAN&t=202010&s=" in Link['href'][1:]:
                SubjectURLs.append(BaseURL + Link['href'][1:])
        # SubjectURLs = list(set(SubjectURLs))
        SubjectURLs = list(dict.fromkeys(SubjectURLs))

        # print("debug SubjectURLs", len(SubjectURLs))
        urlmaker(SubjectURLs)
    else:
        SubjectURLs = urlreader()


        # SubjectTLAs = []
        # for Link in SubjectURLs:
        #     SubjectTLAs.append(Link.partition('&s=')[2])
        # # print("debug SubjectTLAs", len(SubjectTLAs))

    return SubjectURLs