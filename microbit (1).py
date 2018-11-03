# Add your Python code here. E.g.
from microbit import *

rpsls=[
    rock=Image("00000:"
           "00000:"
           "00900:"
           "09990:"
           "09990")
    display.show(rock)

    paper=Image(  "00000:"
              "09990:"
              "09990:"
              "09990:"
              "00000")
    display.show(paper)

    scissors=Image("99009:"
               "99090:"
               "00900:"
               "99090:"
               "99009")
    display.show(scissors)

    spock=Image("00000:"
            "09090:"
            "09090:"
            "09990:"
            "09999")
    display.show(spock)

    Lizard=Image("00900:"
             "99999:"
             "00900:"
             "09990:"
             "90909")
    display.show(Lizard)

]
while True:
     if accelerometer.was_gesture("shake"):
            display.clear()
            choice = random.randint(0, 3)
            if choice == 0:
                display.show(rock)
                break
            elif choice == 1:
                display.show(paper)
                break
            elif choice == 2:
                display.show(Lizard)
                break
            elif choice == 3:
                display.show(spock)
            else:
                display.show(scissors)
                break
            
        
    