import pytest

from leetcode.problems.no_0055.mycode import Solution as SolutionMyCode
from leetcode.problems.no_0055.mycode import (
    SolutionRecursively as SolutionMyCodeRecursively,
)
from leetcode.problems.no_0055.mycode import SolutionModelAnswer


# Input examples here
CASES = [
    # 0 - 4
    {"input": [2, 3, 1, 1, 4], "answer": True},
    {"input": [3, 2, 1, 0, 4], "answer": False},
    {"input": [2, 2, 0, 1, 4], "answer": True},
    {"input": [0], "answer": True},
    {"input": [2, 0], "answer": True},
    # 5 - 10
    # fmt: off
    {"input": [8,2,4,4,4,9,5,2,5,8,8,0,8,6,9,1,1,6,3,5,1,2,6,6,0,4,8,6,0,3,2,8,7,6,5,1,7,0,3,4,8,3,5,9,0,4,0,1,0,5,9,2,0,7,0,2,1,0,8,2,5,1,2,3,9,7,4,7,0,0,1,8,5,6,7,5,1,9,9,3,5,0,7,5], "answer": True},
    # case 72
    # fmt: on
]


class TestMyCode:
    solution = SolutionMyCode()

    def test_00(self):
        case_num = 0
        assert (
            self.solution.canJump(CASES[case_num]["input"]) == CASES[case_num]["answer"]
        )

    def test_01(self):
        case_num = 1
        assert (
            self.solution.canJump(CASES[case_num]["input"]) == CASES[case_num]["answer"]
        )

    def test_02(self):
        case_num = 2
        assert (
            self.solution.canJump(CASES[case_num]["input"]) == CASES[case_num]["answer"]
        )

    def test_03(self):
        case_num = 3
        assert (
            self.solution.canJump(CASES[case_num]["input"]) == CASES[case_num]["answer"]
        )

    def test_04(self):
        case_num = 4
        assert (
            self.solution.canJump(CASES[case_num]["input"]) == CASES[case_num]["answer"]
        )

    def test_05(self):
        case_num = 5
        assert (
            self.solution.canJump(CASES[case_num]["input"]) == CASES[case_num]["answer"]
        )


class TestMyCodeRecursive:
    solution = SolutionMyCodeRecursively()

    def test_00(self):
        case_num = 0
        assert (
            self.solution.canJump(CASES[case_num]["input"]) == CASES[case_num]["answer"]
        )

    def test_01(self):
        case_num = 1
        assert (
            self.solution.canJump(CASES[case_num]["input"]) == CASES[case_num]["answer"]
        )

    def test_02(self):
        case_num = 2
        assert (
            self.solution.canJump(CASES[case_num]["input"]) == CASES[case_num]["answer"]
        )

    def test_03(self):
        case_num = 3
        assert (
            self.solution.canJump(CASES[case_num]["input"]) == CASES[case_num]["answer"]
        )

    def test_04(self):
        case_num = 4
        assert (
            self.solution.canJump(CASES[case_num]["input"]) == CASES[case_num]["answer"]
        )


class TestModelAnswer:
    solution = SolutionModelAnswer()

    @pytest.mark.skip
    def test_00(self):
        case_num = 0
        assert (
            self.solution.canJump(CASES[case_num]["input"]) == CASES[case_num]["answer"]
        )
