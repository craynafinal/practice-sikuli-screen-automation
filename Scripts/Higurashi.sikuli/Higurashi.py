Settings.MoveMouseDelay = 0
running = True
count = 0
scr1 = Screen(1)

def runHotkey(event):
    global running
    running = False

Env.addHotkey(Key.F1, KeyModifier.ALT, runHotkey)

while(running):
    if ((exists("1507485878000.png", .05) or (exists("1509668195740.png", .05))) and scr1.exists(Pattern("1507491127022.png").exact(), .1)):
        #If tip window shows up, wait
        wait(2)
        #Finding element in second screen
        scr1.doubleClick("1507486006667.png")
        type(Key.F7)
        
        exit()
    elif (exists(Pattern("1507484956784.png").similar(0.50), .03) or exists(Pattern("1507485545706.png").similar(0.55), .03) or exists("1507484935580.png", .03) or count == 10):
        #Regular sequence
        wait(.03)
        type(Key.ENTER)
        count = 0
    else:
        count += 1
    wait(.03)
        
        
        
        