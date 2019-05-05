Settings.MoveMouseDelay = 0
running = True
waitTimestamp = time.time()

def runHotkey(event):
    global running
    running = False

Env.addHotkey(Key.F1, KeyModifier.ALT, runHotkey)

while(running):
    if (exists(Pattern("1543709892399.png").exact())):
        wait(2)
        type(Key.F7)
        running = False
        exit()