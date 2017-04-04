#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr  4 14:01:31 2017

@author: EthanMorse
"""

from rtstock.stock import Stock
import DailyUpdateInfo

def get_stock_info(tickerList):
    
    print("Here is the list of desired stock prices.\n")
    
    for ticker in tickerList:
        stock = Stock(ticker)
        stockInfo = stock.get_latest_price()[0]["LastTradePriceOnly"]
        print(ticker + ": $" + stockInfo + "\n")