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
        '''
        imports creature that you want to fight, using the creatureID provided
        
        --arguments--
        none
        
        --returns--
        the values of the imported creature
        '''
        newImport = importer.ImportHandler("source/resources/creatures.txt")
        newCreatureValues = newImport.ImportCreature(self.creatureID)
        return newCreatureValues
    
    def importPlayer(self, filename):
        #imports stats for the player
        #note: shouldn't really be used. just as a backup
        #save files don't really include the relevant information
        return
    
    
    def printCombat(self, debugging = False):
        '''
        void function that prints the combat menu that you can use for actions
        
        --arguments--
        debugging -- boolean value that is used when we are fighting a monster in debug mode
        
        --returns--
        none
        '''
        keyBeingPressed = None
        position = 0
        while(keyBeingPressed != "quit"):
            os.system('cls')
            print("------------------")
            print("A "+str(self.creatureValues[1].decode('UTF-8'))+" appears!")
            print("------------------")
            print("Creature level: "+str(self.creatureValues[2]))
            print("Creature health: "+str(self.currentCreatureHealth)+"/"+str(self.creatureValues[3]))
            print("------------------")
            self.combatCursor(position)
            rolls = self.combatInitiativeRoll()
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
                    self.combatProcess(rolls, False, False)
                    if(debugging):
                        return True
                    else:
                        return False #if not debugging
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
        '''
        the cursor
        '''
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
    
    def combatProcess(self, playerGoesFirst, combatDone, playerWon):
        if(combatDone):
            return playerWon
        
        position = 0
        while(not combatDone):
            #TODO: implement combat
            os.system('cls')
            print("------------------")
            print("Creature level: "+str(self.creatureValues[2]))
            print("Creature health: "+str(self.currentCreatureHealth)+"/"+str(self.creatureValues[3]))
            print("------------------")
            print("Your level: "+str(self.combatPlayer[1]))
            print("Your health: "+str(self.currentPlayerHealth)+"/"+str(self.combatPlayer[2]))
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
                    if(playerGoesFirst):
                        #do player turn first
                        damageDoneToCreature = self.damageToMonster()
                        self.currentCreatureHealth -= damageDoneToCreature
                        if(self.currentCreatureHealth <= 0):
                            print("Player won!")
                            time.sleep(2)
                            print("Experience gained: "+str(self.creatureValues[11]))
                            time.sleep(5)
                            return True #player won
                        damageDoneToPlayer = self.damageToPlayer()
                        self.currentPlayerHealth -= damageDoneToPlayer
                        if(self.currentPlayerHealth <= 0):
                            return False #player dead
                        self.combatProcess(playerGoesFirst, False, False)
                    else:
                        #do enemy turn first
                        damageDoneToPlayer = self.damageToPlayer()
                        self.currentPlayerHealth -= damageDoneToPlayer
                        if(self.currentPlayerHealth <= 0):
                            return False #player dead
                        damageDoneToCreature = self.damageToMonster()
                        self.currentCreatureHealth -= damageDoneToCreature
                        if(self.currentCreatureHealth <= 0):
                            print("Player won!")
                            time.sleep(2)
                            print("Experience gained: "+str(self.creatureValues[11]))
                            time.sleep(5)
                            return True #player won
                        self.combatProcess(playerGoesFirst, False, False)
                
                elif(position == 1):
                    #TODO: implement using ability (spells)
                    print("to be implemented")
                elif(position == 2):
                    #TODO: implement using item
                    print("to be implemented")
                elif(position == 3):
                    break
    
    def damageToMonster(self):
        #TODO: add AC to monsters in creatures.txt for now we use default 15 same goes for weapon modifiers and dice to be rolled
        ArmorClass = self.creatureValues[12] #armor class value
        WeaponModifier = 0 #hack
        #using dice d6
        rolldamage1 = dieroller.DieRoller.rollD6()
        rolldamage2 = dieroller.DieRoller.rollD6()
        
        hitroll = dieroller.DieRoller.rollD20()
        totaldamage = 0
        print("Player hits ("+str(hitroll)+") for: ", end="")
        time.sleep(1)
        if(hitroll == 20):
            print("Critical hit for "+str(rolldamage1)+" and "+str(rolldamage2)+" damage!")
            totaldamage = rolldamage1+rolldamage2
        elif(hitroll+WeaponModifier > ArmorClass):
            print("Hit for "+str(rolldamage1)+" damage!")
            totaldamage = rolldamage1
        else:
            print("Miss!")
        time.sleep(2)
        return totaldamage
    
    def damageToPlayer(self):
        PlayerArmorClass = 17 #hack
        CreatureAttackModifier = self.creatureValues[15] #attack value
        #NOTE: about below. ideally we'd want a function
        # that can do a for loop with rolls with the amount
        # of hit dice we need from the table
        # this is to be implemented
        match (self.creatureValues[13].decode('UTF-8')):
            case "d4":
                rolldamage1 = dieroller.DieRoller.rollD4()
                rolldamage2 = dieroller.DieRoller.rollD4()
            case "d6":
                rolldamage1 = dieroller.DieRoller.rollD6()
                rolldamage2 = dieroller.DieRoller.rollD6()
            case "d10":
                rolldamage1 = dieroller.DieRoller.rollD10()
                rolldamage2 = dieroller.DieRoller.rollD10()
            case "d12":
                rolldamage1 = dieroller.DieRoller.rollD12()
                rolldamage2 = dieroller.DieRoller.rollD12()
            case "d20":
                rolldamage1 = dieroller.DieRoller.rollD20()
                rolldamage2 = dieroller.DieRoller.rollD20()
            case "d100":
                rolldamage1 = dieroller.DieRoller.rollD100()
                rolldamage2 = dieroller.DieRoller.rollD100()
            case _:
                #default case, default to d4
                rolldamage1 = dieroller.DieRoller.rollD4()
                rolldamage2 = dieroller.DieRoller.rollD4()
        
        hitroll = dieroller.DieRoller.rollD20()
        totaldamage = 0
        print("Creature hits ("+str(hitroll)+") for: ", end="")
        time.sleep(1)
        if(hitroll == 20):
            print("Critical hit for "+str(rolldamage1)+" and "+str(rolldamage2)+" damage!")
            totaldamage = rolldamage1+rolldamage2
        elif(hitroll+CreatureAttackModifier > PlayerArmorClass):
            print("Hit for "+str(rolldamage1)+" damage!")
            totaldamage = rolldamage1
        else:
            print("Miss!")
        time.sleep(2)
        return totaldamage