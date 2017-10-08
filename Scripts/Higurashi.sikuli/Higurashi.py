Settings.MoveMouseDelay = 0
running = True
count = 0

def runHotkey(event):
    global running
    running = False

Env.addHotkey(Key.F1, KeyModifier.ALT, runHotkey)

while(running):
    if (exists("1507485878000.png", .5)):
        #If tip window shows up, wait
        wait(3)
        #Finding element in second screen
        scr1 = Screen(1)
        scr1.click("1507486006667.png")
        exit()
    elif (exists(Pattern("1507484956784.png").similar(0.50), .5) or exists(Pattern("1507485545706.png").similar(0.55), .5) or exists("1507484935580.png") or count == 10):
        #Regular sequence
        wait(1.5 *  count + 1)
        type(Key.ENTER)
        count = 0
    else:
        count += 1
    wait(1)
        
        
        
        