import threading
import bcd as cd
import bcd.accessories as cda
import time

class Engine:
    STATE_INIT = "INIT"
    STATE_PLAYING = "PLAYING"
    STATE_PAUSED = "PAUSED"
    STATE_ERROR = "ERROR"
    STATE_CLOSE = "CLOSE"
    STATE_READY = "READY"

    state=""
    mp = ""
    gui = ""
    mapping = ""

    def __init__(self):
        self.state = self.STATE_INIT
        self.mp = cd.MediaPlayer(self)
        self.gui = cd.GUI()

        self.mp.say("Loading library.")
        cda.createBarcodeMapping()
        self.mapping = cda.loadBarcodeMapping()
        self.updateGUI()

        playcheck = PlayChecker(1, "Thread-1", 1, self, self.mp)
        playcheck.start()

        self.setStatus(self.STATE_READY)
        self.mp.say("Ready to rock, my lord!")
        self.updateGUI()

    def setStatus(self,state):
        self.state = state

    def getStatus(self):
        return self.state


    def shutdown(self):
        #print "Goodbye"
        self.mp.say("Goodbye")
        self.gui.close()
        self.mp.close()

    def updateGUI(self):
        #self.gui.init()
        self.gui.updateStatus(self.getStatus())
        self.gui.updateSong(self.mp.currentlyPlaying)
        self.gui.updateVolume(str(self.mp.getVolume()))
        self.gui.updateBarcode(str(self.mp.getBarcode()))


    def askCode(self):
        code = self.gui.inputCommand()
        return code.strip()

    def getMapping(self):
        return self.mapping

    def getMP(self):
        return self.mp

    def getGUI(self):
        return self.gui

    def update(self):
        self.mp.tick()
        self.updateGUI()


    def processInput(self,s):
        if(s == "s" or s=="q"):
            self.setStatus(self.STATE_CLOSE)
        elif(s == "r"):
            d = cda.randomSong()
            self.mp.trySong(d[0])
            self.setStatus(self.STATE_PLAYING)
            self.mp.setBarcode(d[1])
            #self.gui.updateBarcode(d[1])
        elif(s == "+"):
            self.mp.setVolume(mp.getVolume()+0.2)
        elif(s == "-"):
            self.mp.setVolume(mp.getVolume()-0.2)
        elif(s == "p"):
            self.mp.pause()
            if self.mp.isPaused():
                self.setStatus(self.STATE_PAUSED)
            else:
                self.setStatus(self.STATE_PLAYING)
        else:
            try:
                d = self.mapping[s]
                d = cda.chooseSong(d)
                self.mp.trySong(d)
                self.setStatus(self.STATE_PLAYING)
                self.mp.setBarcode(s)

            except Exception as e:
                self.mp.say("I'm afraid I can't let you do that!")

#
class PlayChecker(threading.Thread):
    engine="";
    mp="";
    playing = "";
    def __init__(self,threadID, name, counter, engine, mp):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter
        self.engine = engine
        self.mp = mp
        self.playing = False;


    def run(self):
        while(self.engine.getStatus() != self.engine.STATE_CLOSE):
            time.sleep(0.1)
            self.checkPlaying()
            #self.engine.update()
            if (self.engine.getStatus() == self.engine.STATE_PLAYING and not self.playing):
                self.playing = True
            elif(not self.mp.getBusy() and self.playing):
                self.mp.refresh()
    def checkPlaying(self):
        if self.mp.currentlyPlaying:
            self.engine.setStatus(self.engine.STATE_PLAYING)
