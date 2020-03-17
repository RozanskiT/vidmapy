#!/usr/bin/env python3

import copy
"""
"""
class Parameters:
    def __init__(self, teff=5777, logg=4.44, metallicity=0.0, microturbulence=2.0):
        self.teff = teff
        self.logg = logg
        self.metallicity = metallicity
        self.microturbulence = microturbulence
        self.chemical_composition = Composition(_reference_composition)

        self.no_of_atlas_iterations = 15

    def update_chemical_composition(self, composition_dict):
        for atom_symbol in composition_dict:
            self.chemical_composition[atom_symbol] = composition_dict[atom_symbol]

    def __eq__(self, other):
        return self.teff == other.teff and\
               self.logg == other.logg and\
               self.metallicity == other.metallicity and\
               self.microturbulence == other.microturbulence and\
               self.chemical_composition == other.chemical_composition

class Composition:
    def __init__(self, reference_composition):
        # reference_composition :
        # [(  1, 0.9204 , 'H ', 'Hydrogen'), ... ,(104, None   , 'Rf', 'Rutherfordium'), ...]

        self._atoms_data = copy.deepcopy(reference_composition)
        self._index = {**{        x[0] : idx for idx, x in enumerate(self._atoms_data)},\
                       **{x[2].strip() : idx for idx, x in enumerate(self._atoms_data)}}

    def _get_record(self, key, index):
        return self._atoms_data[self._index[key]][index]

    def _set_record(self, key, data, index):
        self._atoms_data[self._index[key]][index] = data

    def __getitem__(self, key):
        return self._get_record(key, index=1)

    def __setitem__(self, key, data):
        self._set_record(key, data, index=1)

    def __iter__(self):
        return iter({ x[0]:x[1] for x in self._atoms_data})

    def __eq__(self, other):
        return all( [ other[x[0]] == self[x[0]] for x in self._atoms_data] )

