#!/usr/bin/env python3

"""
Implements easy-to-use interface to Kurucz's SYNTHE code

Needs to be use together with class Atlas and Parameters.
eg.
    p = Parameters() # All default

    wa = Atlas()
    m = wa.get_model(p)
    
    ws = Synthe()
    spectrum = ws.get_spectrum(m)
"""

from vidmapy.kurucz.spectrum import Spectrum
from vidmapy.kurucz.parameters import Parameters 

import os
import subprocess
import tempfile
import glob
import pandas as pd
import copy

class Synthe:
    def __init__(self):

        self._kurucz_directory = os.path.dirname(os.path.abspath(__file__))
        # self._kurucz_bin_path = "/usr/local/kurucz/"
        self._kurucz_bin_path = os.path.join(self._kurucz_directory, 'bin')
        self._atomic_data_path = os.path.join(self._kurucz_directory, "atomic_data")

    def get_spectrum(self, model, parameters=None):
        self.model = copy.deepcopy(model)
        if parameters is not None:
            self.model.parameters.get_synthe_parameters(parameters)
        spectrum = self._create_temp_direcotry_and_run_SYNTHE(self.model)
        return spectrum

    def _create_temp_direcotry_and_run_SYNTHE(self, model):
        with tempfile.TemporaryDirectory(prefix="synthe_") as tmpdirname:
            spectrum = self._compute_spectrum(tmpdirname, model)
        return spectrum 

    def _compute_spectrum(self, tmpdirname, model):
        self._run_xnfpelsyn(tmpdirname, model)
        self._run_synbeg(tmpdirname, model)
        self._run_rline2(tmpdirname, model) #  rgfalllinesnew.for  ?
        # self._run_rmolecasc(tmpdirname, model) # Optionally! Include molecular lines
        self._run_synthe(tmpdirname, model)
        self._run_spectrv(tmpdirname, model)
        self._run_rotate(tmpdirname, model)
        self._run_broaden(tmpdirname, model)
        self._run_syntoascanga(tmpdirname, model) #converfsynnmtoa.exe ?

        return Spectrum.from_synthe_spectrum(self.model.parameters, tmpdirname)

    def _run_xnfpelsyn(self, tmpdirname, model):
        # Prepare lines data
        os.symlink(os.path.join(self._atomic_data_path,"lines","he1tables.dat"), os.path.join(tmpdirname,"fort.18"))
        os.symlink(os.path.join(self._atomic_data_path,"lines","molecules.dat"), os.path.join(tmpdirname,"fort.2"))
        os.symlink(os.path.join(self._atomic_data_path,"lines","continua.dat"), os.path.join(tmpdirname,"fort.17"))

        self._call_external_code(tmpdirname,
                                os.path.join(self._kurucz_bin_path, "xnfpelsyn.exe"), 
                                self._extend_model_for_SYNTHE(model)
                                )

    def _run_synbeg(self, tmpdirname, model):
        self._call_external_code(tmpdirname, 
                                os.path.join(self._kurucz_bin_path, "synbeg.exe"), 
                                self._get_synbeg_input(model)
                                )

    def _run_rline2(self, tmpdirname, model):
        # os.symlink(os.path.join(self._atomic_data_path,"lines","gf0600.100"), os.path.join(tmpdirname,"fort.11"))
        os.symlink(os.path.join(self._atomic_data_path,"lines","gfall08oct17.dat"), os.path.join(tmpdirname,"fort.11"))
        self._call_external_code(tmpdirname,
                                os.path.join(self._kurucz_bin_path, "rline2.exe")
                                )
        # self._call_external_code(tmpdirname,
        #                         os.path.join(self._kurucz_bin_path, "rgfalllinesnew.exe")
        #                         )                               
        os.remove(os.path.join(tmpdirname,"fort.11"))

    def _run_rmolecasc(self, tmpdirname, model, molecule_file="coax.dat"):
        os.symlink(os.path.join(self._atomic_data_path, "molecules", molecule_file), os.path.join(tmpdirname, "fort.11"))
        self._call_external_code(tmpdirname,
                        os.path.join(self._kurucz_bin_path, "rmolecasc.exe")
                        )
        os.remove(os.path.join(tmpdirname,"fort.11"))
    

    def _run_synthe(self, tmpdirname, model):
        self._call_external_code(tmpdirname,
                                os.path.join(self._kurucz_bin_path, "synthe.exe")
                                )

    def _run_spectrv(self, tmpdirname, model):
        self._save_to_file(os.path.join(tmpdirname,"fort.5"), self._extend_model_for_SYNTHE(model))
        self._save_to_file(os.path.join(tmpdirname,"fort.25"), self._get_spectrv_string())
        
        self._call_external_code(tmpdirname,
                                os.path.join(self._kurucz_bin_path, "spectrv.exe")
                                )      
    
        os.rename(os.path.join(tmpdirname,"fort.7"), os.path.join(tmpdirname,"spec.bin"))
        os.symlink(os.path.join(tmpdirname,"spec.bin"), os.path.join(tmpdirname,"fort.1"))        

    def _run_rotate(self, tmpdirname, model):
        self._call_external_code(tmpdirname,
                                os.path.join(self._kurucz_bin_path, "rotate.exe"),
                                self._get_rotate_string()
                                )
        
        os.rename(os.path.join(tmpdirname,"ROT1"), os.path.join(tmpdirname,"spec.bin"))
        os.symlink(os.path.join(tmpdirname,"spec.bin"), os.path.join(tmpdirname,"fort.21"))
        os.remove(os.path.join(tmpdirname,"fort.1"))
        os.remove(os.path.join(tmpdirname,"fort.5"))

    def _run_broaden(self, tmpdirname, model):
        os.symlink(os.path.join(tmpdirname,"br_spec.bin"), os.path.join(tmpdirname,"fort.22"))
        self._call_external_code(tmpdirname,
                                os.path.join(self._kurucz_bin_path, "broaden.exe"),
                                self._get_broaden_string()
                                )

    def _run_syntoascanga(self, tmpdirname, model):
        for f in glob.glob(os.path.join(tmpdirname,"fort.*")):
            os.remove(f)
        os.symlink(os.path.join(tmpdirname,"br_spec.bin"), os.path.join(tmpdirname,"fort.1"))
        os.symlink(os.path.join(tmpdirname,"br_spec.dat"), os.path.join(tmpdirname,"fort.2"))
        os.symlink(os.path.join(tmpdirname,"line_list.dat"), os.path.join(tmpdirname,"fort.3"))

        self._call_external_code(tmpdirname,
                                os.path.join(self._kurucz_bin_path, "syntoascanga.exe")
                                )
        # self._call_external_code(tmpdirname,
        #                         os.path.join(self._kurucz_bin_path, "converfsynnmtoa.exe")
        #                         )                            
    def _call_external_code(self, cwd, program_path, input_data=None):
        process = subprocess.Popen([program_path],
                            stdin=subprocess.PIPE,
                            stdout=subprocess.PIPE,
                            encoding='utf8',
                            cwd=cwd)
        outs, errs = process.communicate(input_data)
        process.wait()

    def _extend_model_for_SYNTHE(self, model):
        s = [
            "SURFACE INTENSI 17 1.,.9,.8,.7,.6,.5,.4,.3,.25,.2,.15,.125,.1,.075,.05,.025,.01\n",
            "ITERATIONS 1 PRINT 2 PUNCH 2\n",
            "CORRECTION OFF\n",
            "PRESSURE OFF\n",
            "MOLECULES ON\n",
            "READ MOLECULES\n",
            model.get_model_string()
        ]
        return "".join(s)

    def _get_synbeg_input(self, model):
        s = [
            f"AIR        {self.model.parameters.wave_min/10.:6.1f}    {self.model.parameters.wave_max/10.:6.1f}    600000.    {self.model.parameters.microturbulence:5.2f}    0     30    .0001     1    0\n",
            "AIRorVAC  WLBEG     WLEND     RESOLU    TURBV  IFNLTE LINOUT CUTOFF        NREAD\n"
        ]
        return "".join(s)

    def _save_to_file(self, path, string):
        with open(path,'w') as f:
            f.write(string)

    def _get_spectrv_string(self):
        s = [
        "0.0       0.        1.        0.        0.        0.        0.        0.\n",
        "0.\n",
        "RHOXJ     R1        R101      PH1       PC1       PSI1      PRDDOP    PRDPOW\n"
        ]
        return "".join(s)

    def _get_rotate_string(self):
        s = [
            "    1\n",
            f"{self.model.parameters.vsini:3.0f}."
        ]
        return "".join(s)

    def _get_broaden_string(self):
        return f"GAUSSIAN  {self.model.parameters.resolution:^8.1f}  RESOLUTION"

def main():
    # http://wwwuser.oats.inaf.it/castelli/sources/linuxcodes.html
    # http://wwwuser.oats.inaf.it/castelli/sources/synthe/examples/synthenop.html
    # http://wwwuser.oats.inaf.it/castelli/sources/atlas9/ap00t10000g40k2odfnew.com
    # http://wwwuser.oats.inaf.it/castelli/sources/atlas9codes.html
    # http://wwwuser.oats.inaf.it/castelli/grids/gridp00k2odfnew/ap00k2tab.html
    pass

if __name__ == '__main__':
    main()