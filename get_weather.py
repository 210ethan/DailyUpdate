#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr  4 14:00:03 2017

@author: EthanMorse
"""

import requests
import DailyUpdateInfo
from datetime import datetime


def get_weather(cityName):
    
    # create and request the API request URL based on city ID
    requestURL = "http://api.openweathermap.org/data/2.5/weather?id=" + str(DailyUpdateInfo.owmIDs[cityName]) + "&APPID=" + DailyUpdateInfo.owmKey
    weatherInfo = requests.get(requestURL)
    weatherInfo = weatherInfo.json()
    
    name = weatherInfo["name"]
    minTemp = weatherInfo["main"]["temp_min"] * (9/5) - 459.67 # convert to °F
    maxTemp = weatherInfo["main"]["temp_max"] * (9/5) - 459.67 

    # sunrise, sunset is converted from Epoch time (seconds) to CST
    sunrise = datetime.fromtimestamp(
            int(weatherInfo["sys"]["sunrise"])).strftime(
                    "%H:%M:%S")
    sunset = datetime.fromtimestamp(
            int(weatherInfo["sys"]["sunset"])).strftime(
                    "%H:%M:%S")
    
    windSpeed = weatherInfo["wind"]["speed"]
    
    # convert wind direction from degrees to cardinal directions
    windDirectionDeg = weatherInfo["wind"]["deg"]
    
    windDirectionCard = cardinal_direction(windDirectionDeg)
    
    print("Here's what the weather looks like in",name+"!\n")
    print("Minimum temperature:",str(round(minTemp))+"°F\nMaximum temperature:",
          str(round(maxTemp))+"°F\n")
    print("The sun will rise at",sunrise,"and set at",sunset+".\n")
    print("Wind will be blowing at",windSpeed,"mph to the",
          windDirectionCard + ".\n")
    
    print("For more info, visit https://openweathermap.org/")
    
def cardinal_direction(degree):
    
    cardinal = ["NE","North","NW","West","SW","South","SE","East"]
    
    if (degree > 0 and degree < 90):
        return cardinal[0]
    elif (degree == 90):
        return cardinal[1]
    elif (degree > 90 and degree < 180):
        return cardinal[2]
    elif (degree == 180):
        return cardinal[3]
    elif (degree > 180 and degree < 270):
        return cardinal[4]
    elif (degree == 270):
        return cardinal[5]
    elif (degree > 270 and degree < 360):
        return cardinal[6]
    elif (degree == 0 or degree == 360):
        return cardinal[7]
    
    