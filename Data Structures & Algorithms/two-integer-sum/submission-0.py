class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        # math: target - nums[smaller index = nums [larger index]
        # use a set data structure to check if nums [larger index] exists in the list

        prevMap = {}  # val -> index

        for index, value in enumerate(nums):
            diff = target - value
            if diff in prevMap:
                return [prevMap[diff], index]
            prevMap[value] = index

        


        