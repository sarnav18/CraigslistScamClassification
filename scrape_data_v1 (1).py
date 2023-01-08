
#import libraries
import time

import requests
from bs4 import BeautifulSoup
import pandas as pd

#startpage
car_name=[]
price_list=[]

#import urls
description=[]
df=pd.read_excel("URL_List_v1.xlsx")
urls=list(df['URL'])
output = pd.DataFrame()

#extract description, price, attributes from each url using beautiful soup
for url in urls:
    page=requests.get(url)
    time.sleep(1)
    soup=BeautifulSoup(page.content,'html.parser')
    try:
        try:
            heading=soup.find('span',{'id':'titletextonly'})
            car_name.append(heading.text)
        except:
            car_name.append("")
        try:
            price=soup.find('span',class_='price')
        
            price_list.append(price.text)
        except:
            price_list.append("")
        try:
            attributes=soup.find_all('p',class_='attrgroup')
            
            attr=[]
            for attribute in attributes:
                spans=attribute.find_all('span')
                for span in spans:
                    text = span.text.strip()
                    attr.append(text)
        except:
            attr.append("")
        
        attrsplit = [item.split(':') for item in attr]
        del attrsplit[0]
        
        attrdict={}
        
        for item in attrsplit:
            attrdict[item[0]]=item[1:]
        output = output.append(attrdict, ignore_index=True)
        try:
            body=soup.find('section',{'id':'postingbody'})
            description.append(body.text)
        except:
            description.append("")
    except:
        
         continue
    print(".................//NEXT......")


#put the data into a dataframe
df1 = pd.DataFrame(output)

consolidated_v1 = pd.DataFrame(list(zip(car_name, urls,price_list,description)),columns =['Car Name', 'Car URL','Price', 'Description'])
result=pd.concat([consolidated_v1,df1], axis=1, sort=False)

#save the data in a file
writer = pd.ExcelWriter('Data_from_URL_v1.xlsx', engine='xlsxwriter')
result.to_excel(writer, sheet_name='data', index=False)
writer.save()   
