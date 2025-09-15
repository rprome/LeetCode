from collections import Counter

class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        ransom_count = Counter(ransomNote)
        magazine_count = Counter(magazine)   

        for char, freq in ransom_count.items():
            if magazine_count[char] < freq:   
                return False
        return True
        