class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        
        def isSub(sub, sup):
            j = 0
            for i in range(len(sub)):
                while j < len(sup) and sup[j] != sub[i]:
                    j += 1                
                if j == len(sup):
                    return False
                j += 1
            return True
        
        
        words.sort(key = lambda x: len(x))
        dic = defaultdict(lambda: 1)
        ans = 1

        for i in range(len(words)):
            for j in range(i) :
                if isSub(words[j], words[i]) and len(words[i]) - len(words[j]) == 1 :
                    dic[words[i]] = max(dic[words[i]], dic[words[j]] + 1)  
                    ans = max(ans, dic[words[i]])
                    
        return ans 
        
