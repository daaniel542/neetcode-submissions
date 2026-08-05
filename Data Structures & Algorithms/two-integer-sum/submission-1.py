class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Initialize our hashmap to store {number: index}
        hashmap = {}
        
        # enumerate gives us both the index (i) and the value (num)
        for i, num in enumerate(nums):
            difference = target - num
            
            # Check if the difference is already a key in our hashmap
            if difference in hashmap:
                # If it is, return the index of the difference, and our current index
                return [hashmap[difference], i]
            
            # If not, add the current number and its index to the hashmap for future checks
            hashmap[num] = i