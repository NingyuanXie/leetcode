"""696. Count Binary Substrings
Link: https://leetcode.com/problems/count-binary-substrings/
Difficulty: Easy
Description: Give a string s, count the number of non-empty (contiguous) substrings that have
the same number of 0's and 1's, and all the 0's and all the 1's in these substrings are
grouped consecutively."""


class Solution:
    @staticmethod
    def countBinarySubstrings(s: str) -> int:
        """Optimal Solution: Two Pointers. Time Complexity: O(n), Space Complexity: O(1).
           For a sequence like 0011, both 0 and 1 groups are of length 2. Thus, two valid substrings
           can be formed: 01 and 0011. Similarly, for 1100, the valid substrings are 10 and 1100"""
        # Initialize the count and the previous count
        count, prev_count = 0, 0
        # Initialize the two pointers
        i, j = 0, 0

        # Iterate through the string
        while i < len(s):
            # Count the number of consecutive 0's and 1's; stops whenever the character changes
            while j < len(s) and s[j] == s[i]:
                j += 1
            # Count the number of valid substrings, which is the minimal value between:
            # prev_count = length of the previous group; j - i = length of the current group
            count += min(prev_count, j - i)
            # Update the previous count (initially at 0)
            prev_count = j - i
            # Update the two pointers and move on to the next group
            i = j

        return count


# Unit Test: Input: s = "00110011", Output: 6
assert Solution.countBinarySubstrings("00110011") == 6

# Unit Test: Input: s = "10101", Output: 4
assert Solution.countBinarySubstrings("10101") == 4

print("All unit tests are passed")
