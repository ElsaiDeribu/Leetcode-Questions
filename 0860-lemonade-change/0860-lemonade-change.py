class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        
        five = 0
        ten = 0
        
        for bill in bills:
            if bill == 5:
                five += 1
                
            elif bill == 10:
                if five == 0:
                    return False
                else:
                    five -= 1
                    ten += 1
                    
            elif bill == 20:
                if (five == 0 or ten == 0) and (five < 3):
                    return False
                
                elif five >= 1 and ten >= 1:
                    five -= 1
                    ten -= 1
                    
                elif five >= 3:
                    five -= 3
                    
        
        return True
            
                    