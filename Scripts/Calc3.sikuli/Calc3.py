running = True

def runHotkey(event):
    global running
    running = False

Env.addHotkey(Key.F1, KeyModifier.CTRL, runHotkey)

#Settings.MoveMouseDelay = 1
# 0 means no delay (instant moving), 1 = 1 second

click("1491630044286.png")
wait("1491630110161.png")
type("calc" + Key.ENTER)
wait("1491630710712.png")
#click(Pattern("1491630710712.png").targetOffset(-40,72))

#Settings.MoveMouseDelay = 0

#for step in range(5):
while exists("1491630710712.png") and running:
    click(Pattern("1491630710712.png").targetOffset(217,63))
    click(Pattern("1491630710712.png").targetOffset(-40,66))
click(Pattern("1491630710712.png").targetOffset(211,136))