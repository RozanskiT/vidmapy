from vidmapy.kurucz import parameters
import numpy as np

def test_default_parameters():
    param = parameters.Parameters()

    assert param.teff == 5777
    assert param.logg == 4.44
    assert param.metallicity == 0.0
    assert param.microturbulence == 2.0

def test_chemical_composition():
    param = parameters.Parameters()

    assert param.chemical_composition["H"] == 0.9204
    assert param.chemical_composition["He"] == 0.07834
    assert param.chemical_composition["C"] == -3.52
    assert param.chemical_composition["N"] == -4.12
    assert param.chemical_composition["O"] == -3.21
    assert param.chemical_composition["Si"] == -4.49

def test_change_chemical_composition():
    param = parameters.Parameters()

    param.chemical_composition["C"] = -3.40
    assert param.chemical_composition["C"] == -3.40
    assert param.chemical_composition[6]   == -3.40

    param.chemical_composition[7] = -3.8
    
    assert param.chemical_composition["N"] == -3.8
    assert param.chemical_composition[7]   == -3.8

def test_iterate_composition():
    param = parameters.Parameters()

    x = {k:param.chemical_composition[k] for k in param.chemical_composition}
    assert x[1] == 0.9204
    assert x[100] == None