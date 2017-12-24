Settings.MoveMouseDelay = 0
running = True

def runHotkey(event):
    global running
    running = False

Env.addHotkey(Key.F1, KeyModifier.ALT, runHotkey)

while(running):
    if (exists("1512958109835.png", .5) and exists("1512958130690.png", .5)):
        #If tip window shows up, wait
        wait(2)
        #Finding element in second screen
        #click("1511398531290.png")
        click("1514157343393.png")
        wait(.5)
        type(Key.F7)
        
        exit()
    else:
        wait(.5)
        #click("1512958383576.png")
        click(Pattern("1514157458056.png").exact())