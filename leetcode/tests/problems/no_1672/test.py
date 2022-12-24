from leetcode.problems.no_1672.mycode import Solution as SolutionMyCode
from leetcode.problems.no_1672.mycode import SolutionModelAnswer


# Input examples here
CASES = [
    {
        "input": [[1,2,3],[3,2,1]],
        "answer": 6
    },
    {
        "input": [[1,5],[7,3],[3,5]],
        "answer": 10
    },
    {
        "input": [[2,8,7],[7,1,3],[1,9,5]],
        "answer": 17
    },
]


class TestMyCode:
    def test_00(self):
        case_num = 0
        solution = SolutionMyCode()
        assert (
            solution.maximumWealth(CASES[case_num]["input"]) == CASES[case_num]["answer"]
        )

    def test_01(self):
        case_num = 1
        solution = SolutionMyCode()
        assert (
            solution.maximumWealth(CASES[case_num]["input"]) == CASES[case_num]["answer"]
        )

    def test_02(self):
        case_num = 2
        solution = SolutionMyCode()
        assert (
            solution.maximumWealth(CASES[case_num]["input"]) == CASES[case_num]["answer"]
        )

class TestModelAnswer:
    def test_01(self):
        case_num = 0
        solution = SolutionModelAnswer()
        # assert
