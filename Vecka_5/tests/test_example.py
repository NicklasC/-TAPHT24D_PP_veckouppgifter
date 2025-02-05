import pytest
#  $env:PYTHONPATH="D:\Dev\TAPHT24D_PP_veckouppgifter"
from Vecka_5.src.example import my_add


def test_my_add():
    assert my_add(1, 2) == 3

