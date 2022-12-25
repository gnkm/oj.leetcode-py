import pytest

from leetcode.problems.no_2389.mycode import Solution as SolutionMyCode
from leetcode.problems.no_2389.mycode import SolutionModelAnswer


# Input examples here
CASES = [
    {"input": {"nums": [4, 5, 2, 1], "queries": [3, 10, 21]}, "answer": [2, 3, 4]},
    {"input": {"nums": [2, 3, 4, 5], "queries": [1]}, "answer": [0]},
    # original case
    {"input": {"nums": [1, 2, 3, 4, 5], "queries": [15]}, "answer": [5]},
    {"input": {"nums": [1, 2, 3, 4, 5], "queries": [14]}, "answer": [4]},
]


class TestMyCode:
    solution = SolutionMyCode()

    def test_00(self):
        case_num = 0
        nums = CASES[case_num]["input"]["nums"]
        queries = CASES[case_num]["input"]["queries"]
        assert self.solution.answerQueries(nums, queries) == CASES[case_num]["answer"]

    def test_01(self):
        case_num = 1
        nums = CASES[case_num]["input"]["nums"]
        queries = CASES[case_num]["input"]["queries"]
        assert self.solution.answerQueries(nums, queries) == CASES[case_num]["answer"]

    def test_02(self):
        case_num = 2
        nums = CASES[case_num]["input"]["nums"]
        queries = CASES[case_num]["input"]["queries"]
        assert self.solution.answerQueries(nums, queries) == CASES[case_num]["answer"]

    def test_03(self):
        case_num = 3
        nums = CASES[case_num]["input"]["nums"]
        queries = CASES[case_num]["input"]["queries"]
        assert self.solution.answerQueries(nums, queries) == CASES[case_num]["answer"]


class TestModelAnswer:
    solution = SolutionModelAnswer()

    @pytest.mark.skip
    def test_00(self):
        case_num = 0
        nums = CASES[case_num]["input"]["nums"]
        queries = CASES[case_num]["input"]["queries"]

        assert self.solution.answerQueries(nums, queries) == CASES[case_num]["answer"]
