#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  5 08:35:07 2017

@author: EthanMorse
"""

import DailyUpdateInfo
import praw
from datetime import datetime

def bot_login():
    
    r = praw.Reddit(username = DailyUpdateInfo.username,
            password = DailyUpdateInfo.password,
            client_id = DailyUpdateInfo.client_id,
            client_secret = DailyUpdateInfo.client_secret,
            user_agent = "/u/Awarenesss' DailyUpdate")
    
    return r

def get_todo_list(r):
    
    currentDay = datetime.now()
    currentDayFormatted = currentDay.strftime("%B %d, %Y")
    monthName = currentDay.strftime("%B")
    dayName = currentDay.strftime("%A")
    
    print("Here's your to-do list for",currentDayFormatted+ ".")
    
    for submission in r.subreddit("getdisciplined").new():
        if monthName in submission.title and dayName in submission.title:
            for comment in submission.comments:
                if "Social/Other:" in comment.body and comment.author == "Awarenesss":
                    comment.body.replace("[ ]","")
                    print(comment.body)
                    return None
            
r = bot_login()
get_todo_list(r)
    
    