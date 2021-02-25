import numpy as np
import pytest
import matplotlib.pyplot as plt

"""
This test script is for _plot_args() in lib/matplotlib/axes/_base.py
"""

# This always leads to a failure!
# plot() does sth to float() the 3rd param.
# def test_bad_fmt():
#     with pytest.raises(ValueError, match='third arg must be a format string'):
#         plt.plot([1, 2], [2, 0], 1220)


def test_bad_shape():
    """
    Corresponding to branch: cov.log(10)
    Test x and y data in different shapes
    """
    
    x = np.array([[1, 2],[3, 4],[5, 6]])
    y = np.array([[1, 2],[3, 4]])

    # This is an assertion that a ValueError will be raised.
    # And the error message is asserted to be in a certain format.
    with pytest.raises(ValueError, match=r".*x and y must have same first dimension.*"):
        plt.plot(x, y)


def test_bad_dim():
    """
    Corresponding to branch: cov.log(11)
    Test x and y data with too high dimension
    """
    
    x = np.array([[[1], [2]],[[3], [4]],[[5], [6]]])
    y = np.array([[[3], [4]],[[5], [6]],[[1], [2]]])

    # This is an assertion that a ValueError will be raised.
    # And the error message is asserted to be in a certain format.
    with pytest.raises(ValueError, match=r".*x and y can be no greater than 2D.*"):
        plt.plot(x, y)
