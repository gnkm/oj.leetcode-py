"""2389. Longest Subsequence With Limited Sum

URL: https://leetcode.com/problems/longest-subsequence-with-limited-sum/

## Description

You are given an integer array nums of length n, and an integer array queries of length m.

Return an array answer of length m where answer[i] is the maximum size of a subsequence that you can take from nums such that the sum of its elements is less than or equal to queries[i].

A subsequence is an array that can be derived from another array by deleting some or no elements without changing the order of the remaining elements.

difficulty: Easy
"""

from itertools import accumulate, takewhile
from typing import Dict, List, Union


# my code.
class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        answer = []
        nums.sort()
        for query in queries:
            size = len(list(takewhile(lambda x: x <= query, accumulate(nums))))
            answer.append(size)

        return answer


class SolutionModelAnswer:
    """
    {URL}
    """

    pass


if __name__ == "__main__":
    import pkg_resources

    if any([str(i).startswith("icecream") for i in pkg_resources.working_set]):
        import icecream

        _debug = icecream.ic
    else:
        _debug = print

    global debug
    debug = _debug
