"""{No}. {Title}

URL: {URL}

## Description

{description}

difficulty: {difficulty}
"""

from typing import Dict, List, Union


# my code.
class Solution:
    pass


class SolutionModelAnswer:
    """
    {URL}
    """
    pass


if __name__ == "__main__":
    import pkg_resources
    if any([str(i).startswith('icecream') for i in pkg_resources.working_set]):
        import icecream
        _debug = icecream.ic
    else:
        _debug = print

    global debug
    debug = _debug
