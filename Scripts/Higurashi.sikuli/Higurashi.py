Settings.MoveMouseDelay = 0
running = True
count = 0

def runHotkey(event):
    global running
    running = False

Env.addHotkey(Key.F1, KeyModifier.ALT, runHotkey)

while(running):
    #if (exists(Pattern("1502652749997.png").similar(0.50)) or exists(Pattern("1502652648894.png").similar(0.52)) or count == 5):
    if (count == 5):
        #click(Pattern("1492570635141.png").targetOffset(618,52))
        type(Key.ENTER)
        count = 0
        wait(2);
    else:
        count += 1
        
        
        