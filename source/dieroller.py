import random

class DieRoller:
    # a class to simulate DND rolling mechanics
    @staticmethod
    def rollD4():
        return random.randint(1, 4)
        
    @staticmethod
    def rollD6():
        return random.randint(1, 6)
    
    @staticmethod
    def rollD10():
        return random.randint(1, 10)
    
    @staticmethod
    def rollD12():
        return random.randint(1, 12)
    
    @staticmethod
    def rollD20():
        return random.randint(1, 20)
    
    @staticmethod
    def rollD100():
        return random.randint(1, 100)
        return random.randint(1, 100)
        