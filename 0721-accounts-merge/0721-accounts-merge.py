class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        
        parent = {}
        
        def find(x):
            nonlocal parent
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x
        
        def union(x, y):
            repX = find(x)
            repY = find(y)
            if repX == repY:
                return
            parent[repX] = repY
                
        
        membership = defaultdict(lambda:set())
        edgeList = []
        
        for i in range(len(accounts)):
            parent[i] = i
            for j in range(1, len(accounts[i])):
                parent[accounts[i][j]] = i 
                membership[accounts[i][j]].add(i)
                
        for item in membership:
            if len(membership[item]) > 1:
                edgeList.append(list(membership[item]))
                
                
        for i in range(len(edgeList)):
            for j in range(1, len(edgeList[i])):
                union(edgeList[i][j - 1], edgeList[i][j]) 
                
        res = defaultdict(lambda:set())
        ans = []
        
        for i in range(len(accounts)):
            for j in range(1, len(accounts[i])):
                res[find(accounts[i][j])].add(accounts[i][j])
                
        for item in res:
            temp = []
            temp.append(accounts[item][0])
            temp.extend(list(sorted(res[item])))
            ans.append(temp)
            
        return ans
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         for j in range(len(accounts)):
#             temp = []
#             parent[j] = j
#             for i in range(1, len(accounts[j])):
#                 parent[(accounts[j][i], accounts[j][0])] = j
#                 size[(accounts[j][i], accounts[j][0])] = 1
#                 temp.append((accounts[j][i], accounts[j][0]))
#                 acc3.append((accounts[j][i], accounts[j][0]))
                
#             acc2.append(temp)
            
            
#         def find(x):
#             nonlocal parent
            
#             while parent[x] != x:
#                 parent[x] = parent[parent[x]]
#                 x = parent[x]
                
#             return x
        
        
#         def union(x, y):
#             nonlocal parent
#             repX = find(x)
#             repY = find(y)
            
#             if repX == repY:
#                 return
            
#             if size[repX] > size[repY]:
#                 parent[repY] = repX
#             else:
#                 parent[repX] = repY
            
            
# #         for acc in acc2:
# #             for i in range(1, len(acc)):
# #                 union(acc[i - 1], acc[i])
               
#         for i in range(len(acc3)):
#             for j in range(i + 1, len(acc3)):
#                 if acc3[i] == acc3[j]:
#                     union(acc3[i], acc3[j])
                    
#         res = defaultdict(lambda:set())  
#         ans = []
        
#         for i in range(len(acc3)):
#             rep = find(acc3[i])
#             res[rep].add(acc3[i][0])
                    
#         for item in res:
#             temp = []
#             temp.append(accounts[item][0])
#             temp.extend(sorted(list(res[item])))
#             ans.append(temp)
            
#         print(ans)    
#         return ans
        
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
        