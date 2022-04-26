class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort()
        lastNumberIndex = len(citations)-1
        hIndex = citations[0]
        if len(citations) == 1:
            if citations[0] == 0:
                return 0
            return 1
        for i in range(len(citations)):
            if citations[i] == (lastNumberIndex - i + 1):
                hIndex = citations[i]
                
            elif citations[i] < (lastNumberIndex - i + 1):
                continue
            

            while citations[i] > (lastNumberIndex - i + 1):
                citations[i] -= 1
            return citations[i]
        
        return hIndex
        