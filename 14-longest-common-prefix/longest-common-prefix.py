class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        common = []

        for s in range(len(strs[0])):
            common.append(strs[0][s])
            for i in range(1, len(strs)):

                if len(strs[i]) < s + 1 :
                    common.pop()
                    return ''.join(common)

                elif common[-1] != strs[i][s]:
                    common.pop()
                    return ''.join(common)


        return ''.join(common)


            

        