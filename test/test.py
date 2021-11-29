"""
TODO: Test suite for implementation data structures.
So far, this script only contains some skeleton code for later.
"""

import sys
from pathlib import Path
sys.path.append(str(Path(__file__).absolute().parent.parent))

import src

def queue_validity():
    q = src.Queue()
    assert q.is_empty()
    return

def stack_validity():
    s = src.Stack()
    assert s.is_empty()
    return

if __name__ == '__main__':
    queue_validity()
    stack_validity()
    print("All tests complete.")
