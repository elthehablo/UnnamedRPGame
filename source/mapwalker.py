import os

import mapmovement
import importer
import keyregistry
import drawmap

class MapWalker:
    '''
    a class that walks over a map and draws it every time when a new step is done
    the constructor creates a map using a specific string to import it
    then calling start initialises the map
    '''
    
    
    def __init__(self, mapName, startingCoords, mapEncounterOdds):
        self.startingcoords = startingCoords
        self.mapEncounterOdds = mapEncounterOdds
        importInstance = importer.ImportHandler("source/resources/maps/"+str(mapName))
        self.importedMap = importInstance.ImportMap()
    
    def start(self, runLength):
        '''
        starts movement on the map
        
        --arguments--
        runLength -- the amount of max turns that the map is being run on 
        
        --returns--
        none
        '''
        #clear screen first
        mapmover = mapmovement.MapMovement(self.importedMap, self.startingCoords, self.mapEncounterOdds)
        
        if(self.importedMap[self.startingCoords[0]][self.startingCoords[1]] == 1):
            self.importedMap[self.startingCoords[0]][self.startingCoords[1]] = 50 #set to player
        for i in range(runLength):
            os.system('cls')
            drawmap.DrawMap.PrettyDraw(self.importedMap)
            keyBeingPressed = keyregistry.KeyRegistry.keyPressed()
            mapmover.move(keyBeingPressed)
    
            
            
        
        
        