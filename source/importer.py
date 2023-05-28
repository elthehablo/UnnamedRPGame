import numpy as np

class ImportHandler: 
    def __init__(self, dataPath):
        self.dataPath = dataPath
        print("Path stored as: '"+str(self.dataPath)+"'")

    def ImportAllCreatures(self):
        '''
        returns the full database for all creatures
        '''
        dataArray = np.loadtxt(self.dataPath, delimiter = ',', dtype={
        'names': ('id', 'name', 'hp', 'mp', 'str', 'dex', 'con', 'int', 'wis', 'char', 'exp'),
        'formats': ('i4', 'S30', 'i4', 'i4', 'i4', 'i4', 'i4', 'i4', 'i4', 'i4', 'i4')})

        return dataArray
    
    def ImportCreature(self, id):
        '''
        returns the full row of the creature at id
        '''
        dataArray = np.loadtxt(self.dataPath, delimiter = ',', dtype={
        'names': ('id', 'name', 'hp', 'mp', 'str', 'dex', 'con', 'int', 'wis', 'char', 'exp'),
        'formats': ('i4', 'S30', 'i4', 'i4', 'i4', 'i4', 'i4', 'i4', 'i4', 'i4', 'i4')})

        
        return dataArray[id]
    
    def ImportCreatureStat(self, id, valueId):
        '''
        returns the specific value of the column at column valueId for creature id
        '''
        
        dataArray = np.loadtxt(self.dataPath, delimiter = ',', dtype={
        'names': ('id', 'name', 'hp', 'mp', 'str', 'dex', 'con', 'int', 'wis', 'char', 'exp'),
        'formats': ('i4', 'S30', 'i4', 'i4', 'i4', 'i4', 'i4', 'i4', 'i4', 'i4', 'i4')})
       
        return dataArray[id][valueId]
    
    def ImportMap(self):
        '''
        returns a specific map to play on
        '''
        
        dataArray = np.loadtxt(self.dataPath, delimiter = ',', dtype = 'i4')
        
        return dataArray    
        