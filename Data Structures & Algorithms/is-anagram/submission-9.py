class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # key value pairing where string is the key and the count is the value

        string1 = {}
        string2 = {}

        for i in s:
            if i in string1:
                string1[i] += 1
            else: string1[i] = 1
        
        for j in t:
            if j in string2:
                string2[j] += 1
            else: string2[j] = 1

        return string1 == string2

            
