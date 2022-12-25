import pytest

from leetcode.problems.no_0383.mycode import Solution as SolutionMyCode
from leetcode.problems.no_0383.mycode import SolutionModelAnswer
from leetcode.problems.no_0383.mycode import SolutionExampleAnswer01


# Input examples here
CASES = [
    {"input": {"ransome_note": "a", "magazine": "b"}, "answer": False},
    {"input": {"ransome_note": "aa", "magazine": "ab"}, "answer": False},
    {"input": {"ransome_note": "aa", "magazine": "aab"}, "answer": True},
]


class TestMyCode:
    def test_00(self):
        case_num = 0
        solution = SolutionMyCode()
        ransome_note = CASES[case_num]["input"]["ransome_note"]
        magazine = CASES[case_num]["input"]["magazine"]
        assert (
            solution.canConstruct(ransome_note, magazine) == CASES[case_num]["answer"]
        )

    def test_01(self):
        case_num = 1
        solution = SolutionMyCode()
        ransome_note = CASES[case_num]["input"]["ransome_note"]
        magazine = CASES[case_num]["input"]["magazine"]
        assert (
            solution.canConstruct(ransome_note, magazine) == CASES[case_num]["answer"]
        )

    def test_02(self):
        case_num = 2
        solution = SolutionMyCode()
        ransome_note = CASES[case_num]["input"]["ransome_note"]
        magazine = CASES[case_num]["input"]["magazine"]
        assert (
            solution.canConstruct(ransome_note, magazine) == CASES[case_num]["answer"]
        )


class TestModelAnswer:
    @pytest.mark.skip
    def test_00(self):
        case_num = 0
        solution = SolutionMyCode()
        ransome_note = CASES[case_num]["input"]["ransome_note"]
        magazine = CASES[case_num]["input"]["magazine"]
        assert (
            solution.canConstruct(ransome_note, magazine) == CASES[case_num]["answer"]
        )


class TestExampleAnswer01:
    def test_00(self):
        case_num = 0
        solution = SolutionExampleAnswer01()
        ransome_note = CASES[case_num]["input"]["ransome_note"]
        magazine = CASES[case_num]["input"]["magazine"]
        assert (
            solution.canConstruct(ransome_note, magazine) == CASES[case_num]["answer"]
        )

    def test_01(self):
        case_num = 1
        solution = SolutionExampleAnswer01()
        ransome_note = CASES[case_num]["input"]["ransome_note"]
        magazine = CASES[case_num]["input"]["magazine"]
        assert (
            solution.canConstruct(ransome_note, magazine) == CASES[case_num]["answer"]
        )

    def test_02(self):
        case_num = 2
        solution = SolutionExampleAnswer01()
        ransome_note = CASES[case_num]["input"]["ransome_note"]
        magazine = CASES[case_num]["input"]["magazine"]
        assert (
            solution.canConstruct(ransome_note, magazine) == CASES[case_num]["answer"]
        )
