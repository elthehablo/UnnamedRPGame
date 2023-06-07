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
    
    
    def __init__(self, mapname, startingcoords, mapEncounterOdds):
        self.startingcoords = startingcoords
        self.mapEncounterOdds = mapEncounterOdds
        importInstance = importer.ImportHandler("source/resources/maps/"+str(mapname))
        self.importedmap = importInstance.ImportMap()
    
    def start(self, runlength):
        #initialise mapmover
        mapmover = mapmovement.MapMovement(self.importedmap, self.startingcoords, self.mapEncounterOdds)
        
        if(self.importedmap[self.startingcoords[0]][self.startingcoords[1]] == 1):
            self.importedmap[self.startingcoords[0]][self.startingcoords[1]] = 50 #set to player
        for i in range(runlength):
            os.system('cls')
            drawmap.DrawMap.PrettyDraw(self.importedmap)
            keyBeingPressed = keyregistry.KeyRegistry.keyPressed()
            mapmover.move(keyBeingPressed)
    
            
            
        
        
        