import time
import math

Settings.MoveMouseDelay = 0
running = True
scr0 = Screen(0)
scr1 = Screen(1)
waitTimestamp = time.time()

def runHotkey(event):
    global running
    running = False

Env.addHotkey(Key.F1, KeyModifier.ALT, runHotkey)

while(running):
    #print(time.time())
    if (scr0.exists(Pattern("1519974992622.png").similar(0.61), 1) or scr0.exists(Pattern("1519975036521.png").similar(0.45), 1)):
        value = max(time.time() - waitTimestamp, 1)
        print(value)
        print(time.time() - waitTimestamp)
        print(math.pow(value, 2))
        wait(1 + math.pow(value, 2))
        #wait(math.pow(value, 2))
        type(Key.ENTER)
        waitTimestamp = time.time()



    