"""1480. Running Sum of 1d Array

URL: https://leetcode.com/problems/running-sum-of-1d-array/

## Description

Given an array `nums`. We define a running sum of an array as `runningSum[i] = sum(nums[0]…nums[i])`.
Return the running sum of `nums`.

cf. beginners guide

https://leetcode.com/explore/learn/card/the-leetcode-beginners-guide/692/challenge-problems/4422/

difficulty: Easy
"""

from itertools import accumulate
from typing import List


class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        return list(accumulate(nums))


class SolutionModelAnswer:
    """
    There are no official solution.
    """
    pass
