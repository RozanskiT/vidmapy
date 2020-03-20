#!/usr/bin/env python3

"""
Implements easy-to-use interface to Kurucz's ATLAS code

Needs to be use together with class Parameters.
eg.
    p = Parameters() # All default

    wa = Atlas()
    m = wa.get_model(p)
"""

from vidmapy.kurucz.model import Model
from vidmapy.kurucz.models_grid import Grid
from vidmapy.kurucz.model_definition import ModelDefinition
from vidmapy.kurucz.parameters import Parameters
import os
import subprocess
import tempfile
import copy
import stat

class Atlas:
    def __init__(self):
        self.parameters = Parameters()
        self._kurucz_directory = os.path.dirname(os.path.abspath(__file__))
        self.default_grid = os.path.join(self._kurucz_directory,"grids","ap00k2odfnew.txt")
        self.set_grid(path=self.default_grid)
        
        self._kurucz_bin_path = self._kurucz_directory
        self._atomic_data_path = os.path.join(self._kurucz_directory,"atomic_data")
        # self._kurucz_bin_path = "/usr/local/kurucz/"
        self._atlas_name = "atlas9mem_newodf.exe"

    def get_report(self):
        return f"TEFF  = {self.parameters.teff:5.0f}\n"\
               f"LOGG  = {self.parameters.logg:4.2f}\n"\
               f"[M/H] = {self.parameters.metallicity:4.2f}"

    @property
    def teff(self):
        return self.parameters.teff
        
    @property
    def logg(self):
        return self.parameters.logg

    @property
    def metallicity(self):
        return self.parameters.metallicity  

    @teff.setter
    def teff(self, teff):
        self.parameters.teff = teff

    @logg.setter
    def logg(self, logg):
        self.parameters.logg = logg

    @metallicity.setter
    def metallicity(self, metallicity):
        self.parameters.metallicity = metallicity

    def set_grid(self, path):
        self._grid = Grid(path)

    def get_model(self, parameters):
        self.parameters = copy.deepcopy(parameters)
        initial_model = self._get_initial_model()
        if initial_model.is_model_has_this(self.parameters):
            return initial_model
        else:
            return self._create_temporary_directory_and_run_ATLAS(initial_model)

    def _get_initial_model(self):
        model_as_string = self._grid.get_best_model(self.parameters)
        return Model.from_string(model_as_string, self.parameters)

    def _create_temporary_directory_and_run_ATLAS(self, initial_model):
        with tempfile.TemporaryDirectory(prefix="atlas_") as tmpdirname:
            model = self._compute_model(tmpdirname, initial_model)
        return model

    def _compute_model(self, tmpdirname, initial_model):
        md = ModelDefinition()
        # Link necessary data:
        os.symlink(os.path.join(self._atomic_data_path,"ODF","NEW","kapp02.ros"), os.path.join(tmpdirname,"fort.1"))
        os.symlink(os.path.join(self._atomic_data_path,"ODF","NEW","p00big2.bdf"), os.path.join(tmpdirname,"fort.9"))
        os.symlink(os.path.join(self._atomic_data_path,"lines","molecules.dat"), os.path.join(tmpdirname,"fort.2"))
        # Create intial model:
        initial_model.save_model(os.path.join(tmpdirname, "fort.3"))
        
        # Run ATLAS
        process = subprocess.Popen([os.path.join(self._kurucz_bin_path, "bin", self._atlas_name)],
                                    stdin=subprocess.PIPE,
                                    stdout=subprocess.PIPE,
                                    encoding='utf8',
                                    cwd=tmpdirname)
        outs, errs = process.communicate(md(self.parameters))
        process.wait()
        
        return Model.with_extended_set_of_parameters(os.path.join(tmpdirname,"fort.7"), self.parameters)

def main():
    pass

if __name__ == '__main__':
    main()