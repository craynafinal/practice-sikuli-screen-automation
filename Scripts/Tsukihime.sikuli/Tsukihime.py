Settings.MoveMouseDelay = 0
running = True
count = 0

def runHotkey(event):
    global running
    running = False

Env.addHotkey(Key.F1, KeyModifier.ALT, runHotkey)

while(running):
    if (exists(Pattern("1556857712168.png").similar(0.80)) or exists(Pattern("1556857757472.png").similar(0.80))):
        wait(.6 + (.2 * count))
        type(Key.ENTER)
        count = 0
        wait(.3 + (.05 * count))
    else:
        count += 1
    wait(.5)
        
        
        
        