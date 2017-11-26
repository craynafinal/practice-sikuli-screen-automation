Settings.MoveMouseDelay = 0
running = True
count = 0

def runHotkey(event):
    global running
    running = False

Env.addHotkey(Key.F1, KeyModifier.ALT, runHotkey)

while(running):
    if ((exists("1507485878000.png", .05) or (exists("1509668195740.png", .05))) and exists("1511398610583.png", .1)
            ):
        #If tip window shows up, wait
        wait(2)
        #Finding element in second screen
        click("1511398531290.png")
        wait(.5)
        click("1507486006667.png")
        
        exit()
    elif (exists(Pattern("1507484956784.png").similar(0.45), .03) or exists(Pattern("1507485545706.png").similar(0.45), .03) or exists(Pattern("1507484935580.png").similar(0.45), .03) or count == 10):
        #Regular sequence
        wait(.03)
        type(" ")
        count = 0
    else:
        count += 1
    wait(.03)
        
        
        
        