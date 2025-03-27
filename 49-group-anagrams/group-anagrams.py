class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        dic = defaultdict(list)

        for word in strs:
            temp = [0] * 26

            for l in word:
                temp[ord(l) - 97] += 1

            dic[tuple(temp)].append(word)

        return [dic[key] for key in dic ]

        