class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        
        deq = deque([0])
        visited = set()
        
        while deq:
            for _ in range(len(deq)):
                room = deq.popleft()
                if room not in visited:
                    for keys in rooms[room]:
                        deq.append(keys)
                    
                    visited.add(room)
                    
        
        return len(visited) == len(rooms)
                    
                
        