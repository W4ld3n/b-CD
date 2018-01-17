#!/usr/bin/python
import bcd as cd

engine = cd.Engine()
while not engine.getStatus() == engine.STATE_CLOSE and not engine.getStatus() == engine.STATE_ERROR:
    engine.update()
    c = engine.askCode()
    engine.processInput(c)
engine.shutdown()
