class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        output = {}

        for index, value in enumerate(nums):
            difference = target - value
            if difference in output:
                return [output[difference], index] 
            output[value] = index
            
        
       
            