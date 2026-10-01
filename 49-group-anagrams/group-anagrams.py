class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:

        group = defaultdict(list)


        for word in strs:

            key = [0] * 26

            for char in word:
                key[ord(char) - ord('a')] += 1

            group[tuple(key)].append(word)



        return [val for val in group.values()]
        