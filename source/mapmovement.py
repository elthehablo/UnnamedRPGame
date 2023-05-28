import numpy as np

class MapMovement:
    def __init__(self, currentMap, coords):
        self.currentMap = currentMap
        self.coords = coords
    
    def move(self, keyPress):
        '''
        takes the current map and moves character as long as there is open space
        
        return -- void (movement is done by manipulating self.coords and self.currentMap)
        '''
        #setting old position to open space
        self.currentMap[self.coords[0]][self.coords[1]] = 1
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
        
        if (self.currentMap[newCoords[0]][newCoords[1]] == 0):
            self.coords = np.array(self.coords)
            
        elif (self.currentMap[newCoords[0]][newCoords[1]] == 1):
            self.coords = np.array(newCoords)
        #setting player on new position
        self.currentMap[self.coords[0]][self.coords[1]] = 50
        return
        
    
    