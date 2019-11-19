import smtplib
import ssl


# Email must be a gmail account for this email generator.
# You will have to create a password security token instead of your actual password.
# Lastly you will need the number of receivers.


class Email:
    def __init__(self, Gmail, Password, NumofRecipients, Message):
        self.amount = NumofRecipients
        self.message = Message
        self.recipients = []
        self.sender = Gmail
        self.passW = Password
        self.context = ssl.create_default_context()
        self.server = smtplib.SMTP('smtp.gmail.com', 25)

    def connect(self):
        self.server.connect("smtp.gmail.com", 25)
        self.server.ehlo()
        self.server.starttls(context=self.context)
        self.server.ehlo()
        self.server.login(self.sender, self.passW)

    def input_receivers(self):
        n = 0
        while n != int(self.amount):
            recs = input('Enter receiver email address: ')
            self.recipients.append(recs)
            n += 1

    def recipient(self, recipient):
        self.recipients.append(recipient)


    def sending(self, message):
        n = 0
        while n != len(self.recipients):
            if n == len(self.recipients):
                self.server.sendmail(self.sender, self.recipients[n], message)
                print("The message has been successfully sent to ", self.recipients[n],
                      '\n all messages have been successfully sent!')
            else:
                self.server.sendmail(self.sender, self.recipients[n], message)
                print("The message has been successfully sent to ", self.recipients[n])
                n += 1
    
    def SendMessages(self):
        Send = Email(self.sender, self.passW, len(self.recipients))
        Send.connect()
        Send.input_recievers()
        Send.sending(message=self.message)

        
# Send = Email(your email, your token/pass, # of recipients, Message)
# Send.SendMessages()
