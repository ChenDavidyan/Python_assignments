import pandas as pd
import numpy as np
import find_modified_position
import pytest


test1_path = "C:/work/Python_assignments/day06/test1.csv"
test2_path = "C:/work/Python_assignments/day06/test2.csv"

@pytest.mark.parametrize("text, expected", [
    (test1_path, 'chr9_108202745_+'), 
    (test2_path, 'chr15_40687446_-')
])
def test_find_most_modified_loci(text, expected):
    result = find_modified_position.find_most_modified_loci(text)
    assert result == expected
