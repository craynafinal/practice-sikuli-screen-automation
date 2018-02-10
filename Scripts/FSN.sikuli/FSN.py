Settings.MoveMouseDelay = 0
running = True

def runHotkey(event):
    global running
    running = False

Env.addHotkey(Key.F1, KeyModifier.ALT, runHotkey)

while(running):
    if (exists("1517759683333.png")):
        wait(2)
        doubleClick("1507486006667-1.png")
        type(Key.F7)
        
        exit()
    else:
        wait(.5)