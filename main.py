import vision
import webservice
import AI
import time
import random

v = vision.Vision()
ws = webservice.WebService()
ai = AI.Agent(ws)
time.sleep(1)

startTimer=time.time()

while(True):
    v.setScreenshot(ws.getScreenshot())
    arrCircles, nextFruit = v.calculateMap()
    print(nextFruit)
    if nextFruit is not None:
        ai.algo1(arrCircles, nextFruit)
    v.waitKey(4000)
