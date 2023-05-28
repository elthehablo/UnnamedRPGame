import numpy as np


import importer
import mapmovement
import keyregistry
import drawmap
import menu

def main():
    #TODO: code to execute main program   
    mapTwoPath = importer.ImportHandler("source/resources/maps/map0.txt")
    mapTwo = mapTwoPath.ImportMap()
    mapmover = mapmovement.MapMovement(mapTwo, [3, 2])
    for i in range(5):
        keyBeingPressed = keyregistry.KeyRegistry.keyPressed()
        mapmover.move(keyBeingPressed)
        drawmap.DrawMap.PrettyDraw(mapTwo)
    
    newmenu = menu.Menu(False, True)
    newmenu.start()
    return

if __name__ == "__main__":
    main()