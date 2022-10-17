class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        
        count = Counter(students)
        
        
        i = j = 0
        
        
        while i < len(students):
            
            if students[i] == sandwiches[j]:
                count[students[i]] -= 1
                i += 1
                j += 1
                
                if i >= len(students):
                    return 0
                
            else:
                students.append(students[i])
                if count[sandwiches[j]] == 0:
                    return count[students[i]]
                
                i += 1
                
                
            
            
            
        