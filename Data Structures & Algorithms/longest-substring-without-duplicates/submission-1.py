class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
    # using a sliding window define the longest substring
    # the substring length will be determined if there is a duplicate, if there is a duplicate, pop from the left of the substring and continue checking
        # you can save, add and pop these chars from the substring using a set dsa to keep track of what the chars already found in the substring


        left = 0
        best = 0
        seen = set()
        for right in range(len(s)):
            # if the i'th char is in the string
                # pop the first appearance of the char and keep the current one, the move our left pointer and update our window
            while s[right] in seen:
                seen.remove(s[left])
                left += 1
            # if the char is not in seen then add it into seen
            seen.add(s[right])
            # the longest sequence is the window we have saved with the longest sequence
            best = max(best, right - left + 1)

        return best

            

        