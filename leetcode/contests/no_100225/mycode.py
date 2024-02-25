"""Find the Largest Area of Square Inside Two Rectangles - LeetCode Contest
https://leetcode.com/contest/weekly-contest-386/problems/find-the-largest-area-of-square-inside-two-rectangles/
"""

from typing import List


class Solution:
    def largestSquareArea(
        self, bottomLeft: List[List[int]], topRight: List[List[int]]
    ) -> int:
        # max_intersection = {"bl": [0, 0], "tr": [0, 0], "area": 0}
        max_area = 0
        for i, bottom_left_i in enumerate(bottomLeft):
            if i == len(bottomLeft) - 1:
                break
            for j, bottom_left_j in enumerate(bottomLeft[i + 1 :]):
                rect_1 = [bottom_left_i, topRight[i]]
                rect_2 = [bottom_left_j, topRight[j]]
                center_of_rect_1 = [
                    (rect_1[0][0] + rect_1[1][0]) / 2,
                    (rect_1[0][1] + rect_1[1][1]) / 2,
                ]
                center_of_rect_2 = [
                    (rect_2[0][0] + rect_2[1][0]) / 2,
                    (rect_2[0][1] + rect_2[1][1]) / 2,
                ]
                width_of_rect_1 = abs(rect_1[0][0] - rect_1[1][0])
                height_of_rect_1 = abs(rect_1[0][1] - rect_1[1][1])
                width_of_rect_2 = abs(rect_2[0][0] - rect_2[1][0])
                height_of_rect_2 = abs(rect_2[0][1] - rect_2[1][1])

                if any(
                    [
                        abs(center_of_rect_1[0] - center_of_rect_2[0])
                        < (width_of_rect_1 + width_of_rect_2) / 2,
                        abs(center_of_rect_1[1] - center_of_rect_2[1])
                        < (height_of_rect_1 + height_of_rect_2) / 2,
                    ]
                ):
                    continue
                elif True:
                    intersection = [
                        [rect_1[0][0], rect_2[0][1]],
                        [rect_2[1][0], rect_1[1][1]],
                    ]

        return max_area


def main():
    cases = [
        {
            "bottomLeft": [[1, 1], [2, 2], [3, 1]],
            "topRight": [[3, 3], [4, 4], [6, 6]],
            "expected": 1,
        },
        {
            "bottomLeft": [[1, 1], [2, 2], [1, 2]],
            "topRight": [[3, 3], [4, 4], [3, 4]],
            "expected": 1,
        },
        {
            "bottomLeft": [[1, 1], [3, 3], [3, 1]],
            "topRight": [[2, 2], [4, 4], [4, 2]],
            "expected": 0,
        },
    ]
    for case in cases:
        sol = Solution()
        assert (
            sol.largestSquareArea(case["bottomLeft"], case["topRight"])
            == case["expected"]
        ), f"{case['bottomLeft']} and {case['topRight']} expected {case['expected']}"


if __name__ == "__main__":
    main()
