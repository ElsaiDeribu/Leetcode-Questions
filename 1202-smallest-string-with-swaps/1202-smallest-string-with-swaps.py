class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        
        s = list(s)
        ans = ["l"] * len(s)
        parent = {i:i for i in range(len(s))}
        
        def find(x):
            nonlocal parent
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x
        
        def union(x, y):
            nonlocal parent
            repX = find(x)
            repY = find(y)
            if repX == repY:
                return
      
            parent[repX] = repY
         
            
        for i in range(len(pairs)):
            letter1 = pairs[i][0]
            letter2 = pairs[i][1]
            union(letter1, letter2)
         
        combs = defaultdict(lambda:deque())
        
        for i in range(len(s)):
            combs[find(i)].append(i)
        
        for item in combs:
            combs[item] = deque(sorted(list(combs[item]), key = lambda x: s[x]))
            
        for i in range(len(s)):
            ans[i] = s[combs[find(i)].popleft()]
        
             
        return ''.join(ans)