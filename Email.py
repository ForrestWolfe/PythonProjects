import smtplib
import ssl


# Email must be a gmail account for this email generator.
# You will have to create a password security token instead of your actual password.
# Lastly you will need the number of receivers.


class Email:
    def __init__(self, Gmail, Password, numOfRecs):
        self.amount = numOfRecs
        self.receivers = []
        self.sender = Gmail
        self.passW = Password
        self.context = ssl.create_default_context()
        self.server = smtplib.SMTP('smtp.gmail.com', 25)

    def conneckt(self):
        self.server.connect("smtp.gmail.com", 25)
        self.server.ehlo()
        self.server.starttls(context=self.context)
        self.server.ehlo()
        self.server.login(self.sender, self.passW)

    def list_recievers(self):
        n = 0
        while n != int(self.amount):
            recs = input('Enter receiver email address: ')
            self.receivers.append(recs)
            n += 1

    def sending(self, message):
        n = 0
        while n != len(self.receivers):
            if n == len(self.receivers):
                self.server.sendmail(self.sender, self.receivers[n], message)
                print("The message has been successfully sent to ", self.receivers[n],
                      '\n all messages have been successfully sent!')
            else:
                self.server.sendmail(self.sender, self.receivers[n], message)
                print("The message has been successfully sent to ", self.receivers[n])
                n += 1


Send = Email(Gmail="YourEmailAccount", Password="YourToken/Password", numOfRecs='NumberOfReceivers')
Send.conneckt()
Send.list_recievers()
Send.sending(message='Your message')
# Send.sending()
