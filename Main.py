__author__ = 'ulrichDePrins'

import numpy as np
import pandas as pd
from TermStructure.TermStructure import TermStructure
from TermStructure.TermStructureInterpolation import TermStructureInterpolation

names = ['my_ttm', 'my_zc']
data = pd.read_csv("C:\Documenti\Eclipse_workspace\Interest_Rate_Generator\TS.csv",
                   sep=";", header=None, names=names)

my_ttm = np.array(data.my_ttm)
my_zc = np.array(data.my_zc)
my_ts = TermStructure()
my_ts.set_ttm(my_ttm)
my_ts.set_zc_rates(my_zc)
my_ts_int = TermStructureInterpolation(my_ts)
print(my_ts_int)
print(my_ts_int.get_dimensions())
print(my_ts.get_dimensions())
print(my_ts.get_d_factors())
print(my_ts.get_zc_rates())
print(my_ts.get_ttm())

