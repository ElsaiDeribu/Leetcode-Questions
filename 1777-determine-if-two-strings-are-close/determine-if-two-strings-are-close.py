class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:

        count1 = Counter(word1)
        count2 = Counter(word2)

        if count1 == count2:
            return True

        count1_keys = sorted(count1.keys())
        count2_keys = sorted(count2.keys())

        count1_values = sorted(count1.values())
        count2_values = sorted(count2.values())



        if count1_keys == count2_keys and count1_values == count2_values:
            return True

        return False