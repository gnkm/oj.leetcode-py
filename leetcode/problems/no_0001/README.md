# 0001 Two Sum

## コード

```python
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
```

sample inputs

```python
cases = [
    {"nums": [2, 7, 11, 15], "target": 9, "expected": [0, 1]},
    {"nums": [3, 2, 4], "target": 6, "expected": [1, 2]},
    {"nums": [3, 3,], "target": 6, "expected": [0, 1]},
]
```

## 解説

`nums` の各数に対して、足して `target` になる数が `nums` にあれば、その index が回答になる。

2 番目のケースで考える。

`num_map` は `{3: 0, 2: 1, 4: 2}`。

### loop 1: `i = 0, num = 3, complement = 3`。

`3 in nums` は `True` なのだが、同じ数の和は除くという条件がある。
それが `num_map[complement] != i` という部分で、
`num_map[3]` は `0` なので `num_map[complement] != i` は `False`。
したがって、この組み合わせは回答にはならない。

### loop 2: `i = 1, num = 2, complement = 4`。

`4 in nums` は `True`。
`num_map[4]` は `2` なので `num_map[complement] != i` は `True`。
したがって `[1, 2]` が回答である。
確かに `nums[1] + nums[2]` = 2 + 4 = 6 である。

## URL

[Two Sum - LeetCode](https://leetcode.com/problems/two-sum/)
