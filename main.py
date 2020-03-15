#!/usr/bin/env python3

from vidmapy.kurucz import atlas
from vidmapy.kurucz import parameters
from vidmapy.kurucz import model

def main():
    p = parameters.Parameters()

    # atlas_code = atlas.Atlas(p)
    x = model.Model("/home/tr/repos/vidmapy/tests/test_data/model.txt")
    print(x._parameters)
    print("END")

if __name__ == '__main__':
    main()