#!/usr/bin/env python3

from vidmapy.kurucz.atlas import Atlas
from vidmapy.kurucz.parameters import Parameters

import matplotlib.pyplot as plt

def run_atlas():
    worker = Atlas()
    m1 = worker.get_model(Parameters(8000., 4.0, 0.0, 2.0)) # from grid
    m2a = worker.get_model(Parameters(8120., 4.0, 0.0, 2.0)) # computed
    m2b = worker.get_model(Parameters(8130., 4.0, 0.0, 2.0)) # computed
    m3 = worker.get_model(Parameters(8250., 4.0, 0.0, 2.0)) # from grid

    plt.plot(m1.structure["RHOX"], m1.structure["T"],'k')

    plt.plot(m2a.structure["RHOX"], m2a.structure["T"],'g')
    plt.plot(m2b.structure["RHOX"], m2b.structure["T"],'b')
    
    plt.plot(m3.structure["RHOX"], m3.structure["T"],'k')
    plt.show()

def main():
    run_atlas()

if __name__ == '__main__':
    main()