#!/usr/bin/env python3

from vidmapy.kurucz.atlas import Atlas
from vidmapy.kurucz.synthe import Synthe
from vidmapy.kurucz.parameters import Parameters

import matplotlib.pyplot as plt

def run_synthe():
    p = Parameters(teff=8000., 
                    logg=4.0, 
                    metallicity=0.0, 
                    microturbulence=2.0,
                    vsini = 20.,
                    wave_min = 4500,
                    wave_max = 5000,
                    resolution = 40000,
                    )

    wa = Atlas()
    m = wa.get_model(p)
    
    ws = Synthe()
    spectrum = ws.get_spectrum(m)

    print(spectrum.lines_identification.head())
    plt.plot(spectrum.wave, spectrum.normed_flux)
    plt.show()

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
    # run_atlas()
    run_synthe()

if __name__ == '__main__':
    main()