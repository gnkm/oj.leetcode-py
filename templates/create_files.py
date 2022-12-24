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


TEMPLATE_DIR = "templates"
ANSWER_CODE_FILE_NAME = "mycode.py"
TEST_CODE_FILE_NAME = "test.py"
TEMPLATE_ANSWER_CODE_FILE = f"{TEMPLATE_DIR}/{ANSWER_CODE_FILE_NAME}"
TEMPLATE_TEST_CODE_FILE = f"{TEMPLATE_DIR}/{TEST_CODE_FILE_NAME}"


debug = icecream.ic


def main():
    problem_id = sys.argv[1]
    problem_id_formatted = f"{problem_id:0>4}"

    # codes for answering
    answer_codes_dir = f"leetcode/problems/no_{problem_id_formatted}"
    os.makedirs(answer_codes_dir)
    with open(f"{answer_codes_dir}/__init__.py", "a"):
        pass
    shutil.copy(TEMPLATE_ANSWER_CODE_FILE, answer_codes_dir)

    # codes for testing
    test_codes_dir = f"leetcode/tests/problems/no_{problem_id_formatted}"
    os.makedirs(test_codes_dir)
    with open(f"{test_codes_dir}/__init__.py", "a"):
        pass

    with open(TEMPLATE_TEST_CODE_FILE, "r") as f:
        org_code = f.read()
        new_code = org_code.replace('{ID}', problem_id_formatted)

    with open(f"{test_codes_dir}/{TEST_CODE_FILE_NAME}", "a") as f:
        f.write(new_code)

    sys.exit()


if __name__ == "__main__":
    main()
