#!/usr/bin/env python3

"""
Object of thas class represent atmospheric model:
- parameters
- structure

It is created from file:
    Model(model_path)
or from string or file with extended parameters set:
    Model.from_string(model_string, parameters)
    Model.with_extended_set_of_parameters(path, parameters)
"""

from vidmapy.kurucz.parameters import Parameters
import re
import io
import numpy as np
import copy

class Model:
    _number_regexp = '[-+]?[0-9]*\.?[0-9]+(?:[eE][-+]?[0-9]+)?'

    def __init__(self, path=None):
        self._parameters = Parameters()
        self._depth_dependend_data = None
        
        self._pradk = None
        self._title = None
        self._no_of_depth_points = None
        self._columns_of_depth_dependent_data = None

        if path is not None:
            self._open_model(path)

    @classmethod
    def from_string(cls, model_string, parameters):
        model = cls()
        model._parameters = copy.deepcopy(parameters)
        model.model_from_string(model_string)
        return model

    @classmethod
    def with_extended_set_of_parameters(cls, path, parameters):
        model = cls()
        model._parameters = copy.deepcopy(parameters)
        model._open_model(path)
        return model

    @property
    def parameters(self):
        return self._parameters

    @property
    def teff(self):
        return self._parameters.teff

    @property
    def logg(self):
        return self._parameters.logg
    
    @property
    def metallicity(self):
        return self._parameters.metallicity

    @property
    def chemical_composition(self):
        return self._parameters.chemical_composition

    @property
    def title(self):
        return self._title

    @property
    def structure(self):
        return {k : self._depth_dependend_data[i,:] for i, k in enumerate(self._columns_of_depth_dependent_data)}

    @property
    def pradk(self):
        return self._pradk

    def __str__(self):
        s = [
            "================================\n",
            f"TEFF  = {self.teff}\n",
            f"LOGG  = {self.logg}\n",
            f"[M/H] = {self.metallicity}\n",
            f"TITLE : {self.title}\n"
            "--------------------------------\n",
        ]
        return "".join(s)

    def __repr__(self):
        return f"({self.teff}, {self.logg}, {self.metallicity})"

    def __eq__(self, other):
        return self._parameters == other._parameters

    def is_model_has_this(self, parameters):
        return self._parameters == parameters

    def model_from_string(self, string):
        self._read_model(io.StringIO(string))

    def save_model(self, path):
        model_string = self.get_model_string()
        with open(path,'w') as f:
            f.write(model_string)

    def _open_model(self, path):
        with open(path, 'r') as f:
            self._read_model(f)

    def _read_model(self, file_object):
        reading_depth_dependent_data = {"reading_state":False, "no_of_read_lines":0}

        def read_line_of_depth_dependent_data():
            self._depth_dependend_data.append(self._read_row_data(line))
            reading_depth_dependent_data["no_of_read_lines"] += 1
            if reading_depth_dependent_data["no_of_read_lines"] == self._no_of_depth_points:
                self._depth_dependend_data = np.array(self._depth_dependend_data).T
                reading_depth_dependent_data["reading_state"] = False

        def read_model_paramters():
            if "TEFF" in line:
                self._parameters.teff = self._extract_teff(line)
            if "GRAVITY" in line:
                self._parameters.logg = self._extract_logg(line)
            if "TITLE" in line:
                self._title = self._extract_title(line)
            if "ABUNDANCE SCALE" in line:
                self._parameters.metallicity = self._extract_metallicity(line)
            if "ABUNDANCE CHANGE" in line:
                self._parameters.update_chemical_composition(self._extract_chemical_composition(line))
            if "READ DECK" in line:
                self._no_of_depth_points = self._extract_no_of_depth_points(line)
                self._columns_of_depth_dependent_data = self._extract_columns_names(line)
                reading_depth_dependent_data["reading_state"] = True
                self._depth_dependend_data = []
            if "PRADK" in line:
                self._pradk = self._extract_PRADK(line)

        for line in file_object:
            line = line.strip()
            if reading_depth_dependent_data["reading_state"]:
                read_line_of_depth_dependent_data()
            else:
                read_model_paramters()
                
    def _extract_teff(self, line):
        return self._read_first_number_after_word("TEFF", line)

    def _extract_logg(self, line):
        return self._read_first_number_after_word("GRAVITY", line)

    def _extract_no_of_depth_points(self, line):
        return self._read_first_number_after_word("DECK6", line)

    def _extract_PRADK(self, line):
        return self._read_first_number_after_word("PRADK", line)
    
    def _extract_metallicity(self, line):
        return np.log10(self._read_first_number_after_word("ABUNDANCE SCALE", line))

    def _read_first_number_after_word(self, word, line):
        x = re.findall(f"{word}.*?({self._number_regexp})", line)
        if x:
            if '.' in x[0] or 'e' in x[0].lower():
                return float(x[0].strip())
            else:
                return int(x[0].strip())
        return None
        
    def _extract_title(self, line):
        x = re.findall(f"TITLE(.*)$", line)
        if x:
            return x[0].strip()
        return None

    def _extract_chemical_composition(self, line):
        x = re.findall(f"{self._number_regexp}", re.sub(r".*ABUNDANCE CHANGE","",line))
        if x:
            return {int(atomic_symbol): float(abundance) for atomic_symbol, abundance in zip(x[0::2], x[1::2])}
        return None

    def _extract_columns_names(self,line):
        column_names = re.sub(r".*READ DECK6 *\d*","", line).split(',')
        return [x.strip() for x in column_names]

    def _read_row_data(self, line):
        return [float(x) for x in line.split()]

    def get_model_string(self):
        model_header = [
        f"TEFF {self.teff:6.0f}.  GRAVITY {self.logg:7.5f} LTE\n", 
        f"TITLE {self._title}\n",                                   
        " OPACITY IFOP 1 1 1 1 1 1 1 1 1 1 1 1 1 0 1 0 0 0 0 0\n",
        " CONVECTION ON   1.25 TURBULENCE OFF  0.00  0.00  0.00  0.00\n",
        # f"ABUNDANCE SCALE   {10.**self.metallicity:7.5f}\n",
        ]
        # model_abundances = self._get_abundances_definition()
        model_abundances = self._get_metallicity_and_abundance_lines()
        model_depth_data_header = ["READ DECK6 72 RHOX,T,P,XNE,ABROSS,ACCRAD,VTURB, FLXCNV,VCONV,VELSND\n"]
        model_depth_data = self._get_depth_dependent_data()
        model_footer = [
            f"PRADK {self._pradk:10.4E}\n",
            "BEGIN                    ITERATION  15 COMPLETED\n"
        ]
        return "".join(model_header + model_abundances + model_depth_data_header + model_depth_data + model_footer)

    def _get_abundances_definition(self):
        model_abundances = []
        for atom_symbol in self._parameters.chemical_composition:
            if atom_symbol<100:
                model_abundances.append(self._get_abundance_line(atom_symbol, self._parameters.chemical_composition[atom_symbol]))
        return model_abundances

    def _get_abundance_line(self, atom_symbol, abundace):
        if atom_symbol == 1 or atom_symbol == 2: # special treating - following ATLAS
            abundance_line = f" ABUNDANCE CHANGE {atom_symbol:^2d}{abundace:7.5f}\n"
        else:
            abundance_line = f" ABUNDANCE CHANGE {atom_symbol:^2d} {abundace:6.2f}\n"
        return abundance_line

    def _get_metallicity_and_abundance_lines(self):
        ch = self._parameters.chemical_composition
        s = [
        f"ABUNDANCE SCALE   {10.**self.metallicity:7.5f} ABUNDANCE CHANGE 1 {ch[1]:7.5f} 2 {ch[2]:7.5f}\n",
        f" ABUNDANCE CHANGE  3 {ch[3]:6.2f}  4 {ch[3+1]:6.2f}  5 {ch[3+2]:6.2f}  6 {ch[3+3]:6.2f}  7 {ch[3+4]:6.2f}  8 {ch[3+5]:6.2f}\n",
        f" ABUNDANCE CHANGE  9 {ch[9]:6.2f} 10 {ch[9+1]:6.2f} 11 {ch[9+2]:6.2f} 12 {ch[9+3]:6.2f} 13 {ch[9+4]:6.2f} 14 {ch[9+5]:6.2f}\n",
        f" ABUNDANCE CHANGE 15 {ch[15]:6.2f} 16 {ch[15+1]:6.2f} 17 {ch[15+2]:6.2f} 18 {ch[15+3]:6.2f} 19 {ch[15+4]:6.2f} 20 {ch[15+5]:6.2f}\n",
        f" ABUNDANCE CHANGE 21 {ch[21]:6.2f} 22 {ch[21+1]:6.2f} 23 {ch[21+2]:6.2f} 24 {ch[21+3]:6.2f} 25 {ch[21+4]:6.2f} 26 {ch[21+5]:6.2f}\n",
        f" ABUNDANCE CHANGE 27 {ch[27]:6.2f} 28 {ch[27+1]:6.2f} 29 {ch[27+2]:6.2f} 30 {ch[27+3]:6.2f} 31 {ch[27+4]:6.2f} 32 {ch[27+5]:6.2f}\n",
        f" ABUNDANCE CHANGE 33 {ch[33]:6.2f} 34 {ch[33+1]:6.2f} 35 {ch[33+2]:6.2f} 36 {ch[33+3]:6.2f} 37 {ch[33+4]:6.2f} 38 {ch[33+5]:6.2f}\n",
        f" ABUNDANCE CHANGE 39 {ch[39]:6.2f} 40 {ch[39+1]:6.2f} 41 {ch[39+2]:6.2f} 42 {ch[39+3]:6.2f} 43 {ch[39+4]:6.2f} 44 {ch[39+5]:6.2f}\n",
        f" ABUNDANCE CHANGE 45 {ch[45]:6.2f} 46 {ch[45+1]:6.2f} 47 {ch[45+2]:6.2f} 48 {ch[45+3]:6.2f} 49 {ch[45+4]:6.2f} 50 {ch[45+5]:6.2f}\n",
        f" ABUNDANCE CHANGE 51 {ch[51]:6.2f} 52 {ch[51+1]:6.2f} 53 {ch[51+2]:6.2f} 54 {ch[51+3]:6.2f} 55 {ch[51+4]:6.2f} 56 {ch[51+5]:6.2f}\n",
        f" ABUNDANCE CHANGE 57 {ch[57]:6.2f} 58 {ch[57+1]:6.2f} 59 {ch[57+2]:6.2f} 60 {ch[57+3]:6.2f} 61 {ch[57+4]:6.2f} 62 {ch[57+5]:6.2f}\n",
        f" ABUNDANCE CHANGE 63 {ch[63]:6.2f} 64 {ch[63+1]:6.2f} 65 {ch[63+2]:6.2f} 66 {ch[63+3]:6.2f} 67 {ch[63+4]:6.2f} 68 {ch[63+5]:6.2f}\n",
        f" ABUNDANCE CHANGE 69 {ch[69]:6.2f} 70 {ch[69+1]:6.2f} 71 {ch[69+2]:6.2f} 72 {ch[69+3]:6.2f} 73 {ch[69+4]:6.2f} 74 {ch[69+5]:6.2f}\n",
        f" ABUNDANCE CHANGE 75 {ch[75]:6.2f} 76 {ch[75+1]:6.2f} 77 {ch[75+2]:6.2f} 78 {ch[75+3]:6.2f} 79 {ch[75+4]:6.2f} 80 {ch[75+5]:6.2f}\n",
        f" ABUNDANCE CHANGE 81 {ch[81]:6.2f} 82 {ch[81+1]:6.2f} 83 {ch[81+2]:6.2f} 84 {ch[81+3]:6.2f} 85 {ch[81+4]:6.2f} 86 {ch[81+5]:6.2f}\n",
        f" ABUNDANCE CHANGE 87 {ch[87]:6.2f} 88 {ch[87+1]:6.2f} 89 {ch[87+2]:6.2f} 90 {ch[87+3]:6.2f} 91 {ch[87+4]:6.2f} 92 {ch[87+5]:6.2f}\n",
        f" ABUNDANCE CHANGE 93 {ch[93]:6.2f} 94 {ch[93+1]:6.2f} 95 {ch[93+2]:6.2f} 96 {ch[93+3]:6.2f} 97 {ch[93+4]:6.2f} 98 {ch[93+5]:6.2f}\n",
        f" ABUNDANCE CHANGE 99 {ch[99]:6.2f}\n",
        ]
        return s

    def _get_depth_dependent_data(self):
        model_depth_data = []
        for row in self._depth_dependend_data.T:
            len(row)
            model_depth_data.append(self._get_structure_line(row))
        return model_depth_data

    def _get_structure_line(self, row):
        return " {:14.8E} {:8.1f} {:9.3E} {:9.3E} {:9.3E} {:9.3E} {:9.3E} {:9.3E} {:9.3E} {:9.3E}\n".format(*row)


def main():
    pass

if __name__ == '__main__':
    main()