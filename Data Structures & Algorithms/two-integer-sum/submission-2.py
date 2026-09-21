class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # nums[j] = target - nums[i], ValuesView

        prevMap = {}

        for i, values in enumerate(nums):
            diff = target - values
            if diff in prevMap:
                return [prevMap[diff], i]
            prevMap[values] = i


