"""Minimum Operations to Exceed Threshold Value I - LeetCode Contest
https://leetcode.com/contest/biweekly-contest-125/problems/minimum-operations-to-exceed-threshold-value-i/"""

from typing import List


class Solution:
    def countPairsOfConnectableServers(
        self, edges: List[List[int]], signalSpeed: int
    ) -> List[int]:
        ret = []
        return ret


def main():
    solution = Solution()
    print(
        f"{solution.countPairsOfConnectableServers([[0, 6, 3], [6, 5, 3], [0, 3, 1], [3, 2, 7], [3, 1, 6], [3, 4, 2]], 3) = }"
    )
    print(
        f"{solution.countPairsOfConnectableServers([[0, 1, 1], [1, 2, 5], [2, 3, 13], [3, 4, 9], [4, 5, 2]], 1) = }"
    )


if __name__ == "__main__":
    main()
