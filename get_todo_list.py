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
    
    todo_formatted = ""
    
    current_day = datetime.now()
    current_day_formatted = current_day.strftime("%B %d, %Y")
    month_name = current_day.strftime("%B")
    day_name = current_day.strftime("%A")
    
    todo_intro = "\nHere is your to-do list for " + current_day_formatted + ".\n\n"
    todo_formatted = todo_formatted + todo_intro
    
    for submission in r.subreddit("getdisciplined").new():
        if month_name in submission.title and day_name in submission.title:
            for comment in submission.comments:
                if "Daily:" in comment.body and comment.author == "Awarenesss":
                    comment.body.replace("[ ]","")
                    todo_formatted = todo_formatted + comment.body
                    break
    
    return todo_formatted
