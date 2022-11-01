class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        
        
        count = Counter(arr)
        sortedArr = []
        count = dict(sorted(count.items(), key = lambda x: x[1], reverse = True))
        
        for i in count:
            
            while count[i]:
                sortedArr.append(i)
                count[i] -= 1
        
        
        sortedArr = sortedArr[:len(sortedArr) - k]
        
        return len(set(sortedArr))
