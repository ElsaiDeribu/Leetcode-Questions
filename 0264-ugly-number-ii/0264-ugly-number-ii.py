class Solution:
    def nthUglyNumber(self, n: int) -> int:
        
#         theInteger = []
        
#         factor2 = []
#         factor3 = []
#         factor5 = []
        
#         heappush(factor2, 2)
#         heappush(factor3, 3)
#         heappush(factor5, 5)
#         heappush(theInteger, 1)
        
#         while len(theInteger) < n:
            
#             minOfThree = min(factor2[0], factor3[0], factor5[0])
            
#             heappush(theInteger, minOfThree)
#             heappush(factor2, -2 * minOfThree)
#             heappush(factor3, -3 * minOfThree)
#             heappush(factor5, -5 * minOfThree)
        
#         print(factor2, factor3, factor5)
        # print(n)
        mul = [2,3,5]
        vstd = set()
        heap = []
        heapq.heappush(heap,1)
        while n:
            curr = heapq.heappop(heap)
            for i in mul:
                if curr * i not in vstd:
                    vstd.add(curr*i)
                    heapq.heappush(heap,curr*i)
            n -= 1
        return curr
            
            
            
            
        
        
        
  