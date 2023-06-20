import numpy as np
import os

class DrawMap:
    def PrettyDraw(currentMap):
        '''
        draws currentMap in a pretty way using a visual library
        
        --arguments--
        currentMap -- the current map in a format with integer values to represent the different tiles
        
        --returns--
        none
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
                elif(currentMap[i][j] == 2):
                    print(" ", end = '')
                elif(currentMap[i][j] == 3):
                    print('\x1b[6;30;42m' + 'Y' + '\x1b[0m', end = '')
                elif(currentMap[i][j] == 4):
                    print('\x1b[6;30;43m' + 'Y' + '\x1b[0m', end = '')
                elif(currentMap[i][j] == 5):
                    print('\x1b[6;30;42m' + '*' + '\x1b[0m', end = '')
                elif(currentMap[i][j] == 11):
                    print('\x1b[0;30;44m' + '~' + '\x1b[0m', end = '')
                elif(currentMap[i][j] == 50):
                    print('\x1b[6;30;42m' + 'O' + '\x1b[0m', end = '')
                else:
                    print(" ", end = '')
            print("")