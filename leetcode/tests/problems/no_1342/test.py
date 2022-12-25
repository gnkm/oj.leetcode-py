import pytest

from leetcode.problems.no_1342.mycode import Solution as SolutionMyCode
from leetcode.problems.no_1342.mycode import SolutionModelAnswer


# Input examples here
CASES = [
    {"input": 14, "answer": 6},
    {"input": 8, "answer": 4},
    {"input": 123, "answer": 12},
]


class TestMyCode:
    def test_00(self):
        case_num = 0
        solution = SolutionMyCode()
        assert (
            solution.numberOfSteps(CASES[case_num]["input"])
            == CASES[case_num]["answer"]
        )

    def test_01(self):
        case_num = 1
        solution = SolutionMyCode()
        assert (
            solution.numberOfSteps(CASES[case_num]["input"])
            == CASES[case_num]["answer"]
        )

    def test_02(self):
        case_num = 2
        solution = SolutionMyCode()
        assert (
            solution.numberOfSteps(CASES[case_num]["input"])
            == CASES[case_num]["answer"]
        )


class TestModelAnswer:
    @pytest.mark.skip
    def test_00(self):
        case_num = 0
        solution = SolutionMyCode()
        assert (
            solution.numberOfSteps(CASES[case_num]["input"])
            == CASES[case_num]["answer"]
        )
