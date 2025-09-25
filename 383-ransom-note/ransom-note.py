class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:

        ransom =  Counter(ransomNote)
        mag =  Counter(magazine)

        for letter, count in ransom.items():
            if count > mag[letter]:
                return False

        return True