from main import double_donut
import pytest


@pytest.mark.parametrize('tested_list, expected_result', [([], []),  # blank list
                                                          ([1, -1, 1, 10, -10], [1, -1, 1, 10, -10]),  # no zeros
                                                          ([0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0]), # zeros only
                                                          ([0, -1, 0, 10, 0], [0, 0, -1, 0, 0, 10, 0, 0])]) # list with zeros
def test_positive(tested_list, expected_result):
    assert double_donut(tested_list) == expected_result
