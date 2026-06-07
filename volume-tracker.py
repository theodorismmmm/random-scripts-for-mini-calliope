from calliope_mini import *

while True:
    lautstaerke = microphone.sound_level()
    display.scroll(str(lautstaerke))
    sleep(200)
