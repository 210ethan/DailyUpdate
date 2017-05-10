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
    request_url = "http://api.openweathermap.org/data/2.5/weather?id=" + DailyUpdateInfo.owm_IDs[cityName] + "&APPID=" + DailyUpdateInfo.owm_key
    weather_info = requests.get(request_url)
    weather_info = weather_info.json()
    
    name = weather_info["name"]
    min_temp = weather_info["main"]["temp_min"] * (9/5) - 459.67 # convert to °F
    max_temp = weather_info["main"]["temp_max"] * (9/5) - 459.67 
    
    # Sunrise/set is time at which they happen sunrise, sunset is converted 
    # from Epoch time (seconds) to CST

    sunrise = datetime.fromtimestamp(
            int(weather_info["sys"]["sunrise"])).strftime(
                    "%H:%M:%S")
    sunset = datetime.fromtimestamp(
            int(weather_info["sys"]["sunset"])).strftime(
                    "%H:%M:%S")
    
    wind_speed = weather_info["wind"]["speed"]
    # convert wind direction from degrees to cardinal directions
    wind_direction_deg = weather_info["wind"]["deg"]
    
    wind_direction_card = cardinal_direction(wind_direction_deg)

    weather_intro = "Here is what the weather looks like in " + name + "!\n"
    temp = "Minimum temperature: " + str(round(min_temp)) + " F\nMaximum temperature: " + str(round(max_temp)) + " F\n"
    sun = "The sun will rise at " + sunrise + " and set at " + sunset + ".\n"
    wind = "Wind will be blowing at " + str(wind_speed) + " mph to the " + wind_direction_card + ".\n" 
    more_info = "For more info, visit https://openweathermap.org/\n"
    separator = "_"*50 + "\n"
    
    weather_formatted = weather_intro + temp + sun + wind + more_info + separator
    return weather_formatted

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
    
    
