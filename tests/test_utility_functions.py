#!/usr/bin/env python3
import pytest
from vidmapy.kurucz.utility_functions import string_from_kurucz_code, encode_roman_numeral

@pytest.mark.parametrize("code,atom_symbol", 
                            [(6.01, "CII"),
                             (12.00, 'MgI'),
                             ("01.00",'HI'),
                             ('06.03','CIV'),
                             (6.01105,'CII'),
                             (6.00999,'CII'),
                            ]
                        )
def test_string_from_kurucz_code(code, atom_symbol):
    assert string_from_kurucz_code(code) == atom_symbol

def test_encode_roman_numeral():
    assert "II" == encode_roman_numeral(2)