#!/usr/bin/env python3

"""
"""

class Atlas:
    def __init__(self, parameters):
        self.parameters = parameters

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

    def get_model(self):
        with tempfile.TemporaryDirectory(prefix="atlas_") as tmpdirname:
            string_model = self._compute_model(tmpdirname)

        return string_model

    def _compute_model(self, tmpdirname):
        string_model = None
        return string_model

def main():
    pass

if __name__ == '__main__':
    main()