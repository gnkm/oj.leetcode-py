"""412. Fizz Buzz

URL: https://leetcode.com/problems/fizz-buzz/

## Description

Given an integer n, return a string array answer (1-indexed) where:

- `answer[i] == "FizzBuzz"` if `i` is divisible by 3 and 5.
- `answer[i] == "Fizz"` if `i` is divisible by 3.
- `answer[i] == "Buzz"` if `i` is divisible by 5.
- `answer[i] == i` (as a string) if none of the above conditions are true.

difficulty: Easy
"""

from typing import Dict, List, Union


# my code.
class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        ret = []
        for i in range(1, n + 1):
            if i % 3 == 0 and i % 5 == 0:
                appended = "FizzBuzz"
            elif i % 3 == 0:
                appended = "Fizz"
            elif i % 5 == 0:
                appended = "Buzz"
            else:
                appended = str(i)

            ret.append(appended)

        return ret


class SolutionModelAnswer:
    """
    {URL}
    """
    pass
