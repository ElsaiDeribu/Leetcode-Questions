class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        
        count = defaultdict(int)
        adjList = defaultdict(list)
        deq = deque(supplies)
        order = []
        
        for i in range(len(ingredients)):
            for ing in ingredients[i]:
                adjList[ing].append(recipes[i])
                count[recipes[i]] += 1
                
        
        
        while deq:
            
            for i in range(len(deq)):
                pre = deq.popleft()
                
                for neighbour in adjList[pre]:
                    count[neighbour] -= 1
                    if count[neighbour] == 0:
                        deq.append(neighbour)
                        
                if pre in recipes:
                    order.append(pre)    
                
                
                
        return order
                        