from pykeyboard import PyKeyboard
import time
from random import randint
from pymouse import PyMouse

k = PyKeyboard()

for x in range(2000):
    # To Create an Alt+Tab combo
    # k.press_key(k.alt_key)
    # k.tap_key(k.tab_key)
    # k.release_key(k.alt_key)
    
    # sleep seconds
    print('s')
    time.sleep(2)
    print("r...")
    # simulate key presses
    random_key_count = sum(1 for _ in iter(lambda: randint(0, 2000), 2))
    for x in range(random_key_count):
        random_mouse_clicks = randint(0, 20)
        for x in range(random_mouse_clicks):
            m = PyMouse()
            x, y = m.position() #gets mouse current position coordinates
            m.click(x,y) #the third argument "1" represents the mouse button
            time.sleep(.3)
            #print("Mouse clicked.")
            #k.press_key(k.alt_key)
            k.tap_key(k.alt_key)
            #print("Alt Key sent.")

        k.tap_key(k.alt_key)
        #print("Alt Key sent.")
        sleep_time = randint(1, 2)
        #print("sleeping %ss"%sleep_time)
        time.sleep(sleep_time)
       
    print("\n\n ni.")

