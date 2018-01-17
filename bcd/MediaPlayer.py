import pygame
import pyttsx
import bcd.accessories as cda
import time


class MediaPlayer:
        """docstring for MediaPlayer."""
        clock = ""
        paused = False
        currentlyPlaying = ""
        currentBarcode = ""
        engine = ""

        def __init__(self, engine):
            self.data = []
            self.engine = engine
            pygame.init()
            pygame.mixer.init()
            pygame.mixer.pre_init(44100, -16, 2, 2048)
            self.setVolume(1.0)
            self.clock = pygame.time.Clock()
            self.paused = False

        def playSong(self,path):
            try:
                if pygame.mixer.music.get_busy():
                    self.tick()
                    pygame.mixer.music.stop()
                    self.tick()
                pygame.mixer.music.load(path)
                pygame.mixer.music.play()
                self.paused = False
                self.currentlyPlaying = path
                time.sleep(0.5)
                self.engine.updateGUI()
                time.sleep(0.5)
                #print pygame.mixer.music.get_busy()
                return pygame.mixer.music.get_busy()
                #self.tick()
            except Exception as e:
                print("Exception in playSong!")
                #self.close()

        def getVolume(self):
            return pygame.mixer.music.get_volume()

        def setVolume(self,volume):
            pygame.mixer.music.set_volume(volume)
            #self.engine.updateGUI()

        def getBarcode(self):
            return self.currentBarcode

        def setBarcode(self,code):
            self.currentBarcode = code
            self.engine.updateGUI()

        def close(self):
            pygame.quit()

        def tick(self):
            try:
                self.clock.tick(300)
                #print pygame.mixer.music.get_busy()
            except Exception as e:
                print("Exception!")

        def say(self,sentence):
            speech = pyttsx.init()
            speech.setProperty('rate', 150)
            speech.say(sentence)
            speech.runAndWait()
            #speech.close()

        def pause(self):
            if not self.paused:
                pygame.mixer.music.pause()
                self.paused = True
            else:
                pygame.mixer.music.unpause()
                self.paused = False

        def getBusy(self):
            return pygame.mixer.music.get_busy()

        def isPaused(self):
            return self.paused

        def refresh(self):
            mapping = cda.loadBarcodeMapping()
            d = mapping[self.currentBarcode]
            d = cda.chooseSong(d)
            self.trySong(d)
            self.engine.update()

        def trySong(self,path):
            while not self.playSong(path):
                time.sleep(2)
                if not self.playSong(path):
                    d = cda.chooseSong(path)
