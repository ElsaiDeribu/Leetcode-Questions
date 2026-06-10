class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
           
        group = defaultdict(list)

        for word in strs:

            chrs = [0] * 26
            for c in word:
                chrs[ord(c) - 97] += 1

            group[tuple(chrs)].append(word)


        return list(group.values())

        