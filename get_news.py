#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr  4 14:12:14 2017

@author: EthanMorse
"""

import requests
import DailyUpdateInfo

def get_news(source,sortBy,numArticles):
    
    requestURL = "https://newsapi.org/v1/articles?source=" + str(source) + "&" 
    requestURL = requestURL + str(sortBy) + "=top&apiKey=" + DailyUpdateInfo.newsKey
                                                                
    newsArticles = requests.get(requestURL)
    newsArticles = newsArticles.json()

    articlesWanted = []
    
    for article in range(0,numArticles):
        articlesWanted.append(newsArticles["articles"][article])
        
    sourceFixed = source.replace("-"," ")
    sourceFixed = sourceFixed.title()
    print("Here are today's",sortBy,"stories from",sourceFixed, + ".\n")
    
    print_articles(articlesWanted)
    
    
        
def print_articles(articlesWanted):
    
    for article in articlesWanted:
        
        print(article["title"])
        
        if article["author"] == "None":
            print("No author.")
        else:
            print("Author:",article["author"])
       
        if article["description"] == "None":
            print("No description.")
        else:
            print(article["description"])
        
        print("URL:",article["url"])
        print()
        
                                                                    
                                                            