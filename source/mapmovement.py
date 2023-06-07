import numpy as np
import dieroller

class MapMovement:
    def __init__(self, currentMap, coords, mapEncounterOdds):
        self.currentMap = currentMap
        self.coords = coords
        self.mapEncounterOdds = mapEncounterOdds
        self.newMapValue = 1
    
    def move(self, keyPress):
        '''
        takes the current map and moves character as long as there is open space
        
        return -- void (movement is done by manipulating self.coords and self.currentMap)
        '''
        #setting old position to open space
        self.currentMap[self.coords[0]][self.coords[1]] = self.newMapValue
        newCoords = np.array(self.coords)
        
        match keyPress:
            case "moveUp":
                newCoords[0] -= 1
            case "moveLeft":
                newCoords[1] -= 1
            case "moveDown":
                newCoords[0] += 1
            case "moveRight":
                newCoords[1] += 1
            case _:
                print("DEBUG:'"+str(keyPress)+"' incorrect statement")
        
        print("old coords:"+str(self.coords[0])+" "+str(self.coords[1]))
        print("new coords:"+str(newCoords[0])+" "+str(newCoords[1]))
        
        if (self.__checkObstructMovement(newCoords) == False):
            self.coords = np.array(self.coords)
        else:
            self.coords = np.array(newCoords)
            self.newMapValue = self.currentMap[newCoords[0]][newCoords[1]]
        #checking for monster encounter
        self.__monsterEncounter(newCoords, self.mapEncounterOdds)
        
        #setting player on new position
        self.currentMap[self.coords[0]][self.coords[1]] = 50
        return

    def __monsterEncounter(self, coordstoparse, encounterodds):
        '''
        checks tiles that are monster passable, and allows for them to start combat
        '''
        objectToParse = self.currentMap[coordstoparse[0]][coordstoparse[1]]
        if(objectToParse == 2):
            if(dieroller.DieRoller.rollD100() < encounterodds):
                return True
        return False
    
    def __checkObstructMovement(self, coordstoparse):
        '''
        a boolean function to check whether the current object is not passable
        '''
        objectToParse = self.currentMap[coordstoparse[0]][coordstoparse[1]]
        match objectToParse:
            case 0:
                return False
            case 1 | 2:
                return True
            case 3 | 4:
                return False
            case 5:
                return True
            case 11:
                return False

        
        
        
    
    