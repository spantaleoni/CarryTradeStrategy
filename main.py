#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan  7 18:32:35 2022
# The official interest rate is from Quandl
# REFERENCE: https://quantpedia.com/strategies/fx-carry-trade/
#https://www.quandl.com/data/BCB-Central-Bank-of-Brazil-Statistical-Database?keyword=united%20kingdom&page=2
@author: simonlesflex
"""

import numpy as np
import pandas as pd
import random
from yahoo_fin.stock_info import *

from collections import deque
import quandl

from PortfolioOptimize import *
import telegram_send

tickers = ["USDEUR", "USDZAR", "USDAUD",
           "USDJPY", "USDTRY", "USDINR", 
           "USDCNY", "USDMXN", "USDCAD"]

# creating and initializing a nested list 
countrylist = ['Europe',
              'United States',
              'Great Britain',
              'South Africa',
              'Australia',
              'Japan',
              'Turkey',
              'India',
              'China',
              'Mexico',
              'Canada']

              
Rates = GetGlobalRates("all")

SelRates = [ ]

# creating a pandas dataframe
for index, row in Rates.iterrows():
    #SelRates.append(country, globalRates[globalRates.Name == country].Value)

    if row.Name in countrylist:
        print(row)
        value = row.Value
        SelRates.append([row.Name, value])

print(SelRates)
# Sorting by column 'Country'
quandldata.sort_values(by=['Value'], inplace=True)

print("BUY ", SelRates[-1][0], " -- Current RATES ", SelRates[-1][1])
print("SELL ", SelRates[0][0], "-- Current RATES ", SelRates[0][1])

