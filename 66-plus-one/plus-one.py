class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        rem = 0

        for i in range(len(digits) - 1, -1, -1):
            if i == len(digits) - 1 or rem:
                
                digits[i] += 1

                if digits[i] > 9:
                    digits[i] = 0
                    rem = 1
                else:
                    rem = 0

            else:
                return digits
                
        
        return [1] + digits if rem else digits