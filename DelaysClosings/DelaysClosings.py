from lxml import html
import requests
from datetime import datetime
from Email import Email
import re


# TODO: Add more News URLS to scrape


class ClosingsDelays:
    def __init__(self):
        self.URL = ['https://www.nbc4i.com/weather/closings/']  # defining the URL
        self.schools_affected_colored = ''  # just a fancy dispay for text
        self.schools_affected = ''  # lists all the schools containing keywords
        date = datetime.now()
        date = str(date)
        self.date = date[:9]  # just the date
        self.nbc = ('\033[3;39;41m' + self.date + '\t\tNBC4 SCHOOL CLOSINGS AND DELAYS')  # just a title for looks

    """Do not use spaces in keywords, and capitalize the keywords first letter"""

    def nbc4(self, keyword, keyword2):
        ClosedOrDelay = {}  # dictionary in this format {SchoolName: closed}
        page = requests.get(self.URL[0])  # gets the first url from the list
        tree = html.fromstring(page.content)  # grabs the page content
        schools = tree.xpath('//h3[@class="closing__title"]/text()')  # grabbing text of <h3 class="closing_title">
        closings = tree.xpath('//div[@class="closing__status"]/text()')  # grabbing text of <div class="closing_status">
        for school in schools:  # schools is a list this for loop iterates through that list
            school = str(school)  # transform list item to string if its already not one
            school = re.sub('\s+', '', school)  # regex to remove tabs, newlines, and spaces
            for closing in closings:  # sifting through closings list
                closing = str(closing)  # transforming list item to string if its already not one
                closing = re.sub("\s+", '', closing)  # regex to remove tabs, newlines, and spaces
                ClosedOrDelay[school] = closing  # adding SchoolName to dictionary with its value (delay or closed)
        for key in ClosedOrDelay.keys():  # sifting through the keys in the dictionary
            if key.__contains__(keyword) or key.__contains__(keyword2):  # if any of the keys match keywords
                self.schools_affected_colored += (
                            "\033[1;32;40m\t\t\t" + key + " : \t"  # add to colored string to be printed out
                            + "\033[1;35;40m" + ClosedOrDelay.get(key) + '\n')
                self.schools_affected += key + " " + ClosedOrDelay.get(key) + '\n'  # add to string to be emailed
        print(self.nbc)  # printing the title defined in init
        print(self.schools_affected_colored)  # printing out the schools effected in color

    """ Enter your gmail account, your password or generated token,
        only enter 1 for num and enter recipient address"""

    def send_message(self, gmail, token, num, recipient):
        if len(self.schools_affected) != 0:  # if self.schools_affected strings length is not equal to zero
            sub = 'School Closings & Delays'  # This is the subject of the email
            Send = Email(gmail, token, num)  # defining the Send object
            Send.connect()  # Connecting to the gmail account
            Send.recipient(recipient)  # appends the recipient name to the list of recipients to send to on email.py
            Send.sending(message="Subject: {}\n\n {}".format(sub,
                                                             self.schools_affected))  # Sends the subject and list of schools infected to recipient email
        else:  # If the length of the string schools affected is zero
            # print no delays or closings today
            print(self.date, " No delays or closings today")


#closed = ClosingsDelays()
#closed.nbc4('south', 'South')
#closed.send_message(Gmail, token, 1, recipient)
