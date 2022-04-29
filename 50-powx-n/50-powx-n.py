class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        if x == 1:
            return x
        elif n > 0:
            if n == 1:
                return x
            elif n % 2 == 0:
                oneHalf = self.myPow(x, n/2) 
                return  oneHalf * oneHalf
            elif n % 2 != 0:
                n -= 1
                oneHalf = self.myPow(x, n/2) 
                return x * oneHalf * oneHalf
        elif n < 0:
            if n == -1:
                return 1/x
            elif n % 2 == 0:
                oneHalf = self.myPow(x, n/2) 
                return  oneHalf * oneHalf
            elif n % 2 != 0:
                n += 1
                oneHalf = self.myPow(x, n/2) 
                return 1/x *  oneHalf * oneHalf
            
