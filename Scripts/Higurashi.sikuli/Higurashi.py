Settings.MoveMouseDelay = 0
running = True
count = 0

def runHotkey(event):
    global running
    running = False

Env.addHotkey(Key.F1, KeyModifier.ALT, runHotkey)

while(running):
    if (exists(Pattern("1502652749997.png").similar(0.50)) or exists(Pattern("1502652648894.png").similar(0.52)) or count == 10):
        
        wait(1.5 *  count + 1)
        type(Key.ENTER)
        count = 0
    else:
        count += 1
    wait(1)
        
        
        
        