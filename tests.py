from main import double_donut
import pytest


@pytest.mark.parametrize('tested_list, expected_result', [([], []),
                                                          ([0],[0,0])])
def test_positive(tested_list, expected_result):
    assert double_donut(tested_list) == expected_result

