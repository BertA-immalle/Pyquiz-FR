import random
from Track import Track
import pygame
pygame.init()

class DJ:
    # put song variables here in this format: trackName = Track("string of song to be displayed", 'music/filename.ogg')
    trackRickAstleyNever = Track("Never gonna give you up", 'music/rick.ogg')
    trackShootingStars = Track("Shooting Stars", 'music/shoot.ogg')
    trackBanksGeminiFeed = Track("Gemini Feed", 'music/banks.ogg')
    trackChrisRayGun = Track("Aint No Rest Triggered", 'music/chris.ogg')
    trackArcticMonkeys = Track("Do I Wanna Know", 'music/AM.ogg')

    arraySongs = [
        # put songs here as: varName,
        trackRickAstleyNever,
        trackShootingStars,
        trackBanksGeminiFeed,
        trackChrisRayGun,
        trackArcticMonkeys,
    ]

    arrayRandomSongs = []
    arrayChosen = []
    trackchosen = ""

    def randomizeArray(self):
        del self.arrayRandomSongs[:] # wipes array of all contents without making a new one
        self.arrayRandomSongs = self.arraySongs[:]
        random.shuffle(self.arrayRandomSongs)

    def chooseListing(self):
        del self.arrayChosen[:] # same here
        for i in xrange(4):
            self.arrayChosen.append(self.arrayRandomSongs[i])
        del self.arrayRandomSongs[0:3]

    def chooseTrack(self):
        self.trackChosen = random.choice(self.arrayChosen)
