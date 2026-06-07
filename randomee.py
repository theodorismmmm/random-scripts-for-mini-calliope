from microbit import *
import random

while True:
    display.show(Image.MEH) 
    rgb.clear()
    
    if microphone.sound_level() > 70:
        display.show(Image.SURPRISED)
        sleep(500)
        
        erfolgt = False
        for i in range(5, 0, -1):
            display.show(str(i))
            if button_a.is_pressed():
                erfolgt = True
                break
            sleep(200)
            
        if erfolgt:
            display.show(Image.HAPPY)
            audio.play(Sound.HAPPY)
        else:
            display.show(Image.SKULL)
            audio.play(Sound.SAD)
            
        sleep(2000)
