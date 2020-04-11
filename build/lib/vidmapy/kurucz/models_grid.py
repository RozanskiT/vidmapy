#!/usr/bin/env python3

"""
Class for getting string with best model from the grid of models:

eg.
    p = Parameters(teff=5000, logg=3.2)
    grid = Grid(grid_path)
    model_as_string = grid.get_best_model(p)
"""

from vidmapy.kurucz import model
import re

class Grid:
    def __init__(self, path):
        self._grid_data = None

        self._load_grid(path)
        self._split_models()

    def _load_grid(self, path):
        with open(path) as f:
            self._grid_data = f.read()
    
    def _split_models(self):
        _models_strings = []
        _models = []
        pattern = re.compile('^ *TEFF *(\d*[.]\d*) *GRAVITY *(\d*[.]\d*) *LTE')
        for line in self._grid_data.splitlines():
            if pattern.search(line):
                _models_strings.append([])
                teff_logg_pair = pattern.findall(line)[0]
                _models.append([float(x) for x in teff_logg_pair])
            _models_strings[-1].append(line)
        self._models = _models
        self._models_data = ['\n'.join(model_lines) for model_lines in _models_strings]
        
    def get_best_model(self, parameters):
        best_model = {'teff':0, 'logg':0, 'index':0}
        for i, (teff,logg) in enumerate(self._models):
            if abs(parameters.teff - teff) < abs(parameters.teff - best_model["teff"]):
                best_model['teff'] = teff
                best_model['logg'] = logg
                best_model['index'] = i
            if abs(parameters.teff - teff) == abs(parameters.teff - best_model["teff"]) and \
                      abs(parameters.logg - logg) < abs(parameters.logg - best_model["logg"]):
                best_model['logg'] = logg
                best_model['index'] = i
        return self._models_data[best_model["index"]]

def main():
    pass

if __name__ == '__main__':
    main()