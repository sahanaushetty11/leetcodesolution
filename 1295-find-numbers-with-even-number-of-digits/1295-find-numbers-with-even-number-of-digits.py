class Solution:
    def findNumbers(self, nums: list[int]) -> int:
        count = 0

        for i in range(len(nums)):
            digits = len(str(nums[i]))

            if digits % 2 == 0:
                count += 1

        return count

        