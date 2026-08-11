class Solution:
    # struggles:
    # how to return output, list of lists?

    # store each str's specific characters into a dictionary and cross check it with the array of alphabet chars

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # mapping charCount to the list of Anagrams
        # deafultdict(List): dict of lists, if none exisiting list create new one, else just append to the list
        result = defaultdict(list) 
        for string in strs:
            # before you investigate the count of a string, 
            # the count should be 0 for all 26 chars
            alphaCount = [0]*26 
    
            for character in string: 
                #now we are looping the individual string's characters
                # gets the ascii of the character so basically this line updates 
                # the count for the char that is present in string at each looping iteration  
                alphaCount [ord(character) - ord('a')] += 1 

            # add this into our dictionary of lists so we can get groupings for the anagrams, 
            # based on the character specific count
            # 
            result[tuple(alphaCount)].append(string)
        return list(result.values())

        

