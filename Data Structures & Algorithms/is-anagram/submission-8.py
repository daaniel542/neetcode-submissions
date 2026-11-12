class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False
    
        #hashmap
        string1 = {}
        string2 = {}
        
        for i in range(len(s)):
            string1[s[i]] = 1 + string1.get(s[i],0)
            string2[t[i]] = 1 + string2.get(t[i],0)
        
        for j in string1:
            if string1[j] != string2.get(j,0):
                return False
        
        return True



