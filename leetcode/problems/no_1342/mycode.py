"""1342. Number of Steps to Reduce a Number to Zero

URL: https://leetcode.com/problems/number-of-steps-to-reduce-a-number-to-zero/

## Description

Given an integer `num`, return the number of steps to reduce it to zero.
In one step, if the current number is even, you have to divide it by `2`, otherwise, you have to subtract `1` from it.

difficulty: Easy
"""

from typing import Dict, List, Union


# my code.
class Solution:
    def numberOfSteps(self, num: int) -> int:
        step_num = 0
        tmp_num = num
        while tmp_num > 0:
            if tmp_num % 2 == 0:
                tmp_num /= 2
            else:
                tmp_num -= 1
            step_num += 1

        return step_num


class SolutionModelAnswer:
    """
    There are no model answer.
    """

    pass
