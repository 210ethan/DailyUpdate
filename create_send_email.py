#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 18 20:02:26 2017

@author: EthanMorse
"""

import DailyUpdateInfo
import smtplib

def create_email_body(cityName,source,sortBy,numArticles,tickerList,numShares):

    email_body = get_weather(cityName) + get_news(source,sortBy,numArticles) + get_stock_info(tickerList,numShares) + get_todo_list(bot_login())

    # replace invalid UNICODE codes with valid codes
    return email_body.encode("utf-8")

def send_email(cityName,source,sortBy,numArticles,tickerList,numShares):

    content = create_email_body(cityName,source,sortBy,numArticles,tickerList,numShares)
    sender = DailyUpdateInfo.gmail_sender
    receiver = DailyUpdateInfo.gmail_receiver
    password = DailyUpdateInfo.gmail_password
    mail = smtplib.SMTP("smtp.gmail.com",587)
    mail.ehlo
    mail.starttls()
    mail.login(sender,password)
    mail.sendmail(sender,receiver,content)
    mail.close()
 
