from Vecka_5.src.ovning_5_1_3 import count_vowels
def test_no_vowels():
    assert count_vowels("qwrt") == 0
    assert count_vowels("Tt") == 0
    assert count_vowels("123 123") == 0
    assert count_vowels("") == 0


def test_vowels():
    assert count_vowels("anne") == 2
