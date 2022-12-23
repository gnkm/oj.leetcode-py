"""Create some files for solving a problem.

Usage:
    python create_files.py {ID}

Example:
    python create_files.py 1234

"""

import os
import shutil
import sys

import icecream


TEMPLATE_ANSWER_CODE_FILE = "templates/mycode_01.py"
TEMPLATE_TEST_CODE_FILE = "templates/test.py"


def main():
    problem_id = sys.argv[1]
    # codes for answering
    answer_codes_dir = f"leetcode/problems/no_{problem_id:0>4}"
    os.makedirs(answer_codes_dir)
    with open(f"{answer_codes_dir}/__init__.py", "a"):
        pass
    shutil.copy(TEMPLATE_ANSWER_CODE_FILE, answer_codes_dir)

    # codes for testing
    test_codes_dir = f"leetcode/tests/problems/no_{problem_id:0>4}"
    os.makedirs(test_codes_dir)
    with open(f"{test_codes_dir}/__init__.py", "a"):
        pass
    shutil.copy(TEMPLATE_TEST_CODE_FILE, test_codes_dir)

    sys.exit()


def debug(v):
    icecream.ic(v)


if __name__ == "__main__":
    main()
