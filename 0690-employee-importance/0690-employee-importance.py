"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        
        dic = defaultdict(lambda:Employee(None, 0, []))
        
        for i in range(len(employees)):
            dic[employees[i].id] = employees[i] 

        def dfs(index):
            
            if not dic[index].subordinates:
                return dic[index].importance
            
            total = 0
            
            for idx in dic[index].subordinates:
                total += dfs(idx) 
          
            return total + dic[index].importance
            
        
        return dfs(id) 

            




























#         res = 0
        
#         def dfs(node):
#             nonlocal res
            
#             if not node.subordinates:
#                 return node.importance

                
#             total = node.importance 
#             for sub in node.subordinates:
#                 total += dfs(sub)
                
#             if node.id == id:
#                 res = total
                
#             return total
        
#         dfs(employees)
#         return res