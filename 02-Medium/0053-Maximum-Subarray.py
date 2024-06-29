# Link: https://leetcode.com/problems/maximum-subarray/
# Difficulty: Medium
# Description: Given an integer array nums, find the contiguous subarray
# (containing at least one number) which has the largest sum and return its sum.

from typing import List


class Solution:
    @staticmethod
    def maxSubArray(nums: List[int]) -> int:
        # Initialize the maximum sum and the current sum
        max_sum = current_sum = nums[0]
        # Continue the process until the end of the array
        for i in range(1, len(nums)):
            # Update the current sum
            current_sum = max(nums[i], current_sum + nums[i])
            # Update the maximum sum
            max_sum = max(max_sum, current_sum)
        return max_sum


# Unit Test: Input: nums = [-2,1,-3,4,-1,2,1,-5,4], Output: 6
assert Solution.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6

# Unit Test: Input: nums = [1], Output: 1
assert Solution.maxSubArray([1]) == 1

# Unit Test: Input: nums = [5,4,-1,7,8], Output: 23
assert Solution.maxSubArray([5, 4, -1, 7, 8]) == 23

print("All unit tests are passed")
