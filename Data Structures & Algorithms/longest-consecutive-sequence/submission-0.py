class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        numbers = set(nums)
        output = list()
        longest = 0


        for index in nums:
            if (index - 1) not in numbers:
                length = 0
                while (index + length in numbers):
                    length += 1
                longest = max(length,longest) 
        return longest



