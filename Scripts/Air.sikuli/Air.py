Settings.MoveMouseDelay = 0
running = True
waitTimestamp = time.time()

def runHotkey(event):
    global running
    running = False

Env.addHotkey(Key.F1, KeyModifier.ALT, runHotkey)

while(running):
    if (exists(Pattern("1532233126059.png").similar(0.80), .5)):
        wait(2)
        type(Key.F8)
        running = False
        exit()



    