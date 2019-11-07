import time
from random import randrange


def color_changer(change=True):
    x = randrange(10, 60)
    colors = ["\033[1;33;47m Hello I can change color (: ",
              "\033[0;34;47m Hello I can change color (:",
              "\033[0;31;47m Hello I can change color (:",
              "\033[0;32;47m Hello I can change color (:",
              "\033[0;35;47m Hello I can change color (:",
              "\033[0;36;47m Hello I can change color (:",
              "\033[0;39;47m Hello I can change color (:"]
    while change:
        for color in colors:
            time.sleep(1)
            print(color * x)


color_changer()
