import keyboard
import time

class KeyRegistry:
    def keyPressed():
        #TODO: enhance while loop to catch errors
        while True:
            try:
                if keyboard.is_pressed('w'):
                    time.sleep(0.5)
                    return "moveUp"
                elif keyboard.is_pressed('a'):
                    time.sleep(0.5)
                    return "moveLeft"
                elif keyboard.is_pressed('s'):
                    time.sleep(0.5)
                    return "moveDown"
                elif keyboard.is_pressed('d'):
                    time.sleep(0.5)
                    return "moveRight"
                elif keyboard.is_pressed('f'):
                    time.sleep(0.5)
                    return "interact"
            except:
                break
        return
                