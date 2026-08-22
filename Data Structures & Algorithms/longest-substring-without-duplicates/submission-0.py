class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # create a hashmap of all the chars,
        # have a sliding window 
        # if the value of the key is larger than 1 then we will return false


        left = 0
        best = 0
        seen = set()
        for right in range(len(s)):
            while s[right] in seen:
                seen.remove(s[left])
                left += 1
            seen.add(s[right])
            best = max(best, right - left + 1)

        return best

            

        