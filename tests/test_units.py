"""Unit testing."""
import pytest
import numpy as np

import convising.data as data


def test_cg_deci():

    test_images = np.array(
        [
            [[1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1]],
            [[-1, 1, 1, 1], [1, 1, 1, 1], [-1, -1, 1, -1], [-1, -1, -1, -1]],
            [[-1, -1, -1, -1], [-1, -1, -1, -1], [-1, -1, -1, -1], [-1, -1, -1, -1]],
        ]
    )
    test_cg, _ = data.coarse_grain(4, 0.5, "deci", 2, test_images)
    test_cg = test_cg[0]
    deci_test_images = np.array(
        [[[1, 1], [1, 1]], [[-1, 1], [-1, 1]], [[-1, -1], [-1, -1]]]
    )

    assert np.array_equal(deci_test_images, test_cg)


def test_cg_maj():

    test_images = np.array(
        [
            [[ 1,  1,  1,  1],
             [ 1,  1,  1,  1],
             [ 1,  1,  1,  1],
             [ 1,  1,  1,  1]],
            [[ 1,  1,  1,  1],
             [ 1, -1,  1,  1],
             [-1, -1,  1, -1],
             [-1, -1, -1, -1]],
            [[-1, -1, -1, -1],
             [-1, -1, -1, -1],
             [-1, -1, -1, -1],
             [-1, -1, -1, -1]],
        ]
    )
    test_cg, _ = data.coarse_grain(4, 0.5, "maj", 2, test_images)
    test_cg = test_cg[0]
    maj_test_images = np.array(
        [
            [[ 1,  1],
             [ 1,  1]],
            [[ 1,  1],
             [-1, -1]],
            [[-1, -1],
             [-1, -1]],
        ]
    )

    assert np.array_equal(maj_test_images, test_cg)


def test_cg_maj_e():

    test_images = np.array(
        [
            [[ 1,  1,  1,  1],
             [ 1,  1,  1,  1],
             [ 1,  1,  1,  1],
             [ 1,  1,  1,  1]],

            [[ 1,  1,  1,  1],
             [ 1, -1,  1,  1],
             [-1, -1,  1, -1],
             [-1, -1, -1, -1]],

            [[-1,  1,  1,  1],
             [-1, -1,  1, -1],
             [-1, -1,  1, -1],
             [-1, -1, -1, -1]],

            [[-1,  1, -1,  1],
             [-1, -1,  1, -1],
             [ 1,  1,  1, -1],
             [-1, -1, -1, -1]],

            [[-1, -1, -1, -1],
             [-1, -1, -1, -1],
             [-1, -1, -1, -1],
             [-1, -1, -1, -1]],
             
            [[-1, -1,  1,  1],
             [-1, -1,  1,  1],
             [ 1,  1, -1, -1],
             [ 1,  1, -1, -1]],
        ]
    )
    test_cg, test_ediffs = data.coarse_grain(4, 3.0, "maj", 2, test_images)
    true_ediffs = np.exp(-3.0 * np.array([16, 0, 4, -8, 16, -16]))

    np.testing.assert_allclose(true_ediffs, test_ediffs)


def test_cg_deci_e():

    test_images = np.array(
        [
            [[1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1]],
            [[ 1,  1,  1,  1],
             [ 1, -1,  1,  1],
             [-1, -1,  1, -1],
             [-1, -1, -1, -1]],
            [[-1, -1, -1, -1], [-1, -1, -1, -1], [-1, -1, -1, -1], [-1, -1, -1, -1]],
        ]
    )
    test_cg, test_ediffs = data.coarse_grain(4, 0.5, "deci", 2, test_images)
    true_ediffs = np.exp(-0.5 * np.array([8, 4, 8]))

    np.testing.assert_allclose(true_ediffs, test_ediffs)
