import pytest

from pJITAI import interface

# Ref: https://github.com/realpython/reader/blob/master/tests/test_feed.py

def test_version():
    import pJITAI
    print(pJITAI.__version__)