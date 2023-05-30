import os
import time

import dieroller
import importer
import keyregistry

class Combat:
    #contains values of the imported creatures
    creatureValues = []
    playerValues = []
    currentCreatureHealth = 0
    currentPlayerHealth = 0
    
    def __init__(self, combatPlayer, creatureID):
        self.combatPlayer = combatPlayer
        self.creatureID = creatureID
        
        #initialisation of creature and player
        self.creatureValues = self.importCreature()
        self.currentCreatureHealth = self.creatureValues[3]
        self.currentPlayerHealth = combatPlayer[2]
    
    def importCreature(self):
        newImport = importer.ImportHandler("source/resources/creatures.txt")
        newCreatureValues = newImport.ImportCreature(self.creatureID)
        return newCreatureValues
    
    def importPlayer(self, filename):
        #imports stats for the player
        #note: shouldn't really be used. just as a backup
        #save files don't really include the relevant information
        return
    
    
    def printCombat(self, debugging = False):
        keyBeingPressed = None
        position = 0
        while(keyBeingPressed != "quit"):
            os.system('cls')
            print(self.creatureValues)
            print("------------------")
            print("A "+str(self.creatureValues[1].decode('UTF-8'))+" appears!")
            print("------------------")
            print("Creature level: "+str(self.creatureValues[2]))
            print("Creature health: "+str(self.currentCreatureHealth)+"/"+str(self.creatureValues[3]))
            print("------------------")
            self.combatCursor(position)
            keyBeingPressed = keyregistry.KeyRegistry.keyPressed()
            if(keyBeingPressed == 'moveDown'):
                if(position < 3):
                    position += 1
            elif(keyBeingPressed == 'moveUp'):
                if(position > 0):
                    position -= 1
            elif(keyBeingPressed == "interact"):
                if(position == 0):
                    #TODO: implement fighting
                    rolls = self.combatInitiativeRoll()
                    self.combatProcess(rolls)
                    break
                elif(position == 1):
                    #TODO: implement using ability (spells)
                    print("to be implemented")
                elif(position == 2):
                    #TODO: implement using item
                    print("to be implemented")
                elif(position == 3):
                    if(debugging):
                        return True
                    else:
                        return False #if not debugging
                    
        
    def combatCursor(self, position):
        print("What do you want to do?")
        if(position == 0):
            print(">", end = '')
        print("fight")
        if(position == 1):
            print(">", end = '')
        print("ability")
        if(position == 2):
            print(">", end = '')
        print("item")
        if(position == 3):
            print(">", end = '')
        print("run")
        
    
    def combatInitiativeRoll(self):
        '''
        simulating roll for initiative
        
        return -- returns boolean whether player rolled higher or equal to the monster, meaning the player should go first
        '''
        monsterRoll = dieroller.DieRoller.rollD20() 
        playerRoll = dieroller.DieRoller.rollD20()
        print(str(self.creatureValues[1].decode('UTF-8'))+" rolled "+str(monsterRoll)+" for initiative!")
        print("Player rolled "+str(playerRoll)+" for initiative!")
        time.sleep(2) #sleep to show rolls
        return playerRoll >= monsterRoll 
    
    def combatProcess(self, playerGoesFirst):
        position = 0
        os.system('cls')
        print(self.creatureValues)
        print("------------------")
        print("A "+str(self.creatureValues[1].decode('UTF-8'))+" appears!")
        print("------------------")
        print("Creature level: "+str(self.creatureValues[2]))
        print("Creature health: "+str(self.currentCreatureHealth)+"/"+str(self.creatureValues[3]))
        print("------------------")
        self.combatCursor(position)
        combatDone = False
        while(not combatDone):
            #TODO: implement combat
            if(playerGoesFirst):
                #do player turn first
                break
            else:
                #do enemy turn first
                break
    
    def damageToMonster():
        return
    
    def damageToPlayer():
        return