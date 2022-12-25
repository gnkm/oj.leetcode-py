"""Create some files for solving a problem.

Usage:
    python create_files.py {ID}

Example:
    Make files in `problems` directory
    python create_files.py 123

    Make files in `contests` directory
    python create_files.py 123 --problem_type contests

"""

import argparse
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
    args_from_cli = parse_args()
    problem_id = args_from_cli.problem_id
    problem_type = args_from_cli.problem_type

    problem_id_formatted = f"{problem_id:0>4}"

    # codes for answering
    answer_codes_dir = f"leetcode/{problem_type}/no_{problem_id_formatted}"
    os.makedirs(answer_codes_dir)
    with open(f"{answer_codes_dir}/__init__.py", "a"):
        pass
    shutil.copy(TEMPLATE_ANSWER_CODE_FILE, answer_codes_dir)

    # codes for testing
    test_codes_dir = f"leetcode/tests/{problem_type}/no_{problem_id_formatted}"
    os.makedirs(test_codes_dir)
    with open(f"{test_codes_dir}/__init__.py", "a"):
        pass

    with open(TEMPLATE_TEST_CODE_FILE, "r") as f:
        org_code = f.read()
        new_code = org_code.replace("{ID}", problem_id_formatted)

    with open(f"{test_codes_dir}/{TEST_CODE_FILE_NAME}", "a") as f:
        f.write(new_code)

    sys.exit()


def parse_args():
    parser = argparse.ArgumentParser(
        description="Create some files for solving a problem.",
    )
    parser.add_argument(
        "problem_id",
        help="Problem ID",
    )
    parser.add_argument(
        "--problem_type",
        choices=["problems", "contests"],
        default="problems",
    )
    args = parser.parse_args()

    return args


if __name__ == "__main__":
    main()
