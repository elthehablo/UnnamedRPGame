import numpy as np

import importer
import mapmovement
import keyregistry
import drawmap

##testmap####

mapOne = np.array(
    [[0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 1, 1, 1, 1, 1, 1, 1, 0],
     [0, 1, 0, 1, 1, 0, 0, 1, 0],
     [0, 1, 1, 1, 1, 1, 1, 1, 0],
     [0, 1, 0, 1, 1, 1, 1, 1, 0],
     [0, 1, 0, 1, 1, 0, 1, 1, 0],
     [0, 0, 0, 1, 1, 1, 1, 1, 0],
     [0, 1, 0, 1, 1, 1, 1, 1, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0]]
)


#############

def main():
    #TODO: code to execute main program
    pathing = importer.ImportHandler("source/resources/creatures.txt")
    newarray = pathing.ImportAllCreatures()
    value = pathing.ImportCreatureStat(0, 1)
    print(newarray)
    print("value is: "+value.decode('UTF-8'))
    
    mapOne[3][2] = 50
    
    mapTwoPath = importer.ImportHandler("source/resources/maps/map0.txt")
    mapTwo = mapTwoPath.ImportMap()
    mapmover = mapmovement.MapMovement(mapTwo, [3, 2])
    for i in range(25):
        keyBeingPressed = keyregistry.KeyRegistry.keyPressed()
        mapmover.move(keyBeingPressed)
        drawmap.DrawMap.PrettyDraw(mapTwo)
    return

if __name__ == "__main__":
    main()