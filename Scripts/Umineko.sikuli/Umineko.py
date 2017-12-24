Settings.MoveMouseDelay = 0
running = True
scr1 = Screen(1)

def runHotkey(event):
    global running
    running = False

Env.addHotkey(Key.F1, KeyModifier.ALT, runHotkey)

while(running):
    if (exists("1513223956876.png", .5) and exists("1513223975753.png", .5)):
         #If tip window shows up, wait
        wait(2)
        #Finding element in second screen
        scr1.doubleClick("1507486006667-1.png")
        type(Key.F7)
        
        exit()
    else:
        wait(.5)
        click("1513223915631.png")