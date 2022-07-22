class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        listMagazine = list(magazine)

        for letter in ransomNote:
            if letter in listMagazine:
                listMagazine.remove(letter)
            else:
                return False
        return True