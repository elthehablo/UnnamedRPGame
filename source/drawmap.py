import numpy as np

class DrawMap:
    def PrettyDraw(currentMap):
        '''
        draws currentMap in a pretty way using a visual library
        '''
        N = np.size(currentMap, axis = 0)
        M = np.size(currentMap, axis = 1)
        
        for i in range(N):
            for j in range(M):
                if(currentMap[i][j] == 0):
                    print("X", end = '')
                elif(currentMap[i][j] == 1):
                    print(" ", end = '')
                elif(currentMap[i][j] == 50):
                    print("O", end = '')
                else:
                    print(" ", end = '')
            print("")