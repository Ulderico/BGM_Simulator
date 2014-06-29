__author__ = 'ulrichDePrins'

import numpy as np
import pandas as pd
from TermStructure.TermStructure import TermStructure


class TermStructureInterpolation(TermStructure):
    def __init__(self, termstructure):
        self.__termstructure = termstructure
        self.__ttm = []
        self.__zc_rates = termstructure.get_zc_rates()