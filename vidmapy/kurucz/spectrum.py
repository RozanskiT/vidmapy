#!/usr/bin/env python3

"""
Implements class that contains all spectrum data:
- wave, flux, contrinuum, normed_flux
- parameters of spectrum         if availible
- lines identification dataframe if availible
"""


from vidmapy.kurucz.parameters import Parameters
from vidmapy.kurucz.utility_functions import _read_fixed_width_data
import numpy as np
import pandas as pd
import os


class Spectrum:
    def __init__(self):
        self.wave = None
        self.flux = None 
        self.continuum = None 
        self.normed_flux = None

        self.parameters = None

        self.lines_identification = None

    @classmethod
    def from_synthe_spectrum(cls, parameters, directory, spectrum_file_name="br_spec.dat", linelist_file_name="line_list.dat"):
        sp = cls()
        sp.read_lines_identification_file(os.path.join(directory,linelist_file_name))
        sp.read_spectrum_file(os.path.join(directory,spectrum_file_name))
        sp.parameters = parameters
        return sp

    def read_lines_identification_file(self, path):
        format_string = "++++++++++^^^^^^^+++++^^^^^^^^^^^^+++++^^^^^^^^^^^^+++++++++^^^^^^^^+++++++"
        column_names = ["wave","loggf?","J1?","E1?","J2?","E2?","atom_symbol","literature","strength"]
        self.lines_identification = _read_fixed_width_data(path, format_string, column_names=column_names)
        self.lines_identification["wave"] *= 10.
    
    def read_spectrum_file(self, path):
        df = pd.read_csv(path, header=None, index_col=False, delim_whitespace=True)
        self.wave = df[0]
        self.flux = df[1] 
        self.continuum = df[2] 
        self.normed_flux = df[3]

def main():
    pass

if __name__ == '__main__':
    main()