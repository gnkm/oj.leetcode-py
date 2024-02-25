"""Split the Array - LeetCode Contest
https://leetcode.com/contest/weekly-contest-386/problems/split-the-array/
"""

from collections import Counter
from typing import List


class Solution:
    def isPossibleToSplit(self, nums: List[int]) -> bool:
        counter = Counter(nums)
        for v in counter.values():
            if v > 2:
                return False
        return True


def main():
    cases = [
        {"nums": [1, 1, 2, 2, 3, 4], "expected": True},
        {"nums": [1, 1, 1, 1], "expected": False},
    ]
    for case in cases:
        sol = Solution()
        assert sol.isPossibleToSplit(case["nums"]) == case["expected"]


if __name__ == "__main__":
    main()
