#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr  4 14:12:14 2017

@author: EthanMorse
"""

import requests
import DailyUpdateInfo

def get_news(source,sortBy,numArticles):
    
    # create the url to get news from
    requestURL = "https://newsapi.org/v1/articles?source=" + str(source) + "&" 
    requestURL = requestURL + str(sortBy) + "=top&apiKey=" + DailyUpdateInfo.news_key
                                                                
    newsArticles = requests.get(requestURL)
    newsArticles = newsArticles.json()

    articlesWanted = []
    
    for article in range(0,numArticles):
        articlesWanted.append(newsArticles["articles"][article])
        
    # clean up name of source
    sourceFixed = source.replace("-"," ")
    sourceFixed = sourceFixed.title()
    newsIntro = "\nHere are the " + sortBy + " stories of the day from " + sourceFixed + ".\n"
    
    newsFormatted = newsIntro + print_articles(articlesWanted)
    return newsFormatted
        
def print_articles(articlesWanted):
    
    articlesFormatted = ""
    
    for article in articlesWanted:
        
        title = article["title"]
        
        if article["author"] == "None":
            author = "No author.\n"
        else:
            author = "Author: " + article["author"] + "\n"
       
        if article["description"] == "None":
            description = "No description.\n"
        else:
            description = article["description"] + "\n"
        
        url = "URL: " + article["url"] + "\n"
        separator = "_"*50 + "\n"
        
        articlesFormatted = articlesFormatted + title + author + description + url + separator
    
    return articlesFormatted
                                                         