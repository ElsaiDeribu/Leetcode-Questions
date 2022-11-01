class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        
        sortedArr = []
        count = dict(sorted(Counter(arr).items(), key = lambda x: x[1], reverse = True))
        
        for i in count:
            while count[i]:
                sortedArr.append(i)
                count[i] -= 1
        
        return len(set(sortedArr[:len(sortedArr) - k]))
