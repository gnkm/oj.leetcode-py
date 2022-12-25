import pytest

from leetcode.problems.no_0412.mycode import Solution as SolutionMyCode
from leetcode.problems.no_0412.mycode import SolutionModelAnswer


# Input examples here
CASES = [
    {"input": 3 , "answer": ["1","2","Fizz"]},
    {"input": 5, "answer": ["1","2","Fizz","4","Buzz"]},
    {"input": 15, "answer": ["1","2","Fizz","4","Buzz","Fizz","7","8","Fizz","Buzz","11","Fizz","13","14","FizzBuzz"]},
]


class TestMyCode:
    def test_00(self):
        case_num = 0
        solution = SolutionMyCode()
        assert solution.fizzBuzz(CASES[case_num]["input"]) == CASES[case_num]["answer"]

    def test_01(self):
        case_num = 1
        solution = SolutionMyCode()
        assert solution.fizzBuzz(CASES[case_num]["input"]) == CASES[case_num]["answer"]

    def test_02(self):
        case_num = 2
        solution = SolutionMyCode()
        assert solution.fizzBuzz(CASES[case_num]["input"]) == CASES[case_num]["answer"]


class TestModelAnswer:
    def test_00(self):
        case_num = 0
        solution = SolutionMyCode()
        assert solution.fizzBuzz(CASES[case_num]["input"]) == CASES[case_num]["answer"]

    def test_01(self):
        case_num = 1
        solution = SolutionMyCode()
        assert solution.fizzBuzz(CASES[case_num]["input"]) == CASES[case_num]["answer"]

    def test_02(self):
        case_num = 2
        solution = SolutionMyCode()
        assert solution.fizzBuzz(CASES[case_num]["input"]) == CASES[case_num]["answer"]
