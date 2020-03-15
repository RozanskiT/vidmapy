from vidmapy.kurucz import model
# import pytest 
import io
from unittest.mock import MagicMock, mock_open
import pytest 


@pytest.fixture
def file_mock():
    model_string=\
"""TEFF   6000.  GRAVITY 4.00000 LTE 
TITLE  [0.0] VTURB=0  L/H=1.25 NOVER NEW ODF                                    
 OPACITY IFOP 1 1 1 1 1 1 1 1 1 1 1 1 1 0 1 0 0 0 0 0
 CONVECTION ON   1.25 TURBULENCE OFF  0.00  0.00  0.00  0.00
ABUNDANCE SCALE   0.50000 ABUNDANCE CHANGE 1 0.90040 2 0.08034
 ABUNDANCE CHANGE  3 -10.92  4 -10.64  5  -9.10  6  -4.52  7  -3.12  8  -3.21
 ABUNDANCE CHANGE  9  -8.48 10  -3.96 11  -5.71 12  -4.46 13  -5.57 14  -5.49
READ DECK6  3 RHOX,T,P,XNE,ABROSS,ACCRAD,VTURB, FLXCNV,VCOMV,VELSND
 5.47180180E-04   3658.0 1.507E+01 2.603E+09 2.441E-04 5.682E-02 0.000E+00 0.000E+00 0.000E+00 6.657E+05
 7.13840543E-04   3683.4 1.966E+01 3.340E+09 2.895E-04 6.391E-02 0.000E+00 0.000E+00 0.000E+00 6.576E+05
 9.01230714E-04   3711.3 2.482E+01 4.172E+09 3.441E-04 7.063E-02 0.000E+00 0.000E+00 0.000E+00 6.530E+05
PRADK 1.4875E+00
BEGIN                    ITERATION  15 COMPLETED
"""
    path = "model.mod"
    return io.StringIO(model_string)
    # return mock_open(mock=None, read_data=model_string)

def test_load_model():

    m = model.Model()

    assert 5777 == m.teff
    assert 4.44 == m.logg
    assert 0.00 == m.metallicity
    assert 0.9204 == m.chemical_composition["H"]
    assert 0.9204 == m.chemical_composition[1]
    assert -4.12 == m.chemical_composition["N"]
    assert -4.12 == m.chemical_composition[7]

def test_teff_logg_extraction():
    s = "TEFF   5777.  GRAVITY 3.44000 LTE"
    m = model.Model()

    teff = m._extract_teff(s)
    assert teff == 5777.
    
    logg = m._extract_logg(s)
    assert logg == 3.44

def test_read_title():
    s = "TITLE  [0.0] VTURB=0  L/H=1.25 NOVER NEW ODF \n"
    m = model.Model()

    title = m._extract_title(s)
    assert title == "[0.0] VTURB=0  L/H=1.25 NOVER NEW ODF"

def test_read_chemical_composition():
    s = "ABUNDANCE CHANGE  3 -10.92  4 -10.64  5  -9.10  6  -3.52  7  -3.12  8  -3.21\n"
    correct = {3: -10.92,  4: -10.64,  5:  -9.10,  6:  -3.52,  7:  -3.12,  8:  -3.21} 

    m = model.Model()
    cc = m._extract_chemical_composition(s)
    assert correct == cc
    
def test_read_H_He_chemical_composition():
    s = "ABUNDANCE SCALE   1.00000 ABUNDANCE CHANGE 1 0.90040 2 0.08034\n"
    correct = {1: 0.90040, 2: 0.08034} 

    m = model.Model()
    cc = m._extract_chemical_composition(s)
    assert correct == cc

def test_extract_depth_points():
    s = "READ DECK6 72 RHOX,T,P,XNE,ABROSS,ACCRAD,VTURB, FLXCNV,VCOMV,VELSND\n"
    
    m = model.Model()
    no_dp = m._extract_no_of_depth_points(s)

    assert no_dp == 72

def test_extract_column_names():
    s = "READ DECK6 72 RHOX,T,P,XNE,ABROSS,ACCRAD,VTURB, FLXCNV,VCOMV,VELSND\n"
    correct = ["RHOX","T","P","XNE","ABROSS","ACCRAD","VTURB", "FLXCNV","VCOMV","VELSND"]
    m = model.Model()
    column_names = m._extract_columns_names(s)

    assert all([x == y for x,y in zip(column_names,correct)] + [len(correct) == len(column_names)])

def test_extract_PRADK():
    s = "PRADK 1.4875E+00\n"
    correct = 1.4875
    m = model.Model()

    assert correct == m._extract_PRADK(s)

def test_extract_metallicity():
    s = "ABUNDANCE SCALE   0.10000 ABUNDANCE CHANGE 1 0.92140 2 0.07843"
    correct = 0.10000

    m = model.Model()

    assert m._extract_metallicity(s) == correct

def test_reading_model_in(file_mock):
    m = model.Model()
    m._read_model(file_mock)

    assert m.teff == 6000.
    assert m.logg == 4.00
    assert m.metallicity == 0.50000
    assert m.title == "[0.0] VTURB=0  L/H=1.25 NOVER NEW ODF"

    assert m.chemical_composition["H"] == 0.90040
    assert m.chemical_composition[1] == 0.90040
    assert m.chemical_composition["He"] == 0.08034
    assert m.chemical_composition[2] == 0.08034
    assert m.chemical_composition["C"] == -4.52
    assert m.chemical_composition[6] == -4.52 
    assert m.chemical_composition[9] == -8.48
    assert m.chemical_composition[14] == -5.49

    assert m.pradk == 1.4875E+00

    assert all([x==y for x,y in zip(m.structure["T"], [3658.0, 3683.4, 3711.3])])