"""13. Roman to Integer - LeetCode
https://leetcode.com/problems/roman-to-integer/description/

difficulty: Easy
"""

import sys
from typing import Dict, List, Union

symbol_values = {
    "I": 1,
    "IV": 4,
    "V": 5,
    "IX": 9,
    "X": 10,
    "XL": 40,
    "L": 50,
    "XC": 90,
    "C": 100,
    "CD": 400,
    "D": 500,
    "CM": 900,
    "M": 1000,
}


# my code.
class Solution:
    def romanToInt(self, s: str) -> int:
        if s == "":
            return 0
        sorted_symbol_values = sorted(
            symbol_values.items(), key=lambda x: x[1], reverse=True
        )
        for symbol, value in sorted_symbol_values:
            if s.startswith(symbol):
                return value + self.romanToInt(s[len(symbol) :])


class SolutionModelAnswer:
    """
    {URL}
    """

    pass


def main():
    solution = Solution()
    assert solution.romanToInt("III") == 3
    assert solution.romanToInt("LVIII") == 58
    assert solution.romanToInt("MCMXCIV") == 1994
    sys.exit()


if __name__ == "__main__":
    main()
