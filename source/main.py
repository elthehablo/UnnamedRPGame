import numpy as np

import importer
import mapmovement
import keyregistry

##testmap####

mapOne = np.array(
    [[0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 1, 1, 1, 1, 1, 1, 1, 0],
     [0, 1, 1, 1, 1, 1, 1, 1, 0],
     [0, 1, 1, 1, 1, 1, 1, 1, 0],
     [0, 1, 1, 1, 1, 1, 1, 1, 0],
     [0, 1, 1, 1, 1, 1, 1, 1, 0],
     [0, 1, 1, 1, 1, 1, 1, 1, 0],
     [0, 1, 1, 1, 1, 1, 1, 1, 0],
     [0, 1, 1, 1, 1, 1, 1, 1, 0]]
)


#############

def main():
    #TODO: code to execute main program
    pathing = importer.ImportHandler("source/resources/creatures.txt")
    newarray = pathing.ImportAllCreatures()
    value = pathing.ImportCreatureStat(0, 1)
    print(newarray)
    print("value is: "+value.decode('UTF-8'))
    
    mapmover = mapmovement.MapMovement(mapOne, [3, 2])
    for i in range(10):
        keyBeingPressed = keyregistry.KeyRegistry.keyPressed()
        mapmover.move(keyBeingPressed)
    return

if __name__ == "__main__":
    main()