class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        
        positionTimePair = defaultdict(int)
        
        for i in range(len(position)):
            
            positionTimePair[position[i]] = (target - position[i])/ speed[i]
            
        positionTimePair = sorted(positionTimePair.items(), key = lambda x: x[0])
        
        st = []
        
        
        for i in range(len(positionTimePair)):
            
            while st and st[-1][1] <= positionTimePair[i][1]:
                st.pop()
            
            st.append(positionTimePair[i])
            
            
        return len(st)