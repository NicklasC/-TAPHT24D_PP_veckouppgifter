
import pytest
from Vecka_5.src.example import my_add
from Vecka_5.src.ovning_5_1_2 import sum_list
def test_empty_list():
    expected = None
    actual   = sum_list([])
    assert actual == expected

def test_number_list():
    assert sum_list([5]) == 5
    assert sum_list([5,7,8]) == 20
