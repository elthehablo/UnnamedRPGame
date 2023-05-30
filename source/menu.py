import os
import numpy as np

import keyregistry
import combat

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
        newPosition = 0
        debug = False
        debugCombat = False
        while(keyBeingPressed != "quit"):
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
                    self.newgame()
                elif(position == 1):
                    #TODO: load saved game(using txt character sheets)
                    print("to be implemented")
                elif(position == 2):
                    break
            elif(keyBeingPressed == "debug"):
                debug = True
                break
        
        while(debug and keyBeingPressed != "quit"):
            #open debug menu
            self.debugMenuPrint(newPosition)
            keyBeingPressed = keyregistry.KeyRegistry.keyPressed()
            if(keyBeingPressed == 'moveDown'):
                if(newPosition < 2):
                    newPosition += 1
            elif(keyBeingPressed == 'moveUp'):
                if(newPosition > 0):
                    newPosition -= 1
            elif(keyBeingPressed == "interact"):
                if(newPosition == 0):
                    #TODO: fight creature
                    debugCombat = True
                    break
                elif(newPosition == 1):
                    #TODO: TBA
                    print("to be implemented")
                elif(newPosition == 2):
                    debug = False
                    self.start()
        
        while(debugCombat and keyBeingPressed != "quit"):
            #open debug menu
            parseCondition = False
            
            while(not parseCondition):
                parsedCreatureID = int(input("enter creature ID:"))
                if(parsedCreatureID >= 0 and parsedCreatureID < 100000):
                    # dummy check 
                    # unfortunately with the cast we still might be able 
                    # to parse weird things
                    parseCondition = True
                else:
                    print("not a valid ID!")
            
            debugPlayer = np.array([0, 1, 100, 100, 1, 1, 1, 1, 1, 1, 0])
            newCombat = combat.Combat(debugPlayer, parsedCreatureID)
            cond = newCombat.printCombat(True)
            if(cond):
                debugCombat = False
            
        self.start()
                    
            
                
    
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
    
    def newgame(self):
        os.system('cls')
        print("------------------")
        print("Starting new game!")
        print("------------------")
        print("Enter your character stats:")
        name = str(input("Your name: "))
        level = int(input("Your level: "))
        healthpoints = int(input("Your health points: "))
        manapoints = int(input("Your mana points: "))
        strength = int(input("Your strength: "))
        dexterity = int(input("Your dexterity: "))
        constitution = int(input("Your constitution: "))
        intelligence = int(input("Your intelligence: "))
        wisdom = int(input("Your wisdom: "))
        charisma = int(input("Your charisma: "))
        experience = 0
        
        newcharacter = np.array([0, level, healthpoints, manapoints, strength, dexterity, constitution, intelligence, wisdom, charisma, experience])
        path = "source/resources/characters/"+str(name)+".txt"
        hd, ft = self.prettyHeaderAndFooter(name)
        np.savetxt(path, newcharacter, header = hd, footer = ft, delimiter = ',', newline = " ", comments = "", fmt = '%i')

    def prettyHeaderAndFooter(self, name):
        '''
        creates a nice header and footer for the character sheet using the character name
        '''
        blank = ''
        for i in range(len(name)):
            blank += '-'
        header = '#-----'+str(name)+'-----\n'
        footer = '\n#-----'+str(blank)+'-----\n'
        
        return header, footer
        
    def debugMenuPrint(self, position):
        os.system('cls')
        print("------------------")
        print("Secret debug menu")
        print("------------------")
        print("What do you want to do?")
        if(position == 0):
            print(">", end = '')
        print("fight creature with id")
        if(position == 1):
            print(">", end = '')
        print("TBA")
        if(position == 2):
            print(">", end = '')
        print("exit")

    def savegame(self):
        return
    
            
        