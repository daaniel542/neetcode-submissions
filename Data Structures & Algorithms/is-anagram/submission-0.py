class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False
        # create 2 empty dicts
        string1 = {}
        string2 = {}

        # loop through s and save each char individually in the dict,    updating its value (count) if there are duplicated
        for c in s:
            if c in string1:
                string1[c] += 1
            else:
                string1[c] = 1
        
        # loop through t and save each char individually in the dict,    updating its value (count) if there are duplicated

        for c in t:
            if c in string2:
                string2[c] += 1
            else:
                string2[c] = 1

        # if the 2 dicts are the same, return true
        return string1 == string2
            
        
        


        