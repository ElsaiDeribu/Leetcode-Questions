class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        
        dic = defaultdict(list)
        ans = []
        
        def getpath(string):
            
            string = string.split()
            path = string[0]
            
            for i in range(1, len(string)):
                temp = string[i].split('(')
                dic[temp[-1][:-1]].append(path + "/" + temp[0])
                
         
        for path in paths:
            getpath(path)
        
        for item in dic:
            ans.append(dic[item]) if len(dic[item]) > 1 else None
            
        return ans