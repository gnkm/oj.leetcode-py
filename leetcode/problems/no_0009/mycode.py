"""Palindrome Number - LeetCode
https://leetcode.com/problems/palindrome-number/

difficulty: Easy
"""

from typing import Dict, List, Union


# my code.
class Solution:
    def isPalindrome(self, x: int) -> bool:
        x_str = str(x)
        return x_str == x_str[-1::-1]


def main():
    sol = Solution()
    print(f"{sol.isPalindrome(121) = }")
    print(f"{sol.isPalindrome(-121) = }")
    print(f"{sol.isPalindrome(10) = }")
    print(f"{sol.isPalindrome(12321) = }")


if __name__ == "__main__":
    main()
