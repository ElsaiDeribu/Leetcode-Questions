class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        self.bigCarSpaces = big
        self.mediumCarSpaces = medium
        self.smallCarSpaces = small
        
        
        

    def addCar(self, carType: int) -> bool:
        
        if carType == 1 and self.bigCarSpaces > 0:
            self.bigCarSpaces -= 1
            return True
        
        elif carType == 2 and self.mediumCarSpaces > 0:
            self.mediumCarSpaces -= 1
            return True
        elif carType == 3 and self.smallCarSpaces > 0:
            self.smallCarSpaces -= 1
            return True
        
        return False
            
        


# Your ParkingSystem object will be instantiated and called as such:
# obj = ParkingSystem(big, medium, small)
# param_1 = obj.addCar(carType)