"""Minimum Operations to Exceed Threshold Value I - LeetCode Contest
https://leetcode.com/contest/biweekly-contest-125/problems/minimum-operations-to-exceed-threshold-value-i/"""

from copy import deepcopy
from typing import List


class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        ret = 0
        operated_nums = deepcopy(nums)

        for i, _ in enumerate(nums):
            # print(min(operated_nums))
            print(f"{i = }, {operated_nums = }")
            if min(operated_nums) >= k:
                ret = i
                break
            if len(operated_nums) >= 2:
                x = min(operated_nums)
                operated_nums.remove(x)
                y = min(operated_nums)
                operated_nums.remove(y)
                # print(f"{x = }, {y = }")
                operated_nums.append(x * 2 + y)
            else:
                break
        return ret


def main():
    solution = Solution()
    print(f"{solution.minOperations([2, 11, 10, 1, 3], 10) = }")
    print(f"{solution.minOperations([1, 1, 2, 4, 9], 20) = }")
    print(f"{solution.minOperations([97, 73, 5, 78], 98) = }")
    print(
        f"{solution.minOperations([760340387,289254123,628299234,204198715,565672759,684967229,303459334,302262994,770720781,383343826,148523784,750183433,778902176,930418501,520286131,441750197,402643198,547480026,799770607,303114486,481644752,320289220,792197603,44751343,828179295,804048578,468569446,555743704,416141129,865011209,56010709,133835994,200083188,740956911,842527451,728469270,370323078,880010797,977376598,598070033,866374140,110775975,609860085], 377260496) = }"
    )


if __name__ == "__main__":
    main()
