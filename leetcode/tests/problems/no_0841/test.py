from leetcode.problems.no_0841.mycode_01 import Solution as SolutionMyCode01
from leetcode.problems.no_0841.mycode_01 import SolutionModelAnswer


ROOMS_01 = [[1], [2], [3], []]
ROOMS_02 = [[1, 3], [3, 0, 1], [2], [0]]
ROOMS_03 = [[1], [2], [1], []]


class TestMyCode:
    def test_01(self):
        solution = SolutionMyCode01()
        assert solution.canVisitAllRooms(ROOMS_01) == True

    def test_02(self):
        solution = SolutionMyCode01()
        assert solution.canVisitAllRooms(ROOMS_02) == False

    def test_03(self):
        solution = SolutionMyCode01()
        assert solution.canVisitAllRooms(ROOMS_03) == False


class TestModelAnswer:
    def test_01(self):
        solution = SolutionModelAnswer()
        assert solution.canVisitAllRooms(ROOMS_01) == True

    def test_02(self):
        solution = SolutionModelAnswer()
        assert solution.canVisitAllRooms(ROOMS_02) == False

    def test_03(self):
        solution = SolutionModelAnswer()
        assert solution.canVisitAllRooms(ROOMS_03) == False
