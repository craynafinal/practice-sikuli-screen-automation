Settings.MoveMouseDelay = 0
running = True
shouldClickFor = 50
shouldUpgrade = False
timeToDead = 0

def runHotkey(event):
    global running
    running = False

Env.addHotkey(Key.F1, KeyModifier.CTRL, runHotkey)

ch = switchApp("계산기")

while(ch.hasWindow() and running):
    if shouldClickFor > 0:
        hover(Pattern("1491633515034.png").targetOffset(1,127))
        while shouldClickFor > 0 and running:
            mouseDown(Button.LEFT)
            mouseUp(Button.LEFT)
            shouldClickFor -= 1
#    if timeToDead >= 2 and not exists()
        