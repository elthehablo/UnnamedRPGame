import keyregistry
import os

class Menu:
    #this class is used to start the program
    def __init__(self, isSaved, skipTutorial):
        self.isSaved = isSaved
        self.skipTutorial = skipTutorial
    
    def start(self):
        if(self.skipTutorial):
            print("skipping tutorial")
        else:
            #TODO: script tutorial
            return
        keyBeingPressed = None
        position = 0
        while(keyBeingPressed != quit):
            self.cursorprint(position)
            keyBeingPressed = keyregistry.KeyRegistry.keyPressed()
            if(keyBeingPressed == 'moveDown'):
                if(position < 2):
                    position += 1
            elif(keyBeingPressed == 'moveUp'):
                if(position > 0):
                    position -= 1
            elif(keyBeingPressed == "interact"):
                if(position == 0):
                    #TODO: start new game
                    print("to be implemented")
                elif(position == 1):
                    #TODO: load saved game(using txt character sheets)
                    print("to be implemented")
                elif(position == 2):
                    break
    
    def cursorprint(self, position):
        os.system('cls')
        print("------------------")
        print("Welcome back!")
        print("------------------")
        print("What do you want to do?")
        if(position == 0):
            print(">", end = '')
        print("start new game")
        if(position == 1):
            print(">", end = '')
        print("continue saved game")
        if(position == 2):
            print(">", end = '')
        print("exit")
        
            
        