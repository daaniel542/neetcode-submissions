class Solution:
    def isPalindrome(self, s: str) -> bool:
        # convert string into lowercase
        # remove all whitespace in between characters
        # left and right pointer, and each time compare if they are the same char, if not then return false
        
        cleaned = "".join(char.lower() for char in s if char.isalnum())

        left = 0
        right = len(cleaned) - 1

        # use compare of left and right because for loop pointers will cross each other, you dont wanna cross
        while left < right:
            if cleaned[left] != cleaned[right]:
                return False

            left += 1
            right -= 1

        return True