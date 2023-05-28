import numpy as np
import os

class DrawMap:
    def PrettyDraw(currentMap):
        '''
        draws currentMap in a pretty way using a visual library
        
        TODO: we may want to use a txt file and the importer to draw later
        '''
        #clear screen first
        os.system('cls')
        N = np.size(currentMap, axis = 0)
        M = np.size(currentMap, axis = 1)
        
        for i in range(N):
            for j in range(M):
                if(currentMap[i][j] == 0):
                    print("X", end = '')
                elif(currentMap[i][j] == 1):
                    print(" ", end = '')
                elif(currentMap[i][j] == 50):
                    print('\x1b[6;30;42m' + 'O' + '\x1b[0m', end = '')
                else:
                    print(" ", end = '')
            print("")