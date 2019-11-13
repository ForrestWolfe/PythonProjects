import tkinter as tk
import time
from pygame import mixer


class Pymer:
    def __init__(self, hrs, mins, secs):
        self.hrs = hrs
        self.mins = mins
        self.secs = secs
        if int(self.hrs) < 0 or int(
                self.hrs) <= 9:  # if hours less than 0 or less than or equal to 9 hrs cant go negative and I like the format 00:00:00 better
            self.hrs = str('0' + str(self.hrs))  # makes self.hrs = 00
        if int(
                self.mins) >= 60:  # if mins >= 60 add 1 hour and if mins more than 60 minus 60 from minutes to get new minutes variable
            self.hrs += 1
            self.mins = self.mins - 60
        if len(str(self.mins)) == 1:  # if mins is single digits, insert a zero before mins
            self.mins = str('0' + str(self.mins))
        if int(
                self.secs) > 59:  # if seconds greater than 59 add 1 minute and if its more than 60 minus 60 from seconds to get new seconds variable
            self.mins = int(self.mins) + 1
            self.secs = self.secs - 60
        if len(str(
                self.secs)) == 1:  # if the length of the str(secs) is equal to 1 make sure the secs variable has a 0 before it
            self.secs = str('0' + str(self.secs))
        self.Timer = "{}:{}:{}".format(str(self.hrs), str(self.mins),
                                       str(self.secs))  # The format that the information is displayed in

    # Countdown is the Tkinter part of the project that displays the timer

    def countdown(self):
        global root  # root must be global because it is accessed outside of the class
        root = tk.Tk()
        label_font = ('helvetica', 40)  # font and size of the font
        lbl = tk.Label(font=label_font)  # creating the label of the font in tkinter
        lbl.pack(fill='both', expand=1)
        lbl.config(bg='red')  # setting the background color to red
        while self.Timer != "{}:{}:{}".format('00', '00',
                                              '00'):  # while self.timer is not equal to 00:00:00 continue to print the timer
            time.sleep(1)  # sleep function is used to update the timer
            root.update()  # makes the popup dynamic basically
            self.secs = int(self.secs) - 1  # counting down by 1 second at a time
            if int(self.hrs) <= 9 and len(
                    str(self.hrs)) == 1:  # if hours >= 9 and length of hours = 1 make hours 0 + hrs 01 or 02 for ex.
                self.hrs = str('0' + str(self.hrs))
            if int(self.mins) < 0:  # if mins less than 0, minus 1 hour and make mins equal to 59
                self.hrs = int(self.hrs) - 1
                self.mins = 59
            if len(str(self.mins)) == 1:  # if mins is equal to single digit insert a zero in front of it
                self.mins = str('0' + str(self.mins))
            if int(self.secs) < 0:  # if secs less than 0 change secs to 59 and minus 1 minute
                self.secs = 59
                self.mins = int(self.mins) - 1
            if len(str(self.secs)) == 1:  # if length of seconds is 1 digit insert a zero in front of seconds
                self.secs = str('0' + str(self.secs))
            # Formatting hours, minutes and seconds
            self.Timer = "{}:{}:{}".format(str(self.hrs), str(self.mins), str(self.secs))
            lbl["text"] = self.Timer  # displays the timer countdown

    @staticmethod
    def play_sound():
        for i in range(5):
            time.sleep(5)  # this sleep allows the alarm to go off five times without it it will only go off 1 time
            mixer.init()  # initiates pygames mixer
            mixer.music.load('c:/Windows/Media/Alarm01.wav')  # loads the alarm sound
            mixer.music.play()  # plays the alarm


def start_timer(hour, minute, seconds):
    pyme = Pymer(hour, minute, seconds)
    pyme.countdown()
    pyme.play_sound()
    root.mainloop()


start_timer(0, 0, 5)
