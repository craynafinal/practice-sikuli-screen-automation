Settings.MoveMouseDelay = 0
running = True
count = 0

def runHotkey(event):
    global running
    running = False

Env.addHotkey(Key.F1, KeyModifier.ALT, runHotkey)

while(running):
    if ((exists("1508618395181.png", .5)
            or exists("1508119076616.png", .5)
            or exists("1508618699091.png", .5)
            or exists(Pattern("1508620235412.png").exact(), .5)
            or exists("1508624294446.png", .5)
                
                
                )
            and exists("1508618845400.png", .5)
            
            ):
        click("1507486006667.png")
        wait(1)
        exit()    
    wait(1)
    wait(1)
        
        
        