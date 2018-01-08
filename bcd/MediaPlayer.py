import pygame
import pyttsx


class MediaPlayer:
        """docstring for MediaPlayer."""
        clock = ""
        paused = False
        currentlyPlaying = ""
        currentBarcode = ""

        def __init__(self):
            self.data = []
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
                print pygame.mixer.music.get_busy()
                return pygame.mixer.music.get_busy()
                #self.tick()
            except Exception as e:
                print("Exception in playSong!")
                #self.close()

        def getVolume(self):
            return pygame.mixer.music.get_volume()

        def setVolume(self,volume):
            pygame.mixer.music.set_volume(volume)

        def getBarcode(self):
            return self.currentBarcode

        def setBarcode(self,code):
            self.currentBarcode = code

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
