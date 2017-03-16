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
    print textBlank
    print Layout.bold + textEinde1.format(strNaam, intScore)
    print textEinde2 + Layout.end
    print textEinde3


def startround():
    print textBlank
    print Layout.bold + textRonde1.format(intRonde)
    dj.chooseListing()
    dj.chooseTrack()
    dj.trackChosen.playsong()

    def internalround():
        global intScore
        print textRonde2
        for i in xrange(4):
            print  "{0} - ".format(i) + dj.arrayChosen[i].name
        answer = raw_input(textRonde3 + Layout.end)
        if answer == dj.trackchosenIndex:
            dj.soundCorrect.playsong()
            print Layout.bold + Layout.green + textRonde5 + Layout.end
            print Layout.bold + textRonde6 + Layout.end
            intScore += 1
            raw_input(textEnter)
        elif answer is int[1:4]:
            dj.soundIncorrect.playsong()
            print Layout.bold + Layout.red + textRonde4.format(dj.trackChosen.name) + Layout.end
            raw_input(textEnter)
        else:
            print Layout.bold + Layout.red + textError2 + Layout.end
            raw_input(textEnter)
            internalround()
    internalround()


intro()
dj.randomizeArray()

while boolGameloop:
    # all the functions executed in their respective order
    startround()
    intRonde += 1
    if intRonde == 10:
        boolGameloop = False

einde()

exit()
