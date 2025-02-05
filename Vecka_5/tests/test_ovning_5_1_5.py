from Vecka_5.src.ovning_5_1_5 import find_2nd_max
def test_find_2nd_max():
    assert find_2nd_max([1, 2, 3, 4, 5]) == 4
    assert find_2nd_max([1, 5]) == 1
    assert find_2nd_max([5, 5]) == 5
    assert find_2nd_max([1]) == None
