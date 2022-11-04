from django.shortcuts import render
import pandas as pd
import csv 
# Imports for Reordering Feature

def send_data(request):

        with open('news_scrapping_data.csv', 'r') as file_obj:
      
            reader_obj = csv.reader(file_obj)
            news = []
            news_details = {}

            for row in reader_obj:
                if row:
                    news_details["url"] = row[1]
                    news_details["title"] = row[0]
                    news_details["description"] = row[2]
                    news.append(news_details)
                

        
        return render(request,'index.html',{'news':news})

