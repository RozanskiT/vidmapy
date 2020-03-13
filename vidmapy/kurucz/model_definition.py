#!/usr/bin/env python3

"""
"""

class ModelDefinition:

    def __init__(self):
        pass

    def __call__(self, parameters):
        s = [
            self._introduction(),
            self._microturbulence(parameters),
            self._title(parameters),
            self._metallicity(parameters),
            self._chemical_composition(parameters),
            self._ending()
        ]
        return "".join(s)

    def _introduction(self):
        s = ["READ KAPPA\n",
             "READ PUNCH\n",
             "MOLECULES ON\n",
             "READ MOLECULES\n",
             "FREQUENCIES 337 1 337 BIG\n",
             "CONVECTION OVER 1.25 0 36\n"
            ]
        return "".join(s)

    def _microturbulence(self, parameters):
        # TODO: use it if neccesary:
        # def eformat(f, prec, exp_digits):
        #     s = "%.*e"%(prec, f)
        #     mantissa, exp = s.split('e')
        #     # add 1 to digits as 1 is taken by sign +/-
        #     return "%se%+0*d"%(mantissa, exp_digits+1, int(exp))
        return f"VTURB {parameters.microturbulence:.1E}\n"

    def _title(self, parameters):
        s = [
            f"TITLE TEFF={parameters.teff:.0f}, ",
            f"LOGG={parameters.logg:.2f}, ",
            f"[M/H]={parameters.metallicity:.2f}, ",
            f"VMIC={parameters.microturbulence:.0f}\n"
            ]
        return "".join(s)

    def _metallicity(self, parameters):
        return f"ABUNDANCE SCALE   {parameters.metallicity:6.4f}\n"

    def _teff_logg(self, parameters):
        return f"SCALE 72 -6.875 0.125 {parameters.teff:5.0f}. {parameters.logg:4.2f}\n"

    def _chemical_composition(self, parameters):
        def _single_element(element_atomic_number, abundance):
            return f"ABUNDANCE CHANGE {element_atomic_number:2d} {abundance:7.5f}\n"
        s = []
        for k in parameters.chemical_composition:
            if parameters.chemical_composition[k] is not None:
                s.append(_single_element(k, parameters.chemical_composition[k]))
        return "".join(s)

    def _ending(self):
        s = [
            "ITERATIONS 15\n"
            "PRINT 1 0 0 0 0 0 0 0 0 0 0 0 0 0 1\n"
            "PUNCH 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1\n"
            "BEGIN                    ITERATION  15 COMPLETED\n"
            "END\n"
        ]
        return "".join(s)

def main():
    pass

if __name__ == '__main__':
    main()