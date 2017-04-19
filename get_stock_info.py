#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr  4 14:01:31 2017

@author: EthanMorse
"""

from rtstock.stock import Stock
import DailyUpdateInfo

def get_stock_info(ticker_list,numShares):
    
    stockFormatted = ""
    
    stockIntro = "Here is the list of desired stock prices.\n"
    stockFormatted = stockFormatted + stockIntro
    
    for ticker in ticker_list:
        stock = Stock(ticker)
        stockInfo = stock.get_latest_price()[0]["LastTradePriceOnly"]
        stockFormatted = stockFormatted + ticker + ": $" + stockInfo + "\n"
    
    stock = Stock("VFINX")
    valueOfShares = float(stock.get_latest_price()[0]["LastTradePriceOnly"])*numShares
    value = "Your Vanguard account is worth $" + str(valueOfShares) + ".\n"
    separator = "_"*50 + "\n"
    
    stockFormatted = stockFormatted + value + separator
    return stockFormatted