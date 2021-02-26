import pytest
from matplotlib._version import git_versions_from_keywords

"""
This test script is for git_versions_from_keywords() in lib/matplotlib/_version.py
"""

def test_git_unknown_version():
    """
    This test covers more branches corresponding to git version >= 1.8.3.
    The code version is unknown from the tags.
    """
    keywords = {'refnames': 'tag: 0.01', 'full': 'abcdefg'}
    tag_prefix = "v"
    verbose = False
    git_ans = git_versions_from_keywords(keywords, tag_prefix, verbose)
    unknown_version = {
        "version": "0+unknown",
        "full-revisionid": "abcdefg",
        "dirty": False,
        "error": "no suitable tags"
    }
    assert git_ans == unknown_version


def test_git_known_version():
    """
    This test covers more branches corresponding to git version >= 1.8.3.
    The code version is known from the tags.
    """
    keywords = {'refnames': 'tag: v0.01', 'full': 'abcdefg'}
    tag_prefix = "v"
    verbose = False
    git_ans = git_versions_from_keywords(keywords, tag_prefix, verbose)
    known_version = {"version": "0.01",
                     "full-revisionid": 'abcdefg',
                     "dirty": False,
                     "error": None
                     }
    assert git_ans == known_version


def test_git_verbose(capsys):
    """
    Test the verbose argument and ensure this method can print some info.
    Cover more branches.
    """
    keywords = {'refnames': 'tag: v0.01', 'full': 'abcdefg'}
    tag_prefix = "v"
    verbose = True
    git_ans = git_versions_from_keywords(keywords, tag_prefix, verbose)
    known_version = {"version": "0.01",
                     "full-revisionid": 'abcdefg',
                     "dirty": False,
                     "error": None
                     }
    captured = capsys.readouterr()
    assert captured.out == "likely tags: v0.01\npicking 0.01\n"
    assert git_ans == known_version
