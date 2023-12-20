# webscrape programme that scrapes the names, prices and the page number of an online book store 
from bs4 import BeautifulSoup
import requests
import pandas as pd   # importing libraries 

website= "https://booksagain.co.za/non-fiction/general-non-fiction.html" # the website for scraping

respond = requests.get(website) # requesting the website 

soup = BeautifulSoup(respond.content, "html.parser")

results = soup.find_all('div',{'class':"column main"}) # finding the html code for the category of non-fiction books 


# initialising various lists to store our data 
names = []
prices = [] 
page_num = []

# getting the first element in each array category
for result in results:
    prices.append(result.find('span',{'class':"price"}).get_text())
    names.append(result.find('strong',{'class':"product name product-item-name"}).get_text())
    page_num.append(result.find('strong',{'class':"page"}).get_text())

# adding our results to a dataframe 
bookDetails = []
for bookName, bookPrice, pageNum in zip(names,prices,page_num):
    bookDetails.append({"Names":bookName, "Price":bookPrice, "PageNumber":pageNum})

data = pd.DataFrame(bookDetails)














