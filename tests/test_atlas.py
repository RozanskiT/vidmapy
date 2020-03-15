from vidmapy.kurucz import atlas
import pytest 

from unittest.mock import MagicMock

@pytest.fixture
def atlas_model():
    parameters = MagicMock()
    parameters.teff = 5777
    parameters.logg = 4.44
    parameters.metallicity = 0.0
    return atlas.Atlas(parameters)

def test_raport_state(atlas_model):
    assert atlas_model.get_report() == "TEFF  =  5777\nLOGG  = 4.44\n[M/H] = 0.00"

def test_set_variables_with_setters(atlas_model):
    parameters = MagicMock()
    parameters.teff = 5000
    parameters.logg = 4.3
    parameters.metallicity = 1.0

    atlas_model.teff = parameters.teff
    atlas_model.logg = parameters.logg
    atlas_model.metallicity = parameters.metallicity

    assert atlas_model.teff == parameters.teff
    assert atlas_model.logg == parameters.logg
    assert atlas_model.metallicity == parameters.metallicity

def test_define_all_parameters_at_once(atlas_model):
    parameters = MagicMock()
    parameters.teff = 5000
    parameters.logg = 4.3
    parameters.metallicity = 1.0

    atlas_model.parameters = parameters
    
    assert atlas_model.teff == parameters.teff
    assert atlas_model.logg == parameters.logg
    assert atlas_model.metallicity == parameters.metallicity
