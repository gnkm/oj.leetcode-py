import pytest

from leetcode.problems.no_0001.example_02 import Solution as SolutionEx02
from leetcode.problems.no_0001.mycode_01 import Solution as SolutionMyCode01

# fmt: off
cases = [
    {"nums": [2, 7, 11, 15], "target": 9, "expected": [0, 1]},
    {"nums": [3, 2, 4], "target": 6, "expected": [1, 2]},
    {"nums": [3, 3,], "target": 6, "expected": [0, 1]},
    {"nums": [2, 3, 5, 7, 11, 13], "target": 24, "expected": [4, 5]},
]
# fmt: on


class TestMyCode01:
    solution = SolutionMyCode01()

    def test_00(self):
        solution = self.solution
        case = cases[0]
        assert solution.twoSum(case["nums"], case["target"]) == case["expected"]

    def test_01(self):
        solution = self.solution
        case = cases[1]
        assert solution.twoSum(case["nums"], case["target"]) == case["expected"]

    def test_02(self):
        solution = self.solution
        case = cases[2]
        assert solution.twoSum(case["nums"], case["target"]) == case["expected"]

    def test_03(self):
        solution = self.solution
        case = cases[3]
        assert solution.twoSum(case["nums"], case["target"]) == case["expected"]


class TestEx02:
    solution = SolutionEx02()

    def test_00(self):
        solution = self.solution
        case = cases[0]
        assert solution.twoSum(case["nums"], case["target"]) == case["expected"]

    def test_01(self):
        solution = self.solution
        case = cases[1]
        assert solution.twoSum(case["nums"], case["target"]) == case["expected"]

    def test_02(self):
        solution = self.solution
        case = cases[2]
        assert solution.twoSum(case["nums"], case["target"]) == case["expected"]

    def test_03(self):
        solution = self.solution
        case = cases[3]
        assert solution.twoSum(case["nums"], case["target"]) == case["expected"]
