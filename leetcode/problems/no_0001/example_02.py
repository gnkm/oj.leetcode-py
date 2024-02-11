# https://leetcode.com/problems/two-sum/solutions/3619262/3-method-s-c-java-python-beginner-friendly
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Build the hash table
        num_map = {num: i for i, num in enumerate(nums)}

        # Find the complement
        for i, num in enumerate(nums):
            complement = target - num
            if complement in num_map and num_map[complement] != i:
                return [i, num_map[complement]]

        return []  # No solution found
