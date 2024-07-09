# Link: https://leetcode.com/problems/intersection-of-two-arrays-ii/
# Difficulty: Easy
# Description: Given two integer arrays nums1 and nums2, return an array of their intersection.
# Each element in the result should appear as many times as it shows in both arrays,
# and you may return the result in any order.

from typing import List


class Solution:
    # Optimal Solution: Hash Table. Time Complexity: O(n + m), Space Complexity: O(n)
    # Similar to 0242-Valid-Anagram.py and 0349-Intersection-of-Two-Arrays.py
    @staticmethod
    def intersect(nums1: List[int], nums2: List[int]) -> List[int]:
        # Initialize a hash table to store the frequency of each element in nums1
        freq = {}
        # Loop through each element in nums1
        for num in nums1:
            # Increment the frequency of the element in the hash table
            freq[num] = freq.get(num, 0) + 1  # E.g., freq = {1: 2, 2: 2}
        # Initialize a list to store the intersection of nums1 and nums2
        intersection = []
        # Loop through each element in nums2
        for num in nums2:
            # If the element is in the hash table and the frequency is greater than 0
            if num in freq and freq[num] > 0:
                # Add the element to the intersection
                intersection.append(num)
                # Decrement the frequency of the element in the hash table to avoid duplicates
                freq[num] -= 1
        return intersection


# Unit Test: Input: nums1 = [1, 2, 2, 1], nums2 = [2, 2], Output: [2, 2]
assert Solution.intersect([1, 2, 2, 1], [2, 2]) == [2, 2]

# Unit Test: Input: nums1 = [4, 9, 5], nums2 = [9, 4, 9, 8, 4], Output: [9, 4]
assert Solution.intersect([4, 9, 5], [9, 4, 9, 8, 4]) == [9, 4]

print("All unit tests are passed")
