class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

        dic = {
            "2":["a", "b", "c"],
            "3":["d", "e", "f"],
            "4":["g", "h", "i"],
            "5":["j", "k", "l"],
            "6":["m", "n", "o"],
            "7":["p", "q", "r","s"],
            "8":["t", "u","v"],
            "9":["w", "x","y","z"], 
        }

        ans = []

        def recur(idx, arr):

            if idx == len(digits):
                temp =''.join(arr)
                ans.append(temp) if temp else None
                return

            for l in dic[digits[idx]]:
                arr.append(l)
                recur(idx + 1, arr)
                arr.pop()

            
        recur(0, [])

        return ans








        