modes = ("Add", "Sub", "Mul", "Div")
option = select("What would you like to do?", options = modes)
click("1491630044286.png")
wait("1491630110161.png")
type("calc" + Key.ENTER)
wait("1491630710712.png")
click(Pattern("1491630710712.png").targetOffset(43,2))
if option == modes[0]:
    click(Pattern("1491630710712.png").targetOffset(211,66))
elif option == modes[1]:
    click(Pattern("1491630710712.png").targetOffset(208,0))
elif option == modes[2]:
    click(Pattern("1491630710712.png").targetOffset(205,-63))
else:
    click(Pattern("1491630710712.png").targetOffset(208,-139))
click(Pattern("1491630710712.png").targetOffset(43,-2))
click(Pattern("1491630710712.png").targetOffset(205,127))
