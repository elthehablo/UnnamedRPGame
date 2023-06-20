import numpy as np

class ImportHandler:
    #IMPORTANT NOTE: imports and their paths are of course going to be 
    # heavily dependent on where the main executable is
    
    def __init__(self, dataPath):
        self.dataPath = dataPath
        print("Path stored as: '"+str(self.dataPath)+"'")

    def ImportAllCreatures(self):
        '''
        returns the full database for all creatures
        
        --arguments--
        none
        
        --returns--
        the full array of all creatures
        '''
        dataArray = np.loadtxt(self.dataPath, delimiter = ',', dtype={
        'names': ('id', 'name','level', 'hp', 'mp', 'str', 'dex', 'con', 'int', 'wis', 'char', 'exp', 'armorclass', 'hitdie', 'hitdiceamount', 'attackmodifier'),
        'formats': ('i4', 'S30','i4', 'i4', 'i4', 'i4', 'i4', 'i4', 'i4', 'i4', 'i4', 'i4', 'i4', 'S4', 'i4', 'i4')})

        return dataArray
    
    def ImportCreature(self, id):
        '''
        returns the full row of the creature at id
        
        --arguments--
        id -- id of the monster you want to obtain
        
        --returns--
        returns values of the specific monster of id
        
        '''
        dataArray = np.loadtxt(self.dataPath, delimiter = ',', dtype={
        'names': ('id', 'name','level', 'hp', 'mp', 'str', 'dex', 'con', 'int', 'wis', 'char', 'exp', 'armorclass', 'hitdie', 'hitdiceamount', 'attackmodifier'),
        'formats': ('i4', 'S30','i4', 'i4', 'i4', 'i4', 'i4', 'i4', 'i4', 'i4', 'i4', 'i4', 'i4', 'S4', 'i4', 'i4')})

        
        return dataArray[id]
    
    def ImportCreatureStat(self, id, valueId):
        '''
        returns the specific value of the column at column valueId for creature id
        
        note -- to get the string value from the imported tables you need to do *.decode('UTF-8')
        
        --arguments--
        id      -- id of the monster you want to obtain
        valueId -- specific stat you want to obtain (columnNR)
        
        --returns--
        returns specific stat at valueId of monster at id 
        '''
        
        dataArray = np.loadtxt(self.dataPath, delimiter = ',', dtype={
        'names': ('id', 'name','level', 'hp', 'mp', 'str', 'dex', 'con', 'int', 'wis', 'char', 'exp', 'armorclass', 'hitdie', 'hitdiceamount', 'attackmodifier'),
        'formats': ('i4', 'S30','i4', 'i4', 'i4', 'i4', 'i4', 'i4', 'i4', 'i4', 'i4', 'i4', 'i4', 'S4', 'i4', 'i4')})
       
        return dataArray[id][valueId]
    
    def ImportMap(self):
        '''
        returns a specific map to play on
        
        --arguments--
        none
        
        --returns--
        maps as 2x2 array with the path from the constructor
        '''
        
        dataArray = np.loadtxt(self.dataPath, delimiter = ',', dtype = 'i4')
        
        return dataArray    
        