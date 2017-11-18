Settings.MoveMouseDelay = 0
running = True
scr1 = Screen(1)

def runHotkey(event):
    global running
    running = False

Env.addHotkey(Key.F1, KeyModifier.ALT, runHotkey)

while(running):
    if ((exists("1510798837938.png") or exists("1510889800736.png")) and scr1.exists(Pattern("1507491127022.png").exact(), .3)):
        #If tip window shows up, wait
        wait(2)
        #Finding element in second screen
        scr1.doubleClick("1507486006667.png")
        type(Key.F7)
        
        exit()