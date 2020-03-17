from vidmapy.kurucz import model_definition

import pytest
from unittest.mock import MagicMock

@pytest.mark.parametrize("teff,logg,correct_definition", 
                            [(10000.0, 1.0 , "SCALE 72 -6.875 0.125 10000. 1.00\n"), 
                             (4534.0 , 4.24, "SCALE 72 -6.875 0.125  4534. 4.24\n"), 
                             (900.0  , 0.5 , "SCALE 72 -6.875 0.125   900. 0.50\n")
                            ]
                        )
def test_teff_logg_string(teff, logg, correct_definition):
    parameters = MagicMock()
    parameters.teff = teff
    parameters.logg = logg

    # TEFF FORMAT "-----."
    # LOGG FORMAT "-.--"
    # "SCALE 72 -6.875 0.125 -----. -.--"

    md = model_definition.ModelDefinition()
    assert md._teff_logg(parameters) == correct_definition

def test_introduction():
    correct_intoduction = """READ KAPPA
READ PUNCH
MOLECULES ON
READ MOLECULES
FREQUENCIES 337 1 337 BIG
CONVECTION OVER 1.25 0 36
"""
    md = model_definition.ModelDefinition()
    assert md._introduction() == correct_intoduction

@pytest.mark.parametrize("microturbulence,correct", [(0.0,"VTURB 0.0E+00\n"), (1e5,"VTURB 1.0E+05\n"), (9.2e5,"VTURB 9.2E+05\n")])
def test_turbulence(microturbulence, correct):
    parameters = MagicMock()
    parameters.microturbulence = microturbulence

    md = model_definition.ModelDefinition()
    assert md._microturbulence(parameters) == correct


def test_set_title():
    parameters = MagicMock()
    parameters.microturbulence = 10
    parameters.teff = 8000
    parameters.logg = 4.34
    parameters.metallicity = 0.0

    title_line = "TITLE TEFF=8000, LOGG=4.34, [M/H]=0.00, VMIC=10\n"

    md = model_definition.ModelDefinition()
    assert md._title(parameters) == title_line

@pytest.mark.parametrize("metallicity,correct", 
                            [(1.0 , "ABUNDANCE SCALE   10.0000\n"), 
                             (-0.5, "ABUNDANCE SCALE   0.3162\n"), 
                             (0.5 , "ABUNDANCE SCALE   3.1623\n")
                            ]
                        )
def test_metallicity(metallicity, correct):
    parameters = MagicMock()
    parameters.metallicity = metallicity

    md = model_definition.ModelDefinition()
    assert md._metallicity(parameters) == correct

def test_single_abundance():
    parameters = MagicMock()

    parameters.chemical_composition = {1:0.9004,2:0.08034,3:-10.92, 100:None}

    correct = "ABUNDANCE CHANGE  1 0.9004\nABUNDANCE CHANGE  2 0.08034\nABUNDANCE CHANGE  3 -10.92\n"
    md = model_definition.ModelDefinition()
    for c, r in zip(correct.splitlines(),md._chemical_composition(parameters).splitlines()):
        assert c[0:17] == r[0:17]
        assert float(c[17:20]) == float(r[17:20])
        assert float(c[20:]) == float(r[20:])

def test_ending():
    correct = """ITERATIONS 15
PRINT 1 0 0 0 0 0 0 0 0 0 0 0 0 0 1
PUNCH 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1
BEGIN                    ITERATION  15 COMPLETED
END
"""
    md = model_definition.ModelDefinition()
    assert correct == md._ending()

def test_creating_model_definition():
    parameters = MagicMock()

    parameters.microturbulence = 10
    parameters.teff = 8000
    parameters.logg = 4.34
    parameters.metallicity = 0.0
    parameters.chemical_composition = {1:0.9004,2:0.08034,3:-10.92, 100:None}

    md = model_definition.ModelDefinition()
    model_string = md(parameters)
    # It is difficult to test correct format of ATLAS definition file so I don't do it
    # I test the type in order to document how to use ModelDefinition class
    assert type("string") == type(model_string) 