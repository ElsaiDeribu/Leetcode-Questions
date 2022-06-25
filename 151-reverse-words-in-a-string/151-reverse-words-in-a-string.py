class Solution:
    def reverseWords(self, s: str) -> str:
        
        myList2 = []
        myList = []
        t = ''
        ans = ''
        
        for i in s:
            t = t + i
            if i == " ":
                myList.append(t.strip())
                t = ''
        myList.append(t)
        myList = myList[::-1]
        
        print(myList)
        for i in myList:
            if i != "":
                myList2.append(i)
                
                
        
        myList2 =  " ".join(myList2)
        
        # print(myList2)
        
        return myList2
                
        
            
      