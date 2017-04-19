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
    request_url = "https://newsapi.org/v1/articles?source=" + str(source) + "&" 
    request_url = request_url + str(sortBy) + "=top&apiKey=" + DailyUpdateInfo.news_key
                                                                
    news_articles = requests.get(request_url)
    news_articles = news_articles.json()

    articles_wanted = []
    
    for article in range(0,numArticles):
        articles_wanted.append(news_articles["articles"][article])
        
    # clean up name of source
    source_fixed = source.replace("-"," ")
    source_fixed = source_fixed.title()
    news_intro = "\nHere are the " + sortBy + " stories of the day from " + source_fixed + ".\n"
    
    news_formatted = news_intro + print_articles(articles_wanted)
    return news_formatted
        
def print_articles(articles_wanted):
    
    articles_formatted = ""
    
    for article in articles_wanted:
        
        title = article["title"]
        
        if article["author"] == "None":
            author = "No author.\n"
        else:
            author = "Author: " + str(article["author"]) + "\n"
       
        if article["description"] == "None":
            description = "No description.\n"
        else:
            description = article["description"] + "\n"
        
        url = "URL: " + article["url"] + "\n"
        separator = "_"*50 + "\n"
        
        articles_formatted = articles_formatted + title + author + description + url + separator
    
    return articles_formatted
                                                         