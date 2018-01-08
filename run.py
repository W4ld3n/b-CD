import bcd as cd
import bcd.accessories as cda
import os
import time
import threading


class Engine:
    STATE_INIT = "INIT"
    STATE_PLAYING = "PLAYING"
    STATE_PAUSED = "PAUSED"
    STATE_ERROR = "ERROR"
    STATE_CLOSE = "CLOSE"
    STATE_READY = "READY"

    state=""
    def __init__(self):
        self.state = self.STATE_INIT

    def setStatus(self,state):
        self.state = state

    def getStatus(self):
        return self.state



mp = cd.MediaPlayer()

g = cd.GUI()
g.init()
engine = Engine()



def codeGUI():
    g.updateStatus(engine.getStatus())
    g.updateSong(mp.currentlyPlaying)
    g.updateVolume(str(mp.getVolume()))
    code = g.inputCommand()
    return code.strip()

def trySong(path):
    print(path)
    while not mp.playSong(path):
        time.sleep(2)
        if not mp.playSong(path):
            d = cda.chooseSong(path)
            print(d)

mp.say("Loading library.")
cda.createBarcodeMapping()
mapping = cda.loadBarcodeMapping()

engine.setStatus(engine.STATE_READY)
mp.say("Ready to rock, my lord!")

while not engine.getStatus() == engine.STATE_CLOSE:
    mp.tick()
    #s = raw_input("What to do next?  ")
    s = codeGUI()
    if(s == "s" or s=="q"):
        engine.setStatus(engine.STATE_CLOSE)
    elif(s == "r"):
        d = cda.randomSong()
        trySong(d[0])
        engine.setStatus(engine.STATE_PLAYING)
        mp.setBarcode(d[1])
        g.updateBarcode(d[1])
    elif(s == "+"):
        mp.setVolume(mp.getVolume()+0.2)
    elif(s == "-"):
        mp.setVolume(mp.getVolume()-0.2)
    elif(s == "p"):
        mp.pause()
        if mp.isPaused():
            engine.setStatus(engine.STATE_PAUSED)
        else:
            engine.setStatus(engine.STATE_PLAYING)
    else:
        try:
            d = mapping[s]
            d = cda.chooseSong(d)
            trySong(d)
            engine.setStatus(engine.STATE_PLAYING)
            mp.setBarcode(d[1])
            g.updateBarcode(s)
        except Exception as e:
            mp.say("I'm afraid I can't let you do that!")



def shutdown():
    print "Goodbye"
    mp.say("Goodbye")
    g.close()
    mp.close()

shutdown()
