#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr  4 14:01:31 2017

@author: EthanMorse
"""

from rtstock.stock import Stock
import DailyUpdateInfo

def get_stock_info(ticker_list,numShares):
    
    stocks_formatted = ""
    
    stocks_intro = "Here is the list of desired stock prices.\n"
    stocks_formatted = stocks_formatted + stocks_intro
    
    for ticker in ticker_list:
        stock = Stock(ticker)
        stock_info = stock.get_latest_price()[0]["LastTradePriceOnly"]
        stocks_formatted = stocks_formatted + ticker + ": $" + stock_info + "\n"
    
    stock = Stock("VFINX")
    value_of_shares = float(stock.get_latest_price()[0]["LastTradePriceOnly"])*numShares
    value = "Your Vanguard account is worth $" + str(value_of_shares) + ".\n"
    separator = "_"*50 + "\n"
    
    stocks_formatted = stocks_formatted + value + separator
    return stocks_formatted