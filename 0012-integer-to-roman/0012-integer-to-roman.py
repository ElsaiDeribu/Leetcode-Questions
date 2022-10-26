class Solution:
    def intToRoman(self, num: int) -> str:
        
        dic1 = {1:"I", 2:"II", 3:"III", 4:"IV", 5:"V", 6:"VI", 7:"VII", 8:"VIII", 9:"IX" }
        dic2 = {1:"X",2:"XX", 3:"XXX", 4:"XL", 5:"L", 6:"LX", 7:"LXX", 8:"LXXX", 9:"XC"}
        dic3 = {1:"C",2:"CC", 3:"CCC", 4:"CD", 5:"D", 6:"DC", 7:"DCC", 8:"DCCC", 9:"CM"}
        dic4 = {1:"M", 2:"MM", 3:"MMM"}
        ans = []
        num = str(num)
        
        if len(num) == 1:
            return dic1[int(num[0])]
            
        elif len(num) == 2:
            for i in range(len(num) - 1, -1, -1 ) :
                if num[i] == "0":
                    continue
                    
                if i == 1:
                    ans.append(dic1[int(num[i])])
                elif i == 0:
                    ans.append(dic2[int(num[i])]) 
                    
        elif len(num) == 3:
            for i in range(len(num) - 1, -1, -1 ) :
                if num[i] == "0":
                    continue
                if i == 2:
                    ans.append(dic1[int(num[i])])
                elif i == 1:
                    ans.append(dic2[int(num[i])])
                elif i == 0:
                    ans.append(dic3[int(num[i])]) 
            
        elif len(num) == 4:
            
            for i in range(len(num) - 1, -1, -1 ) :
                if num[i] == "0":
                    continue
                if i == 3:
                    ans.append(dic1[int(num[i])])
                elif i == 2:
                    ans.append(dic2[int(num[i])])
                elif i == 1:
                    ans.append(dic3[int(num[i])])
                elif i == 0:
                    ans.append(dic4[int(num[i])]) 
                    
                
        ans.reverse()       
                
        return ''.join(ans)