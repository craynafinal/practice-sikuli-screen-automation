Settings.MoveMouseDelay = 0
running = True

def runHotkey(event):
    global running
    running = False

Env.addHotkey(Key.F1, KeyModifier.ALT, runHotkey)

while(running):
    if (exists("1507485878000.png", .005) or (exists("1509668195740.png", .005))):
        #If tip window shows up, wait
        wait(2)
        #Finding element in second screen
        click("1511398531290.png")
        wait(.5)
        click("1507486006667.png")
        
        exit()
    elif (exists("1512201064021.png", .003)or exists(Pattern("1507484935580.png").similar(0.45), .003)):
        #Regular sequence
        wait(.03)
        type(" ")
    else:
        wait(.03)
        type(" ")