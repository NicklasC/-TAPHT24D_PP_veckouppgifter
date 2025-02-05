from Vecka_5.src.ovning_5_1_4 import find_max

def test_find_max():
    assert find_max([1,4,5,7,9]) == 9

def test_find_max_no_list():
    assert find_max([]) == None
