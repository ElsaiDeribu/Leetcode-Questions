class Solution:
    def findTheWinner(self, n: int, k: int) -> int:

        deq = deque()

        for i in range(1, n + 1):
            deq.append(i)

        count = k 
        while len(deq) > 1:
            if count == 1:
                deq.popleft() 
                count = k
            else:
                deq.append(deq.popleft())
                count -= 1


        return deq[0]
                
            





        