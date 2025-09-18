from microbit import *
import radio


radio.config(group=1)
radio.on()

while True:
    message = radio.receive()
    if message:
        display.show(Image.HAPPY)
        
    if button_a.was_pressed():
        display.clear()
        radio.send('smile')
        
    if button_b.was_pressed():
        display.clear()
        radio.send('frown')
    