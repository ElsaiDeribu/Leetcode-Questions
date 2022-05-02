class Solution:
    def kthGrammar(self, n, k):
        k -= 1
        
        def recursive(n, k):
            if n == 1:
                return 0
            if not k % 2:
                return recursive(n-1, k//2)

            else: 
                if recursive(n-1, k//2) == 0:
                    return 1
                elif recursive(n-1, k//2) == 1:
                    return 0
            return 0
        
        return recursive(n, k)
            

    #         0     N=1
    #    0        1  N=2
    #   0 1       1  0  N=3
    # 01  10     10   01  N=4