class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        
        ranking = []
        ans = []
        
        for i in range(len(mat)):
            soldiers = Counter(mat[i])[1]
            
            ranking.append((soldiers,i))
        
        ranking.sort()

        for i in range(k):
            ans.append(ranking[i][1])
            
        return ans
        
        
            
        