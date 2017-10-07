Settings.MoveMouseDelay = 0
running = True
count = 0

def runHotkey(event):
    global running
    running = False

Env.addHotkey(Key.F1, KeyModifier.ALT, runHotkey)

while(running):
    if (exists(Pattern("1507354727310.png").similar(0.80)) or exists("1507354826038.png") or count == 10):
        
        wait(1.5 *  count + 2)
        type(Key.ENTER)
        count = 0
    else:
        count += 1
    wait(1)
        
        
        