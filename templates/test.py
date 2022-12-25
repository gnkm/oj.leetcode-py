from leetcode.problems.no_{ID}.mycode import Solution as SolutionMyCode
from leetcode.problems.no_{ID}.mycode import SolutionModelAnswer


# Input examples here
CASES = [
    {"input": None, "answer": None},
    {"input": None, "answer": None},
    {"input": None, "answer": None},
]


class TestMyCode:
    def test_00(self):
        case_num = 0
        solution = SolutionMyCode()
        # edit method name
        assert solution.problem_function(CASES[case_num]["input"]) == CASES[case_num]["answer"]


class TestModelAnswer:
    def test_00(self):
        case_num = 0
        solution = SolutionMyCode()
        # edit method name
        assert solution.problem_function(CASES[case_num]["input"]) == CASES[case_num]["answer"]
