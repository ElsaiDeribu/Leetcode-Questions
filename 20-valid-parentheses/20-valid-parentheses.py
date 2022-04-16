class Solution:
    def isValid(self, s: str) -> bool:
        class Stack:
            def __init__(self):
                self.st = []
            def push(self, x ):
                self.st.append(x)
            def pop(self):
                if len(self.st) > 0:
                    self.st.pop()
            def top(self):
                if len(self.st) == 0:
                    return None
                return self.st[-1]
            def print(self):
                print(self.st)
            def length(self):
                return len(self.st)

        dic = {'(' : ')', '{': '}', '[' :']'}
        st = Stack()
        for i in s:
            if i in dic.keys():
                st.push(i)
   
            
            else:
                if st.length() != 0:
                    if (dic[st.top()] == i):
                        st.pop()
                    else:
                        return False
                else:
                    return False
                
        if st.length() != 0:
            return False
        
        return True   
