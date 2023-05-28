import keyboard

class KeyRegistry:
    def keyPressed():
        #TODO: enhance while loop to catch errors
        while True:
            try:
                if keyboard.is_pressed('w'):
                    return "moveUp"
                elif keyboard.is_pressed('a'):
                    return "moveLeft"
                elif keyboard.is_pressed('s'):
                    return "moveDown"
                elif keyboard.is_pressed('d'):
                    return "moveRight"
                elif keyboard.is_pressed('f'):
                    return "interact"
            except:
                break
        return
                