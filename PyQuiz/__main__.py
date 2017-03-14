import time
import random
import pygame
from dictionary import DJ
from texts import *
from Layout import Layout
pygame.init()

boolGameloop = True
strNaam = ""
intScore = 0
intRonde = 0

# functions go here
dj = DJ()

def intro():
    global boolGameloop
    print textBlank + Layout.bold + textIntro1 + "\n"

    def naamopgeven():
        global strNaam
        strNaam = raw_input(textIntro2 + Layout.blue) + Layout.end

    naamopgeven()

    if not strNaam:
        print Layout.red + textError1
        naamopgeven()
    print Layout.bold + textIntro3.format(strNaam) + Layout.end


def einde():
    print Layout.bold + textEinde1.format(strNaam, intScore)
    print textEinde2 + Layout.end
    print textEinde3


def startround():
    raw_input()

intro()
dj.randomizeArray()

while boolGameloop:
    # all the functions executed in their respective order
    dj.chooseListing()
    dj.chooseTrack()
    startround()
    intRonde += 1

    if intRonde == 10:
        boolGameloop = False

einde()

exit()
