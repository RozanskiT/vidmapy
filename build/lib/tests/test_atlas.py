from vidmapy.kurucz import atlas
import pytest 

from unittest.mock import MagicMock

@pytest.fixture
def atlas_model():

    return atlas.Atlas()

def test_raport_state(atlas_model):
    parameters = MagicMock()
    parameters.teff = 5777
    parameters.logg = 4.44
    parameters.metallicity = 0.0
    atlas_model.parameters = parameters
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



grid_text =\
"""TEFF   7750.  GRAVITY 3.50000 LTE 
TITLE  [-1.0] VTURB=2  L/H=1.25 NOVER NEW ODF                                   
 OPACITY IFOP 1 1 1 1 1 1 1 1 1 1 1 1 1 0 1 0 0 0 0 0
 CONVECTION ON   1.25 TURBULENCE OFF  0.00  0.00  0.00  0.00
ABUNDANCE SCALE   0.10000 ABUNDANCE CHANGE 1 0.92140 2 0.07843
 ABUNDANCE CHANGE  3 -10.94  4 -10.64  5  -9.49  6  -3.52  7  -4.12  8  -3.21
 ABUNDANCE CHANGE  9  -7.48 10  -3.96 11  -5.71 12  -4.46 13  -5.57 14  -4.49
 ABUNDANCE CHANGE 15  -6.59 16  -4.71 17  -6.54 18  -5.64 19  -6.92 20  -5.68
 ABUNDANCE CHANGE 21  -8.87 22  -7.02 23  -8.04 24  -6.37 25  -6.65 26  -4.54
 ABUNDANCE CHANGE 27  -7.12 28  -5.79 29  -7.83 30  -7.44 31  -9.16 32  -8.63
 ABUNDANCE CHANGE 33  -9.67 34  -8.63 35  -9.41 36  -8.73 37  -9.44 38  -9.07
 ABUNDANCE CHANGE 39  -9.80 40  -9.44 41 -10.62 42 -10.12 43 -20.00 44 -10.20
 ABUNDANCE CHANGE 45 -10.92 46 -10.35 47 -11.10 48 -10.27 49 -10.38 50 -10.04
 ABUNDANCE CHANGE 51 -11.04 52  -9.80 53 -10.53 54  -9.87 55 -10.91 56  -9.91
 ABUNDANCE CHANGE 57 -10.87 58 -10.46 59 -11.33 60 -10.54 61 -20.00 62 -11.03
 ABUNDANCE CHANGE 63 -11.53 64 -10.92 65 -11.69 66 -10.90 67 -11.78 68 -11.11
 ABUNDANCE CHANGE 69 -12.04 70 -10.96 71 -11.98 72 -11.16 73 -12.17 74 -10.93
 ABUNDANCE CHANGE 75 -11.76 76 -10.59 77 -10.69 78 -10.24 79 -11.03 80 -10.91
 ABUNDANCE CHANGE 81 -11.14 82 -10.09 83 -11.33 84 -20.00 85 -20.00 86 -20.00
 ABUNDANCE CHANGE 87 -20.00 88 -20.00 89 -20.00 90 -11.95 91 -20.00 92 -12.54
 ABUNDANCE CHANGE 93 -20.00 94 -20.00 95 -20.00 96 -20.00 97 -20.00 98 -20.00
 ABUNDANCE CHANGE 99 -20.00
READ DECK6 72 RHOX,T,P,XNE,ABROSS,ACCRAD,VTURB, FLXCNV,VCONV,VELSND
 5.67130439E-05   4913.9 1.793E-01 1.508E+09 2.351E-03 3.251E-01 2.000E+05 0.000E+00 0.000E+00 2.948E+06
 7.59239944E-05   4941.4 2.401E-01 1.911E+09 2.279E-03 3.195E-01 2.000E+05 0.000E+00 0.000E+00 2.619E+06
 1.02367353E-04   4969.0 3.237E-01 2.429E+09 2.207E-03 3.118E-01 2.000E+05 0.000E+00 0.000E+00 2.326E+06
 1.38539351E-04   5000.6 4.381E-01 3.130E+09 2.166E-03 3.032E-01 2.000E+05 0.000E+00 0.000E+00 2.063E+06
 1.87420200E-04   5035.4 5.926E-01 4.068E+09 2.153E-03 2.936E-01 2.000E+05 0.000E+00 0.000E+00 1.833E+06
 2.52627539E-04   5072.0 7.988E-01 5.299E+09 2.163E-03 2.837E-01 2.000E+05 0.000E+00 0.000E+00 1.636E+06
 3.38766128E-04   5109.8 1.071E+00 6.898E+09 2.193E-03 2.740E-01 2.000E+05 0.000E+00 0.000E+00 1.469E+06
 4.51528668E-04   5148.2 1.428E+00 8.953E+09 2.244E-03 2.648E-01 2.000E+05 0.000E+00 0.000E+00 1.330E+06
 5.97887688E-04   5186.8 1.891E+00 1.157E+10 2.314E-03 2.561E-01 2.000E+05 0.000E+00 0.000E+00 1.215E+06
 7.86272730E-04   5225.3 2.486E+00 1.487E+10 2.407E-03 2.479E-01 2.000E+05 0.000E+00 0.000E+00 1.120E+06
 1.02673043E-03   5263.7 3.247E+00 1.901E+10 2.525E-03 2.400E-01 2.000E+05 0.000E+00 0.000E+00 1.042E+06
 1.33116832E-03   5301.5 4.209E+00 2.413E+10 2.669E-03 2.329E-01 2.000E+05 0.000E+00 0.000E+00 9.796E+05
 1.71401524E-03   5338.1 5.420E+00 3.038E+10 2.838E-03 2.264E-01 2.000E+05 0.000E+00 0.000E+00 9.291E+05
 2.19288474E-03   5373.1 6.934E+00 3.790E+10 3.033E-03 2.209E-01 2.000E+05 0.000E+00 0.000E+00 8.888E+05
 2.78891293E-03   5406.5 8.819E+00 4.688E+10 3.258E-03 2.172E-01 2.000E+05 0.000E+00 0.000E+00 8.567E+05
 3.52698149E-03   5438.7 1.115E+01 5.757E+10 3.518E-03 2.153E-01 2.000E+05 0.000E+00 0.000E+00 8.312E+05
 4.43546875E-03   5470.2 1.403E+01 7.029E+10 3.823E-03 2.152E-01 2.000E+05 0.000E+00 0.000E+00 8.111E+05
 5.54598129E-03   5501.6 1.754E+01 8.548E+10 4.186E-03 2.164E-01 2.000E+05 0.000E+00 0.000E+00 7.952E+05
 6.89314141E-03   5533.4 2.180E+01 1.037E+11 4.619E-03 2.187E-01 2.000E+05 0.000E+00 0.000E+00 7.828E+05
 8.51468572E-03   5566.0 2.692E+01 1.254E+11 5.136E-03 2.219E-01 2.000E+05 0.000E+00 0.000E+00 7.731E+05
 1.04522782E-02   5599.5 3.305E+01 1.515E+11 5.750E-03 2.260E-01 2.000E+05 0.000E+00 0.000E+00 7.657E+05
 1.27525313E-02   5633.9 4.032E+01 1.826E+11 6.478E-03 2.313E-01 2.000E+05 0.000E+00 0.000E+00 7.601E+05
 1.54676249E-02   5669.2 4.891E+01 2.198E+11 7.337E-03 2.375E-01 2.000E+05 0.000E+00 0.000E+00 7.560E+05
 1.86575147E-02   5705.4 5.900E+01 2.641E+11 8.344E-03 2.445E-01 2.000E+05 0.000E+00 0.000E+00 7.530E+05
 2.23905479E-02   5742.5 7.080E+01 3.169E+11 9.525E-03 2.523E-01 2.000E+05 0.000E+00 0.000E+00 7.509E+05
 2.67459770E-02   5780.0 8.457E+01 3.793E+11 1.090E-02 2.613E-01 2.000E+05 0.000E+00 0.000E+00 7.495E+05
 3.18168832E-02   5818.1 1.006E+02 4.531E+11 1.249E-02 2.715E-01 2.000E+05 0.000E+00 0.000E+00 7.488E+05
 3.77125574E-02   5856.4 1.192E+02 5.398E+11 1.433E-02 2.831E-01 2.000E+05 0.000E+00 0.000E+00 7.486E+05
 4.45639180E-02   5894.7 1.409E+02 6.414E+11 1.645E-02 2.958E-01 2.000E+05 0.000E+00 0.000E+00 7.488E+05
 5.25308837E-02   5932.3 1.661E+02 7.593E+11 1.885E-02 3.096E-01 2.000E+05 0.000E+00 0.000E+00 7.494E+05
 6.18118160E-02   5969.0 1.954E+02 8.951E+11 2.155E-02 3.249E-01 2.000E+05 0.000E+00 0.000E+00 7.503E+05
 7.26535655E-02   6004.1 2.297E+02 1.050E+12 2.456E-02 3.418E-01 2.000E+05 0.000E+00 0.000E+00 7.514E+05
 8.53579896E-02   6037.8 2.699E+02 1.226E+12 2.791E-02 3.610E-01 2.000E+05 0.000E+00 0.000E+00 7.528E+05
 1.00289966E-01   6070.0 3.171E+02 1.427E+12 3.162E-02 3.827E-01 2.000E+05 0.000E+00 0.000E+00 7.545E+05
 1.17880276E-01   6101.1 3.727E+02 1.655E+12 3.577E-02 4.080E-01 2.000E+05 0.000E+00 0.000E+00 7.563E+05
 1.38630640E-01   6131.5 4.383E+02 1.916E+12 4.042E-02 4.366E-01 2.000E+05 0.000E+00 0.000E+00 7.583E+05
 1.63122680E-01   6161.8 5.158E+02 2.217E+12 4.567E-02 4.693E-01 2.000E+05 0.000E+00 0.000E+00 7.604E+05
 1.92028305E-01   6192.0 6.072E+02 2.564E+12 5.161E-02 5.069E-01 2.000E+05 0.000E+00 0.000E+00 7.627E+05
 2.26110491E-01   6222.8 7.149E+02 2.967E+12 5.842E-02 5.504E-01 2.000E+05 0.000E+00 0.000E+00 7.650E+05
 2.66227410E-01   6254.8 8.418E+02 3.440E+12 6.625E-02 6.008E-01 2.000E+05 0.000E+00 0.000E+00 7.674E+05
 3.13332878E-01   6288.4 9.907E+02 3.998E+12 7.535E-02 6.601E-01 2.000E+05 0.000E+00 0.000E+00 7.698E+05
 3.68433675E-01   6324.7 1.165E+03 4.665E+12 8.611E-02 7.314E-01 2.000E+05 0.000E+00 0.000E+00 7.723E+05
 4.32561527E-01   6364.4 1.368E+03 5.473E+12 9.894E-02 8.176E-01 2.000E+05 0.000E+00 0.000E+00 7.759E+05
 5.06718700E-01   6408.9 1.602E+03 6.467E+12 1.145E-01 9.237E-01 2.000E+05 0.000E+00 0.000E+00 7.773E+05
 5.91760464E-01   6459.5 1.871E+03 7.711E+12 1.338E-01 1.057E+00 2.000E+05 0.000E+00 0.000E+00 7.797E+05
 6.88223926E-01   6518.5 2.176E+03 9.306E+12 1.583E-01 1.229E+00 2.000E+05 0.000E+00 0.000E+00 7.820E+05
 7.96112516E-01   6588.2 2.517E+03 1.140E+13 1.903E-01 1.457E+00 2.000E+05 0.000E+00 0.000E+00 7.842E+05
 9.14588798E-01   6672.0 2.891E+03 1.424E+13 2.336E-01 1.768E+00 2.000E+05 0.000E+00 0.000E+00 7.863E+05
 1.04176782E+00   6773.0 3.293E+03 1.818E+13 2.938E-01 2.206E+00 2.000E+05 0.000E+00 0.000E+00 7.883E+05
 1.17463267E+00   6895.3 3.713E+03 2.382E+13 3.808E-01 2.847E+00 2.000E+05 0.000E+00 0.000E+00 7.901E+05
 1.30906000E+00   7042.9 4.138E+03 3.208E+13 5.109E-01 3.817E+00 2.000E+05 7.555E-16 1.077E+01 7.920E+05
 1.43987599E+00   7221.9 4.551E+03 4.458E+13 7.158E-01 5.359E+00 2.000E+05 2.334E-11 3.210E+02 7.943E+05
 1.56144119E+00   7437.2 4.934E+03 6.391E+13 1.053E+00 7.920E+00 2.000E+05 7.693E-10 9.758E+02 7.977E+05
 1.66858288E+00   7695.6 5.272E+03 9.455E+13 1.640E+00 1.240E+01 2.000E+05 2.571E-08 2.977E+03 8.034E+05
 1.75735487E+00   8004.2 5.552E+03 1.440E+14 2.721E+00 2.064E+01 2.000E+05 1.197E-06 1.014E+04 8.134E+05
 1.82707038E+00   8357.4 5.770E+03 2.212E+14 4.726E+00 3.579E+01 2.000E+05 7.916E-05 3.911E+04 8.293E+05
 1.87845399E+00   8789.9 5.930E+03 3.498E+14 8.870E+00 6.706E+01 2.000E+05 2.348E-03 1.166E+05 8.560E+05
 1.91372126E+00   9308.9 6.038E+03 5.558E+14 1.736E+01 1.236E+02 2.000E+05 1.854E-02 2.262E+05 8.994E+05
 1.93934648E+00   9788.7 6.116E+03 7.888E+14 2.914E+01 1.682E+02 2.000E+05 1.949E-01 5.079E+05 9.515E+05
 1.96214696E+00  10159.1 6.184E+03 9.842E+14 4.024E+01 1.704E+02 2.000E+05 3.844E-01 6.559E+05 9.994E+05
 1.98547559E+00  10473.4 6.254E+03 1.149E+15 4.991E+01 1.625E+02 2.000E+05 5.124E-01 7.404E+05 1.045E+06
 2.01122143E+00  10795.1 6.331E+03 1.307E+15 5.904E+01 1.616E+02 2.000E+05 5.913E-01 8.037E+05 1.094E+06
 2.04090915E+00  11144.3 6.420E+03 1.454E+15 6.671E+01 1.735E+02 2.000E+05 6.009E-01 8.334E+05 1.149E+06
 2.07711782E+00  11578.3 6.527E+03 1.591E+15 7.028E+01 2.361E+02 2.000E+05 5.502E-01 8.940E+05 1.216E+06
 2.12690157E+00  12428.9 6.670E+03 1.710E+15 6.269E+01 3.344E+02 2.000E+05 1.264E-01 5.785E+05 1.336E+06
 2.21330434E+00  13712.5 6.917E+03 1.708E+15 4.026E+01 2.690E+02 2.000E+05 3.315E-04 1.008E+05 1.507E+06
 2.40234994E+00  15064.0 7.475E+03 1.711E+15 2.472E+01 1.687E+02 2.000E+05 9.150E-07 1.547E+04 1.634E+06
 2.78879552E+00  16436.8 8.643E+03 1.836E+15 1.740E+01 1.184E+02 2.000E+05 1.097E-07 7.083E+03 1.675E+06
 3.46646181E+00  17858.1 1.071E+04 2.126E+15 1.423E+01 9.651E+01 2.000E+05 1.962E-08 3.816E+03 1.758E+06
 4.51825053E+00  19338.1 1.394E+04 2.582E+15 1.273E+01 8.617E+01 2.000E+05 1.823E-10 8.116E+02 1.897E+06
 6.04696404E+00  20900.1 1.865E+04 3.212E+15 1.193E+01 8.063E+01 2.000E+05 0.000E+00 0.000E+00 2.054E+06
 8.16791358E+00  22546.9 2.519E+04 4.029E+15 1.165E+01 7.712E+01 2.000E+05 0.000E+00 0.000E+00 2.190E+06
PRADK 4.8293E+00
BEGIN                    ITERATION  15 COMPLETED
TEFF   7750.  GRAVITY 4.00000 LTE 
TITLE  [-1.0] VTURB=2  L/H=1.25 NOVER NEW ODF                                   
 OPACITY IFOP 1 1 1 1 1 1 1 1 1 1 1 1 1 0 1 0 0 0 0 0
 CONVECTION ON   1.25 TURBULENCE OFF  0.00  0.00  0.00  0.00
ABUNDANCE SCALE   0.10000 ABUNDANCE CHANGE 1 0.92140 2 0.07843
 ABUNDANCE CHANGE  3 -10.94  4 -10.64  5  -9.49  6  -3.52  7  -4.12  8  -3.21
 ABUNDANCE CHANGE  9  -7.48 10  -3.96 11  -5.71 12  -4.46 13  -5.57 14  -4.49
 ABUNDANCE CHANGE 15  -6.59 16  -4.71 17  -6.54 18  -5.64 19  -6.92 20  -5.68
 ABUNDANCE CHANGE 21  -8.87 22  -7.02 23  -8.04 24  -6.37 25  -6.65 26  -4.54
 ABUNDANCE CHANGE 27  -7.12 28  -5.79 29  -7.83 30  -7.44 31  -9.16 32  -8.63
 ABUNDANCE CHANGE 33  -9.67 34  -8.63 35  -9.41 36  -8.73 37  -9.44 38  -9.07
 ABUNDANCE CHANGE 39  -9.80 40  -9.44 41 -10.62 42 -10.12 43 -20.00 44 -10.20
 ABUNDANCE CHANGE 45 -10.92 46 -10.35 47 -11.10 48 -10.27 49 -10.38 50 -10.04
 ABUNDANCE CHANGE 51 -11.04 52  -9.80 53 -10.53 54  -9.87 55 -10.91 56  -9.91
 ABUNDANCE CHANGE 57 -10.87 58 -10.46 59 -11.33 60 -10.54 61 -20.00 62 -11.03
 ABUNDANCE CHANGE 63 -11.53 64 -10.92 65 -11.69 66 -10.90 67 -11.78 68 -11.11
 ABUNDANCE CHANGE 69 -12.04 70 -10.96 71 -11.98 72 -11.16 73 -12.17 74 -10.93
 ABUNDANCE CHANGE 75 -11.76 76 -10.59 77 -10.69 78 -10.24 79 -11.03 80 -10.91
 ABUNDANCE CHANGE 81 -11.14 82 -10.09 83 -11.33 84 -20.00 85 -20.00 86 -20.00
 ABUNDANCE CHANGE 87 -20.00 88 -20.00 89 -20.00 90 -11.95 91 -20.00 92 -12.54
 ABUNDANCE CHANGE 93 -20.00 94 -20.00 95 -20.00 96 -20.00 97 -20.00 98 -20.00
 ABUNDANCE CHANGE 99 -20.00
READ DECK6 72 RHOX,T,P,XNE,ABROSS,ACCRAD,VTURB, FLXCNV,VCONV,VELSND
 7.27209007E-05   5007.4 7.272E-01 4.129E+09 1.834E-03 3.691E-01 2.000E+05 0.000E+00 0.000E+00 1.749E+06
 9.69853593E-05   5039.4 9.698E-01 5.279E+09 1.832E-03 3.630E-01 2.000E+05 0.000E+00 0.000E+00 1.572E+06
 1.29460866E-04   5068.0 1.295E+00 6.674E+09 1.820E-03 3.543E-01 2.000E+05 0.000E+00 0.000E+00 1.423E+06
 1.72666781E-04   5100.3 1.727E+00 8.521E+09 1.841E-03 3.448E-01 2.000E+05 0.000E+00 0.000E+00 1.294E+06
 2.29253803E-04   5134.7 2.292E+00 1.091E+10 1.889E-03 3.348E-01 2.000E+05 0.000E+00 0.000E+00 1.185E+06
 3.02304168E-04   5170.2 3.023E+00 1.395E+10 1.963E-03 3.248E-01 2.000E+05 0.000E+00 0.000E+00 1.095E+06
 3.95488057E-04   5206.2 3.955E+00 1.776E+10 2.063E-03 3.155E-01 2.000E+05 0.000E+00 0.000E+00 1.022E+06
 5.13074943E-04   5242.2 5.130E+00 2.249E+10 2.191E-03 3.068E-01 2.000E+05 0.000E+00 0.000E+00 9.633E+05
 6.59988021E-04   5277.9 6.599E+00 2.830E+10 2.349E-03 2.987E-01 2.000E+05 0.000E+00 0.000E+00 9.162E+05
 8.41931209E-04   5313.4 8.419E+00 3.537E+10 2.540E-03 2.912E-01 2.000E+05 0.000E+00 0.000E+00 8.787E+05
 1.06545373E-03   5348.3 1.065E+01 4.392E+10 2.766E-03 2.842E-01 2.000E+05 0.000E+00 0.000E+00 8.490E+05
 1.33821562E-03   5382.5 1.338E+01 5.414E+10 3.031E-03 2.783E-01 2.000E+05 0.000E+00 0.000E+00 8.256E+05
 1.66939895E-03   5415.3 1.669E+01 6.620E+10 3.335E-03 2.732E-01 2.000E+05 0.000E+00 0.000E+00 8.073E+05
 2.07020084E-03   5446.8 2.070E+01 8.031E+10 3.680E-03 2.692E-01 2.000E+05 0.000E+00 0.000E+00 7.930E+05
 2.55393025E-03   5477.0 2.554E+01 9.677E+10 4.071E-03 2.667E-01 2.000E+05 0.000E+00 0.000E+00 7.820E+05
 3.13619775E-03   5506.3 3.136E+01 1.159E+11 4.516E-03 2.658E-01 2.000E+05 0.000E+00 0.000E+00 7.734E+05
 3.83517766E-03   5534.9 3.835E+01 1.382E+11 5.024E-03 2.670E-01 2.000E+05 0.000E+00 0.000E+00 7.670E+05
 4.67157076E-03   5563.3 4.671E+01 1.643E+11 5.608E-03 2.697E-01 2.000E+05 0.000E+00 0.000E+00 7.621E+05
 5.66872851E-03   5591.9 5.668E+01 1.949E+11 6.285E-03 2.736E-01 2.000E+05 0.000E+00 0.000E+00 7.585E+05
 6.85294938E-03   5621.1 6.853E+01 2.309E+11 7.070E-03 2.787E-01 2.000E+05 0.000E+00 0.000E+00 7.560E+05
 8.25388203E-03   5651.1 8.253E+01 2.734E+11 7.985E-03 2.848E-01 2.000E+05 0.000E+00 0.000E+00 7.544E+05
 9.90513430E-03   5681.9 9.905E+01 3.235E+11 9.048E-03 2.920E-01 2.000E+05 0.000E+00 0.000E+00 7.534E+05
 1.18453048E-02   5713.5 1.184E+02 3.825E+11 1.028E-02 3.009E-01 2.000E+05 0.000E+00 0.000E+00 7.530E+05
 1.41179761E-02   5746.2 1.412E+02 4.523E+11 1.172E-02 3.110E-01 2.000E+05 0.000E+00 0.000E+00 7.530E+05
 1.67741930E-02   5779.4 1.677E+02 5.343E+11 1.339E-02 3.225E-01 2.000E+05 0.000E+00 0.000E+00 7.534E+05
 1.98734263E-02   5813.4 1.987E+02 6.308E+11 1.531E-02 3.356E-01 2.000E+05 0.000E+00 0.000E+00 7.542E+05
 2.34834862E-02   5848.1 2.348E+02 7.444E+11 1.754E-02 3.501E-01 2.000E+05 0.000E+00 0.000E+00 7.551E+05
 2.76846289E-02   5883.3 2.768E+02 8.774E+11 2.010E-02 3.660E-01 2.000E+05 0.000E+00 0.000E+00 7.563E+05
 3.25721679E-02   5918.7 3.257E+02 1.033E+12 2.305E-02 3.837E-01 2.000E+05 0.000E+00 0.000E+00 7.577E+05
 3.82613628E-02   5953.8 3.826E+02 1.213E+12 2.638E-02 4.036E-01 2.000E+05 0.000E+00 0.000E+00 7.593E+05
 4.48923738E-02   5988.5 4.489E+02 1.420E+12 3.016E-02 4.256E-01 2.000E+05 0.000E+00 0.000E+00 7.610E+05
 5.26369520E-02   6022.0 5.263E+02 1.657E+12 3.439E-02 4.497E-01 2.000E+05 0.000E+00 0.000E+00 7.629E+05
 6.17070246E-02   6054.5 6.170E+02 1.928E+12 3.911E-02 4.768E-01 2.000E+05 0.000E+00 0.000E+00 7.649E+05
 7.23599576E-02   6085.4 7.236E+02 2.233E+12 4.434E-02 5.071E-01 2.000E+05 0.000E+00 0.000E+00 7.670E+05
 8.49054633E-02   6115.3 8.490E+02 2.581E+12 5.016E-02 5.413E-01 2.000E+05 0.000E+00 0.000E+00 7.692E+05
 9.97090792E-02   6144.3 9.970E+02 2.976E+12 5.664E-02 5.802E-01 2.000E+05 0.000E+00 0.000E+00 7.715E+05
 1.17195944E-01   6172.8 1.172E+03 3.428E+12 6.393E-02 6.252E-01 2.000E+05 0.000E+00 0.000E+00 7.739E+05
 1.37856287E-01   6201.3 1.378E+03 3.948E+12 7.217E-02 6.770E-01 2.000E+05 0.000E+00 0.000E+00 7.764E+05
 1.62246643E-01   6230.5 1.622E+03 4.552E+12 8.158E-02 7.366E-01 2.000E+05 0.000E+00 0.000E+00 7.789E+05
 1.90998238E-01   6260.8 1.910E+03 5.257E+12 9.237E-02 8.056E-01 2.000E+05 0.000E+00 0.000E+00 7.815E+05
 2.24816533E-01   6292.7 2.248E+03 6.089E+12 1.049E-01 8.864E-01 2.000E+05 0.000E+00 0.000E+00 7.841E+05
 2.64452051E-01   6327.2 2.644E+03 7.081E+12 1.196E-01 9.822E-01 2.000E+05 0.000E+00 0.000E+00 7.867E+05
 3.10706861E-01   6365.0 3.107E+03 8.278E+12 1.370E-01 1.097E+00 2.000E+05 0.000E+00 0.000E+00 7.905E+05
 3.64337803E-01   6407.9 3.643E+03 9.756E+12 1.582E-01 1.240E+00 2.000E+05 0.000E+00 0.000E+00 7.919E+05
 4.25989413E-01   6457.1 4.260E+03 1.161E+13 1.843E-01 1.418E+00 2.000E+05 0.000E+00 0.000E+00 7.945E+05
 4.96125820E-01   6514.7 4.961E+03 1.398E+13 2.174E-01 1.646E+00 2.000E+05 0.000E+00 0.000E+00 7.971E+05
 5.74854876E-01   6582.9 5.748E+03 1.711E+13 2.602E-01 1.944E+00 2.000E+05 0.000E+00 0.000E+00 7.996E+05
 6.61731226E-01   6665.0 6.617E+03 2.133E+13 3.176E-01 2.347E+00 2.000E+05 0.000E+00 0.000E+00 8.021E+05
 7.55580967E-01   6764.1 7.555E+03 2.719E+13 3.967E-01 2.908E+00 2.000E+05 0.000E+00 0.000E+00 8.044E+05
 8.54437102E-01   6884.2 8.543E+03 3.557E+13 5.093E-01 3.715E+00 2.000E+05 0.000E+00 0.000E+00 8.065E+05
 9.55525844E-01   7029.5 9.553E+03 4.787E+13 6.752E-01 4.917E+00 2.000E+05 0.000E+00 0.000E+00 8.084E+05
 1.05522833E+00   7206.0 1.055E+04 6.652E+13 9.319E-01 6.797E+00 2.000E+05 2.681E-11 2.685E+02 8.103E+05
 1.14944220E+00   7418.8 1.149E+04 9.550E+13 1.346E+00 9.869E+00 2.000E+05 2.854E-09 1.211E+03 8.125E+05
 1.23419909E+00   7674.8 1.234E+04 1.417E+14 2.050E+00 1.516E+01 2.000E+05 1.048E-07 3.824E+03 8.160E+05
 1.30607438E+00   7982.9 1.306E+04 2.175E+14 3.324E+00 2.482E+01 2.000E+05 4.384E-06 1.257E+04 8.222E+05
 1.36374533E+00   8339.6 1.363E+04 3.392E+14 5.669E+00 4.265E+01 2.000E+05 2.571E-04 4.631E+04 8.332E+05
 1.40645696E+00   8792.0 1.405E+04 5.556E+14 1.071E+01 8.035E+01 2.000E+05 3.008E-03 9.966E+04 8.536E+05
 1.43547307E+00   9321.3 1.434E+04 9.105E+14 2.105E+01 1.436E+02 2.000E+05 5.469E-02 2.509E+05 8.874E+05
 1.45706948E+00   9752.6 1.455E+04 1.285E+15 3.402E+01 1.755E+02 2.000E+05 2.836E-01 4.392E+05 9.233E+05
 1.47677296E+00  10065.1 1.475E+04 1.601E+15 4.626E+01 1.672E+02 2.000E+05 4.753E-01 5.256E+05 9.543E+05
 1.49691825E+00  10335.8 1.495E+04 1.898E+15 5.836E+01 1.497E+02 2.000E+05 6.128E-01 5.745E+05 9.844E+05
 1.51877054E+00  10578.1 1.516E+04 2.177E+15 7.023E+01 1.346E+02 2.000E+05 7.097E-01 6.090E+05 1.014E+06
 1.54324232E+00  10825.4 1.540E+04 2.468E+15 8.290E+01 1.267E+02 2.000E+05 7.792E-01 6.438E+05 1.046E+06
 1.57116973E+00  11079.0 1.568E+04 2.765E+15 9.578E+01 1.163E+02 2.000E+05 8.127E-01 6.485E+05 1.080E+06
 1.60392931E+00  11333.0 1.600E+04 3.056E+15 1.074E+02 1.218E+02 2.000E+05 8.393E-01 6.856E+05 1.116E+06
 1.64309916E+00  11674.5 1.639E+04 3.409E+15 1.191E+02 1.291E+02 2.000E+05 8.446E-01 7.039E+05 1.166E+06
 1.69116207E+00  12025.0 1.686E+04 3.731E+15 1.268E+02 1.327E+02 2.000E+05 8.278E-01 6.893E+05 1.217E+06
 1.75249358E+00  12508.9 1.747E+04 4.072E+15 1.292E+02 2.454E+02 2.000E+05 7.930E-01 8.198E+05 1.284E+06
 1.84812413E+00  14008.4 1.839E+04 4.352E+15 9.155E+01 4.167E+02 2.000E+05 1.190E-01 4.460E+05 1.475E+06
 2.07967379E+00  16763.5 2.063E+04 4.271E+15 3.603E+01 2.454E+02 2.000E+05 6.915E-05 4.664E+04 1.695E+06
 2.70374992E+00  18924.8 2.674E+04 5.011E+15 2.597E+01 1.712E+02 2.000E+05 1.712E-06 1.284E+04 1.812E+06
 3.74103117E+00  21064.2 3.695E+04 6.295E+15 2.226E+01 1.480E+02 2.000E+05 6.428E-08 4.476E+03 2.014E+06
PRADK 4.8309E+00
TEFF   8000.  GRAVITY 3.50000 LTE 
TITLE  [-1.0] VTURB=2  L/H=1.25 NOVER NEW ODF                                   
 OPACITY IFOP 1 1 1 1 1 1 1 1 1 1 1 1 1 0 1 0 0 0 0 0
 CONVECTION ON   1.25 TURBULENCE OFF  0.00  0.00  0.00  0.00
ABUNDANCE SCALE   0.10000 ABUNDANCE CHANGE 1 0.92140 2 0.07843
 ABUNDANCE CHANGE  3 -10.94  4 -10.64  5  -9.49  6  -3.52  7  -4.12  8  -3.21
 ABUNDANCE CHANGE  9  -7.48 10  -3.96 11  -5.71 12  -4.46 13  -5.57 14  -4.49
 ABUNDANCE CHANGE 15  -6.59 16  -4.71 17  -6.54 18  -5.64 19  -6.92 20  -5.68
 ABUNDANCE CHANGE 21  -8.87 22  -7.02 23  -8.04 24  -6.37 25  -6.65 26  -4.54
 ABUNDANCE CHANGE 27  -7.12 28  -5.79 29  -7.83 30  -7.44 31  -9.16 32  -8.63
 ABUNDANCE CHANGE 33  -9.67 34  -8.63 35  -9.41 36  -8.73 37  -9.44 38  -9.07
 ABUNDANCE CHANGE 39  -9.80 40  -9.44 41 -10.62 42 -10.12 43 -20.00 44 -10.20
 ABUNDANCE CHANGE 45 -10.92 46 -10.35 47 -11.10 48 -10.27 49 -10.38 50 -10.04
 ABUNDANCE CHANGE 51 -11.04 52  -9.80 53 -10.53 54  -9.87 55 -10.91 56  -9.91
 ABUNDANCE CHANGE 57 -10.87 58 -10.46 59 -11.33 60 -10.54 61 -20.00 62 -11.03
 ABUNDANCE CHANGE 63 -11.53 64 -10.92 65 -11.69 66 -10.90 67 -11.78 68 -11.11
 ABUNDANCE CHANGE 69 -12.04 70 -10.96 71 -11.98 72 -11.16 73 -12.17 74 -10.93
 ABUNDANCE CHANGE 75 -11.76 76 -10.59 77 -10.69 78 -10.24 79 -11.03 80 -10.91
 ABUNDANCE CHANGE 81 -11.14 82 -10.09 83 -11.33 84 -20.00 85 -20.00 86 -20.00
 ABUNDANCE CHANGE 87 -20.00 88 -20.00 89 -20.00 90 -11.95 91 -20.00 92 -12.54
 ABUNDANCE CHANGE 93 -20.00 94 -20.00 95 -20.00 96 -20.00 97 -20.00 98 -20.00
 ABUNDANCE CHANGE 99 -20.00
READ DECK6 72 RHOX,T,P,XNE,ABROSS,ACCRAD,VTURB, FLXCNV,VCONV,VELSND
 3.05518751E-05   5022.9 9.660E-02 1.565E+09 4.365E-03 5.149E-01 2.000E+05 0.000E+00 0.000E+00 3.534E+06
 4.09612058E-05   5049.5 1.295E-01 1.973E+09 4.181E-03 5.095E-01 2.000E+05 0.000E+00 0.000E+00 3.141E+06
 5.55515909E-05   5073.0 1.756E-01 2.475E+09 3.949E-03 5.010E-01 2.000E+05 0.000E+00 0.000E+00 2.792E+06
 7.59683841E-05   5102.8 2.402E-01 3.177E+09 3.798E-03 4.910E-01 2.000E+05 0.000E+00 0.000E+00 2.468E+06
 1.04137658E-04   5136.7 3.293E-01 4.128E+09 3.703E-03 4.791E-01 2.000E+05 0.000E+00 0.000E+00 2.179E+06
 1.42389041E-04   5174.1 4.502E-01 5.405E+09 3.660E-03 4.658E-01 2.000E+05 0.000E+00 0.000E+00 1.927E+06
 1.93662757E-04   5213.9 6.123E-01 7.097E+09 3.662E-03 4.513E-01 2.000E+05 0.000E+00 0.000E+00 1.713E+06
 2.61633472E-04   5255.1 8.272E-01 9.310E+09 3.701E-03 4.365E-01 2.000E+05 0.000E+00 0.000E+00 1.532E+06
 3.50875279E-04   5297.2 1.109E+00 1.217E+10 3.775E-03 4.220E-01 2.000E+05 0.000E+00 0.000E+00 1.381E+06
 4.67043888E-04   5339.5 1.477E+00 1.584E+10 3.883E-03 4.084E-01 2.000E+05 0.000E+00 0.000E+00 1.255E+06
 6.17064538E-04   5381.9 1.951E+00 2.049E+10 4.024E-03 3.957E-01 2.000E+05 0.000E+00 0.000E+00 1.152E+06
 8.09285010E-04   5424.0 2.559E+00 2.635E+10 4.204E-03 3.840E-01 2.000E+05 0.000E+00 0.000E+00 1.068E+06
 1.05370684E-03   5465.5 3.332E+00 3.365E+10 4.424E-03 3.730E-01 2.000E+05 0.000E+00 0.000E+00 9.993E+05
 1.36243351E-03   5506.0 4.308E+00 4.263E+10 4.684E-03 3.633E-01 2.000E+05 0.000E+00 0.000E+00 9.439E+05
 1.75018440E-03   5545.0 5.534E+00 5.355E+10 4.985E-03 3.550E-01 2.000E+05 0.000E+00 0.000E+00 8.995E+05
 2.23491329E-03   5582.4 7.067E+00 6.669E+10 5.329E-03 3.487E-01 2.000E+05 0.000E+00 0.000E+00 8.641E+05
 2.83811265E-03   5618.3 8.974E+00 8.240E+10 5.725E-03 3.450E-01 2.000E+05 0.000E+00 0.000E+00 8.359E+05
 3.58483819E-03   5653.1 1.133E+01 1.011E+11 6.184E-03 3.443E-01 2.000E+05 0.000E+00 0.000E+00 8.135E+05
 4.50339792E-03   5687.5 1.424E+01 1.236E+11 6.727E-03 3.462E-01 2.000E+05 0.000E+00 0.000E+00 7.959E+05
 5.62492776E-03   5722.0 1.779E+01 1.504E+11 7.376E-03 3.503E-01 2.000E+05 0.000E+00 0.000E+00 7.820E+05
 6.98316992E-03   5757.3 2.208E+01 1.827E+11 8.154E-03 3.562E-01 2.000E+05 0.000E+00 0.000E+00 7.712E+05
 8.61488728E-03   5793.5 2.724E+01 2.214E+11 9.085E-03 3.641E-01 2.000E+05 0.000E+00 0.000E+00 7.629E+05
 1.05604921E-02   5830.6 3.339E+01 2.678E+11 1.019E-02 3.738E-01 2.000E+05 0.000E+00 0.000E+00 7.565E+05
 1.28650764E-02   5868.8 4.068E+01 3.232E+11 1.151E-02 3.857E-01 2.000E+05 0.000E+00 0.000E+00 7.518E+05
 1.55793533E-02   5908.0 4.926E+01 3.895E+11 1.306E-02 3.990E-01 2.000E+05 0.000E+00 0.000E+00 7.483E+05
 1.87619355E-02   5947.9 5.932E+01 4.683E+11 1.488E-02 4.137E-01 2.000E+05 0.000E+00 0.000E+00 7.459E+05
 2.24813570E-02   5988.4 7.108E+01 5.617E+11 1.701E-02 4.300E-01 2.000E+05 0.000E+00 0.000E+00 7.443E+05
 2.68196283E-02   6028.9 8.480E+01 6.714E+11 1.945E-02 4.476E-01 2.000E+05 0.000E+00 0.000E+00 7.435E+05
 3.18783251E-02   6069.0 1.008E+02 7.993E+11 2.224E-02 4.668E-01 2.000E+05 0.000E+00 0.000E+00 7.432E+05
 3.77839331E-02   6107.9 1.195E+02 9.469E+11 2.537E-02 4.885E-01 2.000E+05 0.000E+00 0.000E+00 7.434E+05
 4.46941510E-02   6145.5 1.413E+02 1.116E+12 2.888E-02 5.125E-01 2.000E+05 0.000E+00 0.000E+00 7.440E+05
 5.28032997E-02   6181.3 1.670E+02 1.309E+12 3.277E-02 5.396E-01 2.000E+05 0.000E+00 0.000E+00 7.450E+05
 6.23478003E-02   6215.6 1.971E+02 1.528E+12 3.708E-02 5.704E-01 2.000E+05 0.000E+00 0.000E+00 7.462E+05
 7.36033675E-02   6248.9 2.327E+02 1.779E+12 4.191E-02 6.054E-01 2.000E+05 0.000E+00 0.000E+00 7.477E+05
 8.68909008E-02   6281.6 2.747E+02 2.067E+12 4.732E-02 6.449E-01 2.000E+05 0.000E+00 0.000E+00 7.495E+05
 1.02585697E-01   6314.0 3.244E+02 2.399E+12 5.342E-02 6.897E-01 2.000E+05 0.000E+00 0.000E+00 7.514E+05
 1.21119138E-01   6346.4 3.829E+02 2.783E+12 6.035E-02 7.414E-01 2.000E+05 0.000E+00 0.000E+00 7.534E+05
 1.42990421E-01   6379.1 4.521E+02 3.227E+12 6.822E-02 8.003E-01 2.000E+05 0.000E+00 0.000E+00 7.556E+05
 1.68774482E-01   6412.5 5.336E+02 3.744E+12 7.722E-02 8.682E-01 2.000E+05 0.000E+00 0.000E+00 7.579E+05
 1.99125600E-01   6446.8 6.296E+02 4.348E+12 8.757E-02 9.470E-01 2.000E+05 0.000E+00 0.000E+00 7.603E+05
 2.34766159E-01   6482.8 7.422E+02 5.062E+12 9.959E-02 1.040E+00 2.000E+05 0.000E+00 0.000E+00 7.628E+05
 2.76462116E-01   6521.5 8.740E+02 5.913E+12 1.138E-01 1.151E+00 2.000E+05 0.000E+00 0.000E+00 7.653E+05
 3.24993333E-01   6564.0 1.027E+03 6.944E+12 1.308E-01 1.287E+00 2.000E+05 0.000E+00 0.000E+00 7.678E+05
 3.81060755E-01   6611.9 1.205E+03 8.217E+12 1.516E-01 1.457E+00 2.000E+05 0.000E+00 0.000E+00 7.703E+05
 4.45183274E-01   6666.8 1.407E+03 9.819E+12 1.778E-01 1.673E+00 2.000E+05 0.000E+00 0.000E+00 7.728E+05
 5.17609057E-01   6730.9 1.636E+03 1.187E+13 2.114E-01 1.955E+00 2.000E+05 0.000E+00 0.000E+00 7.753E+05
 5.98168368E-01   6806.5 1.891E+03 1.457E+13 2.557E-01 2.330E+00 2.000E+05 0.000E+00 0.000E+00 7.777E+05
 6.86077214E-01   6896.7 2.169E+03 1.820E+13 3.158E-01 2.846E+00 2.000E+05 0.000E+00 0.000E+00 7.800E+05
 7.79804519E-01   7004.7 2.465E+03 2.321E+13 4.002E-01 3.577E+00 2.000E+05 0.000E+00 0.000E+00 7.825E+05
 8.76955172E-01   7134.7 2.771E+03 3.031E+13 5.231E-01 4.651E+00 2.000E+05 0.000E+00 0.000E+00 7.851E+05
 9.74254094E-01   7291.1 3.079E+03 4.061E+13 7.100E-01 6.288E+00 2.000E+05 2.052E-12 1.632E+02 7.884E+05
 1.06788585E+00   7478.5 3.374E+03 5.587E+13 1.005E+00 8.883E+00 2.000E+05 6.196E-11 4.820E+02 7.928E+05
 1.15394113E+00   7702.6 3.645E+03 7.901E+13 1.496E+00 1.317E+01 2.000E+05 1.247E-09 1.244E+03 7.994E+05
 1.22900061E+00   7968.9 3.881E+03 1.146E+14 2.350E+00 2.056E+01 2.000E+05 3.743E-08 3.674E+03 8.094E+05
 1.29094001E+00   8282.6 4.076E+03 1.696E+14 3.898E+00 3.374E+01 2.000E+05 1.712E-06 1.255E+04 8.248E+05
 1.33964504E+00   8644.2 4.227E+03 2.528E+14 6.737E+00 5.745E+01 2.000E+05 9.952E-05 4.699E+04 8.479E+05
 1.37656533E+00   9065.5 4.341E+03 3.776E+14 1.201E+01 1.007E+02 2.000E+05 2.124E-03 1.281E+05 8.826E+05
 1.40397828E+00   9556.8 4.424E+03 5.559E+14 2.140E+01 1.719E+02 2.000E+05 1.042E-02 2.180E+05 9.346E+05
 1.42537452E+00  10060.0 4.488E+03 7.572E+14 3.404E+01 2.430E+02 2.000E+05 9.593E-02 4.734E+05 1.001E+06
 1.44527994E+00  10511.6 4.545E+03 9.302E+14 4.529E+01 2.741E+02 2.000E+05 2.128E-01 6.511E+05 1.070E+06
 1.46643393E+00  10957.9 4.606E+03 1.072E+15 5.370E+01 3.137E+02 2.000E+05 2.539E-01 7.357E+05 1.142E+06
 1.49168056E+00  11544.6 4.677E+03 1.191E+15 5.647E+01 3.781E+02 2.000E+05 1.287E-01 6.272E+05 1.233E+06
 1.52753544E+00  12364.5 4.777E+03 1.252E+15 4.815E+01 3.663E+02 2.000E+05 4.307E-03 2.298E+05 1.348E+06
 1.58797643E+00  13286.6 4.949E+03 1.258E+15 3.489E+01 2.730E+02 2.000E+05 2.279E-05 4.724E+04 1.474E+06
 1.70300903E+00  14280.1 5.287E+03 1.271E+15 2.440E+01 1.897E+02 2.000E+05 1.161E-07 8.917E+03 1.591E+06
 1.91821547E+00  15333.2 5.933E+03 1.340E+15 1.786E+01 1.382E+02 2.000E+05 6.560E-09 3.337E+03 1.644E+06
 2.29276399E+00  16472.6 7.071E+03 1.503E+15 1.434E+01 1.108E+02 2.000E+05 3.260E-09 2.429E+03 1.677E+06
 2.88627458E+00  17689.3 8.887E+03 1.781E+15 1.257E+01 9.689E+01 2.000E+05 1.052E-09 1.591E+03 1.752E+06
 3.76439036E+00  19007.4 1.158E+04 2.181E+15 1.159E+01 8.925E+01 2.000E+05 7.313E-12 3.035E+02 1.873E+06
 5.01139804E+00  20414.8 1.542E+04 2.716E+15 1.105E+01 8.497E+01 2.000E+05 0.000E+00 0.000E+00 2.016E+06
 6.73085776E+00  21936.8 2.071E+04 3.404E+15 1.082E+01 8.309E+01 2.000E+05 0.000E+00 0.000E+00 2.149E+06
 9.04140309E+00  23564.6 2.783E+04 4.262E+15 1.083E+01 8.077E+01 2.000E+05 0.000E+00 0.000E+00 2.262E+06
PRADK 5.4848E+00
BEGIN                    ITERATION  15 COMPLETED
TEFF   8000.  GRAVITY 4.00000 LTE 
TITLE  [-1.0] VTURB=2  L/H=1.25 NOVER NEW ODF                                   
 OPACITY IFOP 1 1 1 1 1 1 1 1 1 1 1 1 1 0 1 0 0 0 0 0
 CONVECTION ON   1.25 TURBULENCE OFF  0.00  0.00  0.00  0.00
ABUNDANCE SCALE   0.10000 ABUNDANCE CHANGE 1 0.92140 2 0.07843
 ABUNDANCE CHANGE  3 -10.94  4 -10.64  5  -9.49  6  -3.52  7  -4.12  8  -3.21
 ABUNDANCE CHANGE  9  -7.48 10  -3.96 11  -5.71 12  -4.46 13  -5.57 14  -4.49
 ABUNDANCE CHANGE 15  -6.59 16  -4.71 17  -6.54 18  -5.64 19  -6.92 20  -5.68
 ABUNDANCE CHANGE 21  -8.87 22  -7.02 23  -8.04 24  -6.37 25  -6.65 26  -4.54
 ABUNDANCE CHANGE 27  -7.12 28  -5.79 29  -7.83 30  -7.44 31  -9.16 32  -8.63
 ABUNDANCE CHANGE 33  -9.67 34  -8.63 35  -9.41 36  -8.73 37  -9.44 38  -9.07
 ABUNDANCE CHANGE 39  -9.80 40  -9.44 41 -10.62 42 -10.12 43 -20.00 44 -10.20
 ABUNDANCE CHANGE 45 -10.92 46 -10.35 47 -11.10 48 -10.27 49 -10.38 50 -10.04
 ABUNDANCE CHANGE 51 -11.04 52  -9.80 53 -10.53 54  -9.87 55 -10.91 56  -9.91
 ABUNDANCE CHANGE 57 -10.87 58 -10.46 59 -11.33 60 -10.54 61 -20.00 62 -11.03
 ABUNDANCE CHANGE 63 -11.53 64 -10.92 65 -11.69 66 -10.90 67 -11.78 68 -11.11
 ABUNDANCE CHANGE 69 -12.04 70 -10.96 71 -11.98 72 -11.16 73 -12.17 74 -10.93
 ABUNDANCE CHANGE 75 -11.76 76 -10.59 77 -10.69 78 -10.24 79 -11.03 80 -10.91
 ABUNDANCE CHANGE 81 -11.14 82 -10.09 83 -11.33 84 -20.00 85 -20.00 86 -20.00
 ABUNDANCE CHANGE 87 -20.00 88 -20.00 89 -20.00 90 -11.95 91 -20.00 92 -12.54
 ABUNDANCE CHANGE 93 -20.00 94 -20.00 95 -20.00 96 -20.00 97 -20.00 98 -20.00
 ABUNDANCE CHANGE 99 -20.00
READ DECK6 72 RHOX,T,P,XNE,ABROSS,ACCRAD,VTURB, FLXCNV,VCONV,VELSND
 4.22792970E-05   5117.1 4.228E-01 4.416E+09 3.154E-03 5.727E-01 2.000E+05 0.000E+00 0.000E+00 2.042E+06
 5.65534123E-05   5146.1 5.655E-01 5.580E+09 3.078E-03 5.661E-01 2.000E+05 0.000E+00 0.000E+00 1.831E+06
 7.60929585E-05   5173.6 7.609E-01 7.034E+09 2.993E-03 5.561E-01 2.000E+05 0.000E+00 0.000E+00 1.647E+06
 1.02653912E-04   5205.6 1.026E+00 8.993E+09 2.962E-03 5.442E-01 2.000E+05 0.000E+00 0.000E+00 1.483E+06
 1.38177805E-04   5241.2 1.382E+00 1.159E+10 2.982E-03 5.309E-01 2.000E+05 0.000E+00 0.000E+00 1.342E+06
 1.84887528E-04   5279.0 1.849E+00 1.496E+10 3.045E-03 5.164E-01 2.000E+05 0.000E+00 0.000E+00 1.223E+06
 2.45465895E-04   5318.1 2.454E+00 1.927E+10 3.150E-03 5.014E-01 2.000E+05 0.000E+00 0.000E+00 1.125E+06
 3.23072220E-04   5357.8 3.230E+00 2.473E+10 3.298E-03 4.868E-01 2.000E+05 0.000E+00 0.000E+00 1.045E+06
 4.21374803E-04   5397.6 4.213E+00 3.154E+10 3.488E-03 4.738E-01 2.000E+05 0.000E+00 0.000E+00 9.808E+05
 5.44688397E-04   5437.1 5.446E+00 3.996E+10 3.725E-03 4.618E-01 2.000E+05 0.000E+00 0.000E+00 9.290E+05
 6.98005536E-04   5476.2 6.979E+00 5.027E+10 4.011E-03 4.509E-01 2.000E+05 0.000E+00 0.000E+00 8.877E+05
 8.87104585E-04   5514.7 8.870E+00 6.278E+10 4.352E-03 4.408E-01 2.000E+05 0.000E+00 0.000E+00 8.550E+05
 1.11877133E-03   5552.3 1.119E+01 7.781E+10 4.750E-03 4.318E-01 2.000E+05 0.000E+00 0.000E+00 8.291E+05
 1.40113777E-03   5588.5 1.401E+01 9.565E+10 5.208E-03 4.242E-01 2.000E+05 0.000E+00 0.000E+00 8.089E+05
 1.74394720E-03   5623.5 1.744E+01 1.167E+11 5.729E-03 4.184E-01 2.000E+05 0.000E+00 0.000E+00 7.930E+05
 2.15889466E-03   5657.0 2.159E+01 1.413E+11 6.320E-03 4.146E-01 2.000E+05 0.000E+00 0.000E+00 7.807E+05
 2.65986407E-03   5689.2 2.660E+01 1.700E+11 6.989E-03 4.133E-01 2.000E+05 0.000E+00 0.000E+00 7.712E+05
 3.26303554E-03   5720.6 3.263E+01 2.035E+11 7.752E-03 4.147E-01 2.000E+05 0.000E+00 0.000E+00 7.640E+05
 3.98698117E-03   5751.6 3.987E+01 2.427E+11 8.628E-03 4.193E-01 2.000E+05 0.000E+00 0.000E+00 7.585E+05
 4.85269393E-03   5782.6 4.852E+01 2.886E+11 9.640E-03 4.266E-01 2.000E+05 0.000E+00 0.000E+00 7.545E+05
 5.88363882E-03   5814.1 5.883E+01 3.426E+11 1.082E-02 4.361E-01 2.000E+05 0.000E+00 0.000E+00 7.516E+05
 7.10614684E-03   5846.3 7.106E+01 4.064E+11 1.219E-02 4.476E-01 2.000E+05 0.000E+00 0.000E+00 7.497E+05
 8.54977314E-03   5879.5 8.549E+01 4.817E+11 1.379E-02 4.611E-01 2.000E+05 0.000E+00 0.000E+00 7.485E+05
 1.02481325E-02   5913.7 1.025E+02 5.707E+11 1.566E-02 4.765E-01 2.000E+05 0.000E+00 0.000E+00 7.479E+05
 1.22397131E-02   5948.7 1.224E+02 6.758E+11 1.783E-02 4.948E-01 2.000E+05 0.000E+00 0.000E+00 7.478E+05
 1.45687407E-02   5984.7 1.457E+02 7.997E+11 2.036E-02 5.150E-01 2.000E+05 0.000E+00 0.000E+00 7.482E+05
 1.72873866E-02   6021.3 1.729E+02 9.451E+11 2.327E-02 5.371E-01 2.000E+05 0.000E+00 0.000E+00 7.489E+05
 2.04576885E-02   6058.2 2.046E+02 1.115E+12 2.662E-02 5.615E-01 2.000E+05 0.000E+00 0.000E+00 7.499E+05
 2.41538376E-02   6095.0 2.415E+02 1.313E+12 3.044E-02 5.880E-01 2.000E+05 0.000E+00 0.000E+00 7.511E+05
 2.84680270E-02   6131.2 2.847E+02 1.541E+12 3.474E-02 6.170E-01 2.000E+05 0.000E+00 0.000E+00 7.525E+05
 3.35129002E-02   6166.5 3.351E+02 1.802E+12 3.958E-02 6.495E-01 2.000E+05 0.000E+00 0.000E+00 7.542E+05
 3.94295844E-02   6199.9 3.943E+02 2.098E+12 4.492E-02 6.867E-01 2.000E+05 0.000E+00 0.000E+00 7.561E+05
 4.63866877E-02   6232.6 4.638E+02 2.436E+12 5.091E-02 7.289E-01 2.000E+05 0.000E+00 0.000E+00 7.581E+05
 5.45805218E-02   6264.4 5.458E+02 2.821E+12 5.759E-02 7.761E-01 2.000E+05 0.000E+00 0.000E+00 7.602E+05
 6.42438097E-02   6295.7 6.424E+02 3.263E+12 6.510E-02 8.293E-01 2.000E+05 0.000E+00 0.000E+00 7.625E+05
 7.56492172E-02   6326.6 7.564E+02 3.769E+12 7.352E-02 8.891E-01 2.000E+05 0.000E+00 0.000E+00 7.649E+05
 8.91174326E-02   6357.4 8.911E+02 4.351E+12 8.302E-02 9.567E-01 2.000E+05 0.000E+00 0.000E+00 7.663E+05
 1.05022348E-01   6388.3 1.050E+03 5.023E+12 9.377E-02 1.034E+00 2.000E+05 0.000E+00 0.000E+00 7.699E+05
 1.23790503E-01   6419.9 1.238E+03 5.802E+12 1.060E-01 1.124E+00 2.000E+05 0.000E+00 0.000E+00 7.726E+05
 1.45910400E-01   6452.3 1.459E+03 6.710E+12 1.201E-01 1.227E+00 2.000E+05 0.000E+00 0.000E+00 7.752E+05
 1.71932641E-01   6486.4 1.719E+03 7.778E+12 1.363E-01 1.348E+00 2.000E+05 0.000E+00 0.000E+00 7.780E+05
 2.02439158E-01   6523.0 2.024E+03 9.050E+12 1.553E-01 1.493E+00 2.000E+05 0.000E+00 0.000E+00 7.807E+05
 2.38042964E-01   6563.3 2.380E+03 1.059E+13 1.780E-01 1.668E+00 2.000E+05 0.000E+00 0.000E+00 7.834E+05
 2.79322447E-01   6608.7 2.793E+03 1.248E+13 2.055E-01 1.883E+00 2.000E+05 0.000E+00 0.000E+00 7.861E+05
 3.26748155E-01   6661.1 3.267E+03 1.485E+13 2.398E-01 2.156E+00 2.000E+05 0.000E+00 0.000E+00 7.888E+05
 3.80574797E-01   6722.8 3.805E+03 1.791E+13 2.837E-01 2.510E+00 2.000E+05 0.000E+00 0.000E+00 7.914E+05
 4.40772795E-01   6796.0 4.407E+03 2.192E+13 3.411E-01 2.978E+00 2.000E+05 0.000E+00 0.000E+00 7.939E+05
 5.06908908E-01   6883.7 5.068E+03 2.733E+13 4.182E-01 3.615E+00 2.000E+05 0.000E+00 0.000E+00 7.963E+05
 5.78000791E-01   6989.2 5.779E+03 3.480E+13 5.252E-01 4.507E+00 2.000E+05 0.000E+00 0.000E+00 7.985E+05
 6.52428777E-01   7116.7 6.523E+03 4.541E+13 6.790E-01 5.804E+00 2.000E+05 0.000E+00 0.000E+00 8.008E+05
 7.27861971E-01   7271.2 7.276E+03 6.092E+13 9.098E-01 7.767E+00 2.000E+05 4.040E-14 3.523E+01 8.032E+05
 8.01482869E-01   7456.8 8.012E+03 8.407E+13 1.269E+00 1.085E+01 2.000E+05 1.622E-10 5.321E+02 8.061E+05
 8.70268998E-01   7680.2 8.699E+03 1.196E+14 1.855E+00 1.591E+01 2.000E+05 4.860E-09 1.569E+03 8.103E+05
 9.31315833E-01   7947.9 9.308E+03 1.752E+14 2.865E+00 2.463E+01 2.000E+05 1.461E-07 4.626E+03 8.169E+05
 9.82545753E-01   8264.7 9.819E+03 2.630E+14 4.678E+00 4.025E+01 2.000E+05 6.195E-06 1.532E+04 8.277E+05
 1.02330379E+00   8635.1 1.022E+04 4.013E+14 8.050E+00 6.930E+01 2.000E+05 3.610E-04 5.675E+04 8.448E+05
 1.05357772E+00   9096.2 1.052E+04 6.333E+14 1.497E+01 1.275E+02 2.000E+05 2.342E-03 1.018E+05 8.737E+05
 1.07489433E+00   9627.3 1.073E+04 9.849E+14 2.799E+01 2.175E+02 2.000E+05 5.290E-02 2.820E+05 9.179E+05
 1.09147017E+00  10075.4 1.090E+04 1.342E+15 4.357E+01 2.638E+02 2.000E+05 2.597E-01 4.926E+05 9.652E+05
 1.10708777E+00  10420.7 1.105E+04 1.641E+15 5.757E+01 2.562E+02 2.000E+05 4.305E-01 5.947E+05 1.008E+06
 1.12346698E+00  10733.3 1.121E+04 1.914E+15 7.093E+01 2.402E+02 2.000E+05 5.507E-01 6.573E+05 1.050E+06
 1.14164439E+00  11036.6 1.138E+04 2.171E+15 8.339E+01 2.367E+02 2.000E+05 6.321E-01 7.104E+05 1.094E+06
 1.16264101E+00  11382.8 1.159E+04 2.435E+15 9.459E+01 2.420E+02 2.000E+05 6.596E-01 7.384E+05 1.146E+06
 1.18800183E+00  11766.7 1.184E+04 2.682E+15 1.015E+02 2.823E+02 2.000E+05 6.465E-01 7.774E+05 1.203E+06
 1.22060533E+00  12385.8 1.215E+04 2.939E+15 1.011E+02 4.409E+02 2.000E+05 4.693E-01 7.638E+05 1.291E+06
 1.27098533E+00  13564.4 1.263E+04 3.078E+15 7.541E+01 5.027E+02 2.000E+05 1.163E-02 2.477E+05 1.445E+06
 1.37303512E+00  15121.5 1.361E+04 3.083E+15 4.414E+01 3.420E+02 2.000E+05 1.908E-05 3.587E+04 1.621E+06
 1.59496911E+00  16636.4 1.577E+04 3.294E+15 2.955E+01 2.279E+02 2.000E+05 6.496E-07 1.116E+04 1.688E+06
 1.99860018E+00  18183.2 1.972E+04 3.829E+15 2.369E+01 1.822E+02 2.000E+05 1.430E-07 6.319E+03 1.764E+06
 2.63101554E+00  19764.1 2.594E+04 4.688E+15 2.118E+01 1.626E+02 2.000E+05 3.084E-09 1.760E+03 1.897E+06
 3.54677967E+00  21419.9 3.495E+04 5.865E+15 1.999E+01 1.532E+02 2.000E+05 0.000E+00 0.000E+00 2.058E+06
 4.80710901E+00  23151.3 4.736E+04 7.372E+15 1.970E+01 1.466E+02 2.000E+05 0.000E+00 0.000E+00 2.204E+06
PRADK 5.4832E+00
BEGIN                    ITERATION  15 COMPLETED
"""

from unittest.mock import patch, mock_open, MagicMock

@patch("builtins.open", new_callable=mock_open, read_data=grid_text)
def test_get_best_model(mock_file, atlas_model):
    parameters = MagicMock()
    parameters.teff = 8100
    parameters.logg = 3.90
    parameters.metallicity = 1.0

    atlas_model.parameters = parameters

    atlas_model.set_grid("grid_path")
    initial_model = atlas_model._get_initial_model()

    assert initial_model.teff == 8000.
    assert initial_model.logg == 4.0