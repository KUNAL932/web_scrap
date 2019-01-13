from bs4 import BeautifulSoup
import requests

website_address="http://quotes.toscrape.com"
result=requests.get(website_address,verify=False)

soup=BeautifulSoup(result.text,"html.parser")
# print(soup.prettify())

# quotation=soup.find("span",{"class":"text"}).text
# print(quotation)
# author=soup.find("small",{"class":"author"}).text
# print(author)

quotation_list=[]
author_list=[]
quotes_dict={}


quotes=soup.findAll("div",{"class":"quote"})
for quote in quotes:
    quotation=quote.find("span",{"class":"text"}).text
    #print(quotation)
    quotation_list.append(quotation)

    author=quote.find("small",{"class":"author"}).text
    #print(author)
    author_list.append(author)


quotes_dict['Quotation']=quotation_list
quotes_dict['Name']=author_list


import pandas as pd
data=pd.DataFrame(data=quotes_dict)

print(data)
data.to_csv("quotation.csv")