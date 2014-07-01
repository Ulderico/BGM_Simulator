__author__ = 'ulrichDePrins'

import numpy as np
import pandas as pd
import TermStructure


class TermStructureInterpolation():
    def __init__(self, termstructure):
        self.__termstructure = termstructure
        self.__ttm = termstructure.get_ttm()
        self.__zc_rates = termstructure.get_zc_rates()