_reference_composition = [
    [  1, 0.9204 , 'H' , 'Hydrogen'],
    [  2, 0.07834, 'He', 'Helium'],
    [  3, -10.94 , 'Li', 'Lithium'],
    [  4, -10.64 , 'Be', 'Beryllium'],
    [  5, -9.49  , 'B' , 'Boron'],
    [  6, -3.52  , 'C' , 'Carbon'],
    [  7, -4.12  , 'N' , 'Nitrogen'],
    [  8, -3.21  , 'O' , 'Oxygen'],
    [  9, -7.48  , 'F' , 'Fluorine'],
    [ 10, -3.96  , 'Ne', 'Neon'],
    [ 11, -5.71  , 'Na', 'Sodium'],
    [ 12, -4.46  , 'Mg', 'Magnesium'],
    [ 13, -5.57  , 'Al', 'Aluminum'],
    [ 14, -4.49  , 'Si', 'Silicon'],
    [ 15, -6.59  , 'P' , 'Phosphorus'],
    [ 16, -4.71  , 'S' , 'Sulfur'],
    [ 17, -6.54  , 'Cl', 'Chlorine'],
    [ 18, -5.64  , 'Ar', 'Argon'],
    [ 19, -6.92  , 'K' , 'Potassium'],
    [ 20, -5.68  , 'Ca', 'Calcium'],
    [ 21, -8.87  , 'Sc', 'Scandium'],
    [ 22, -7.02  , 'Ti', 'Titanium'],
    [ 23, -8.04  , 'V' , 'Vanadium'],
    [ 24, -6.37  , 'Cr', 'Chromium'],
    [ 25, -6.65  , 'Mn', 'Manganese'],
    [ 26, -4.54  , 'Fe', 'Iron'],
    [ 27, -7.12  , 'Co', 'Cobalt'],
    [ 28, -5.79  , 'Ni', 'Nickel'],
    [ 29, -7.83  , 'Cu', 'Copper'],
    [ 30, -7.44  , 'Zn', 'Zinc'],
    [ 31, -9.16  , 'Ga', 'Gallium'],
    [ 32, -8.63  , 'Ge', 'Germanium'],
    [ 33, -9.67  , 'As', 'Arsenic'],
    [ 34, -8.63  , 'Se', 'Selenium'],
    [ 35, -9.41  , 'Br', 'Bromine'],
    [ 36, -8.73  , 'Kr', 'Krypton'],
    [ 37, -9.44  , 'Rb', 'Rubidium'],
    [ 38, -9.07  , 'Sr', 'Strontium'],
    [ 39, -9.8   , 'Y' , 'Yttrium'],
    [ 40, -9.44  , 'Zr', 'Zirconium'],
    [ 41, -10.62 , 'Nb', 'Niobium'],
    [ 42, -10.12 , 'Mo', 'Molybdenum'],
    [ 43, -20.0  , 'Tc', 'Technetium'],
    [ 44, -10.2  , 'Ru', 'Ruthenium'],
    [ 45, -10.92 , 'Rh', 'Rhodium'],
    [ 46, -10.35 , 'Pd', 'Palladium'],
    [ 47, -11.1  , 'Ag', 'Silver'],
    [ 48, -10.27 , 'Cd', 'Cadmium'],
    [ 49, -10.38 , 'In', 'Indium'],
    [ 50, -10.04 , 'Sn', 'Tin'],
    [ 51, -11.04 , 'Sb', 'Antimony'],
    [ 52, -9.8   , 'Te', 'Tellurium'],
    [ 53, -10.53 , 'I' , 'Iodine'],
    [ 54, -9.87  , 'Xe', 'Xenon'],
    [ 55, -10.91 , 'Cs', 'Cesium'],
    [ 56, -9.91  , 'Ba', 'Barium'],
    [ 57, -10.87 , 'La', 'Lanthanum'],
    [ 58, -10.46 , 'Ce', 'Cerium'],
    [ 59, -11.33 , 'Pr', 'Praseodymium'],
    [ 60, -10.54 , 'Nd', 'Neodymium'],
    [ 61, -20.0  , 'Pm', 'Promethium'],
    [ 62, -11.03 , 'Sm', 'Samarium'],
    [ 63, -11.53 , 'Eu', 'Europium'],
    [ 64, -10.92 , 'Gd', 'Gadolinium'],
    [ 65, -11.69 , 'Tb', 'Terbium'],
    [ 66, -10.9  , 'Dy', 'Dysprosium'],
    [ 67, -11.78 , 'Ho', 'Holmium'],
    [ 68, -11.11 , 'Er', 'Erbium'],
    [ 69, -12.04 , 'Tm', 'Thulium'],
    [ 70, -10.96 , 'Yb', 'Ytterbium'],
    [ 71, -11.98 , 'Lu', 'Lutetium'],
    [ 72, -11.16 , 'Hf', 'Hafnium'],
    [ 73, -12.17 , 'Ta', 'Tantalum'],
    [ 74, -10.93 , 'W' , 'Tungsten'],
    [ 75, -11.76 , 'Re', 'Rhenium'],
    [ 76, -10.59 , 'Os', 'Osmium'],
    [ 77, -10.69 , 'Ir', 'Iridium'],
    [ 78, -10.24 , 'Pt', 'Platinum'],
    [ 79, -11.03 , 'Au', 'Gold'],
    [ 80, -10.91 , 'Hg', 'Mercury'],
    [ 81, -11.14 , 'Tl', 'Thallium'],
    [ 82, -10.09 , 'Pb', 'Lead'],
    [ 83, -11.33 , 'Bi', 'Bismuth'],
    [ 84, -20.0  , 'Po', 'Polonium'],
    [ 85, -20.0  , 'At', 'Astatine'],
    [ 86, -20.0  , 'Rn', 'Radon'],
    [ 87, -20.0  , 'Fr', 'Francium'],
    [ 88, -20.0  , 'Ra', 'Radium'],
    [ 89, -20.0  , 'Ac', 'Actinium'],
    [ 90, -11.95 , 'Th', 'Thorium'],
    [ 91, -20.0  , 'Pa', 'Protactinium'],
    [ 92, -12.54 , 'U' , 'Uranium'],
    [ 93, -20.0  , 'Np', 'Neptunium'],
    [ 94, -20.0  , 'Pu', 'Plutonium'],
    [ 95, -20.0  , 'Am', 'Americium'],
    [ 96, -20.0  , 'Cm', 'Curium'],
    [ 97, -20.0  , 'Bk', 'Berkelium'],
    [ 98, -20.0  , 'Cf', 'Californium'],
    [ 99, -20.0  , 'Es', 'Einsteinium'],
    [100, None   , 'Fm', 'Fermium'],
    [101, None   , 'Md', 'Mendelevium'],
    [102, None   , 'No', 'Nobelium'],
    [103, None   , 'Lr', 'Lawrencium'],
    [104, None   , 'Rf', 'Rutherfordium'],
    [105, None   , 'Db', 'Dubnium'],
    [106, None   , 'Sg', 'Seaborgium'],
    [107, None   , 'Bh', 'Bohrium'],
    [108, None   , 'Hs', 'Hassium'],
    [109, None   , 'Mt', 'Meitnerium'],
    [110, None   , 'Ds', 'Darmstadtium'],
    [111, None   , 'Rg', 'Roentgenium'],
    [112, None   , 'Cn', 'Copernicium'],
    [113, None   , 'Nh', 'Nihonium'],
    [114, None   , 'Fl', 'Flerovium'],
    [115, None   , 'Mc', 'Moscovium'],
    [116, None   , 'Lv', 'Livermorium'],
    [117, None   , 'Ts', 'Tennessine'],
    [118, None   , 'Og', 'Oganesson']
    ]

def main():
    pass

if __name__ == '__main__':
    main()