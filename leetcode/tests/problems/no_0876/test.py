import pytest

from leetcode.problems.no_0876.mycode import Solution as SolutionMyCode
from leetcode.problems.no_0876.mycode import SolutionModelAnswer


# Input examples here
CASES = [
    {"input": [1, 2, 3, 4, 5], "answer": [3,4,5]},
    {"input": [1, 2, 3, 4, 5, 6], "answer": [4,5,6]},
]


class TestMyCode:
    @pytest.mark.skip
    def test_00(self):
        case_num = 0
        solution = SolutionMyCode()
        assert solution.middleNode(CASES[case_num]["input"]) == CASES[case_num]["answer"]

    @pytest.mark.skip
    def test_01(self):
        case_num = 1
        solution = SolutionMyCode()
        assert solution.middleNode(CASES[case_num]["input"]) == CASES[case_num]["answer"]


class TestModelAnswer:
    @pytest.mark.skip
    def test_00(self):
        case_num = 0
        solution = SolutionModelAnswer()
        assert solution.middleNode(CASES[case_num]["input"]) == CASES[case_num]["answer"]
