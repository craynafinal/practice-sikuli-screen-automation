Settings.MoveMouseDelay = 0
running = True
count = 0

def runHotkey(event):
    global running
    running = False

Env.addHotkey(Key.F1, KeyModifier.ALT, runHotkey)

while(running):
    if ((exists("1507485878000.png", .05) or (exists("1509668195740.png", .05)))):
        #If tip window shows up, wait
        wait(2)
        #Finding element in second screen
        type(Key.F7)
        
        exit()
    elif (exists("1547320001138.png", .03) or exists("1547320016459.png", .03) or exists("1547319967504.png", .03) or count == 10):
        #Regular sequence
        wait(.03)
        type(Key.ENTER)
        count = 0
    else:
        count += 1
    wait(.03)
        
        
        
        