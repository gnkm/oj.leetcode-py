import pytest

from leetcode.problems.no_{ID}.mycode import Solution as SolutionMyCode
from leetcode.problems.no_{ID}.mycode import SolutionModelAnswer


# Input examples here
CASES = [
    {"input": None, "answer": None},
    {"input": None, "answer": None},
    {"input": None, "answer": None},
]


class TestMyCode:
    solution = SolutionMyCode()

    def test_00(self):
        case_num = 0
        solution = SolutionMyCode()
        # Edit method name
        assert self.solution.problem_function(CASES[case_num]["input"]) == CASES[case_num]["answer"]


class TestModelAnswer:
    solution = SolutionModelAnswer()

    # Delete following line if test model answer
    @pytest.mark.skip
    def test_00(self):
        case_num = 0
        # Edit method name
        assert self.solution.problem_function(CASES[case_num]["input"]) == CASES[case_num]["answer"]
