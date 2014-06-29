__author__ = 'ulrichDePrins'
'''
Created on 25/giu/2014

@author: ulrichDePrins
'''

import numpy as np
import pandas as pd

class TermStructure:
    '''
    classdocs
    '''

    def __init__(self):
        self.__ttm = []
        self.__zc_rates = []
        self.__d_factors = []

    def set_ttm(self, ttm):
        self.__ttm = ttm

    def set_zc_rates(self, zc_rates):
        self.__zc_rates = zc_rates

    def get_ttm(self):
        return self.__ttm

    def get_zc_rates(self):
        return self.__zc_rates

    def get_dimensions(self):
        if self.__ttm.shape[0] != self.__zc_rates.shape[0]:
            print("Dimensions maturity and rate vectors are not the same")
        else:
            return self.__ttm.shape[0]

    def get_d_factors(self):
        self.__d_factors = np.zeros((self.__ttm.shape[0]))
        i = 0
        while self.__ttm[i] < 1:
            self.__d_factors[i] = 1 / (1 + self.__zc_rates[i] * self.__ttm[i])
            i += 1
        while i <= self.__ttm.shape[0] - 1:
            self.__d_factors[i] = 1 / ((1 + self.__zc_rates[i]) ** self.__ttm[i])
            i += 1
        return self.__d_factors