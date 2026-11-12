class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # key value pairing where string is the key and the count is the value

    #string1[i] accesses the value associated with key i.    
    #i in string1 checks whether i exists as a key, not a value.

        string1 = {}
        string2 = {}

        # loop through the s string and create an key-value pair in string1
            # if there is already a key then increment it
            # otherwise create the key and give it value 1
        for i in s:
            if i in string1:
                string1[i] += 1
            else: string1[i] = 1

        # loop through the s string and create an key-value pair in string1
            # if there is already a key then increment it
            # otherwise create the key and give it value 1
        for j in t:
            if j in string2:
                string2[j] += 1
            else: string2[j] = 1

        # check if string1 and string2 are the same length
        return string1 == string2

            
