from leetcode.problems.no_1480.mycode_01 import Solution as SolutionMyCode01

# from leetcode.problems.no_1480.mycode_01 import SolutionModelAnswer


CASES = [
    {"input": [1, 2, 3, 4], "answer": [1, 3, 6, 10]},
    {"input": [1, 1, 1, 1, 1], "answer": [1, 2, 3, 4, 5]},
    {"input": [3, 1, 2, 10, 1], "answer": [3, 4, 6, 16, 17]},
]


class TestMyCode:
    def test_01(self):
        case_num = 0
        solution = SolutionMyCode01()
        assert (
            solution.runningSum(CASES[case_num]["input"]) == CASES[case_num]["answer"]
        )

    def test_02(self):
        case_num = 1
        solution = SolutionMyCode01()
        assert (
            solution.runningSum(CASES[case_num]["input"]) == CASES[case_num]["answer"]
        )

    def test_03(self):
        case_num = 2
        solution = SolutionMyCode01()
        assert (
            solution.runningSum(CASES[case_num]["input"]) == CASES[case_num]["answer"]
        )


class TestModelAnswer:
    def test_01(self):
        case_num = 0
        solution = SolutionMyCode01()
        assert (
            solution.runningSum(CASES[case_num]["input"]) == CASES[case_num]["answer"]
        )

    def test_02(self):
        case_num = 1
        solution = SolutionMyCode01()
        assert (
            solution.runningSum(CASES[case_num]["input"]) == CASES[case_num]["answer"]
        )

    def test_03(self):
        case_num = 2
        solution = SolutionMyCode01()
        assert (
            solution.runningSum(CASES[case_num]["input"]) == CASES[case_num]["answer"]
        )
