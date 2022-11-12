class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        
        
#         count = defaultdict(int)
#         ans  = 1000
        
#         for i in range(k):
#             count[blocks[i]] += 1
            
#         r = i
#         l = 0
        
#         while r < len(blocks):
#             ans = min(ans, count['W'])
#             count[blocks[l]] -= 1
#             l += 1
#             r += 1
#             if r < len(blocks):
#                 count[blocks[r]] += 1

#         return ans

        l = 0
        windowCount = 0
        minWinCount = 10**6

        for i in range(k):
            if blocks[i] == 'W':
                windowCount += 1
        r = i

        minWinCount = min(minWinCount, windowCount)

        while r < len(blocks):
            r += 1
            if r < len(blocks) and blocks[r] == 'W':
                windowCount += 1

            if blocks[l] == 'W':
                windowCount -= 1
            l += 1

            if r < len(blocks):
                minWinCount = min(minWinCount, windowCount)

        return minWinCount


        