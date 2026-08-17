class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()

        for index, value in enumerate(nums):

            # skip duplicate starting values
            if index > 0 and value == nums[index - 1]:
                continue

            left = index + 1
            right = len(nums) - 1

            while left < right:
                total = value + nums[left] + nums[right]

                if total > 0:
                    right -= 1

                elif total < 0:
                    left += 1

                else:
                    result.append([value, nums[left], nums[right]])

                    left += 1

                    # skip duplicate left values
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1

        return result