from time import sleep_ms

from microbit import pin1, display, Image
from speech import say

# Customize bot speaking speed
SPEED = 95

val = 0

while True:
    display.show(Image.SURPRISED)
    
    say('The light is getting brighter!', speed=SPEED)
    
    display.show(Image.HAPPY)
    
    # The val is initialized to 0 on line 6 and 
    # increments by one through each iteration
    # through the while loop until it hits 
    # 1022 and as it does it increments the value
    # of pin1 which makes the light brigter
    # every 5 ms
    while val <= 1022:
        val += 1
        pin1.write_analog(val)
        
        sleep_ms(5)
   
    display.show(Image.SURPRISED)
    
    say('The light is getting darker!', speed=SPEED)
    
    display.show(Image.HAPPY)    
    
    # After we complete the first loop the val
    # is now equal to 1023 so during this
    # while loop it gets smaller until it hits 
    # 0 and as it decrements the value
    # of pin1 which makes the light darker
    # every 5 ms
    while val > 0:
        val -= 1
        pin1.write_analog(val)
        
        sleep_ms(5)
