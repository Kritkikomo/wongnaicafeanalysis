import os
import bs4
from bs4 import Comment
from selenium import webdriver
import time
import requests
import bs4
import pandas as ps

def html_text_get(url):
    ### this function is to get desired html and return in to text
    
    
    agent = {"User-Agent":'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36'}
    page = requests.get(str(url), headers=agent)
    html_page=bs4.BeautifulSoup(page.text,'html.parser')
    return [html_page,page]
    '''selector = 'span.bd36.bd18-mWeb.text-gray-700'
    name = html_page.select_one(selector)
    print(name.text)'''

def html_gen(url,outputname):
    [soup,b]=html_text_get(url)
    [x.extract() for x in soup.find_all('script')];
    [x.extract() for x in soup.find_all('style')];
    [x.extract() for x in soup.find_all('meta')];
    [x.extract() for x in soup.find_all('noscript')];
    [x.extract() for x in soup.find_all(text=lambda text:isinstance(text, Comment))];
    html =soup.contents
    html = soup.prettify("utf-8")
    with open(str(outputname+'.html'), "wb") as file:
        file.write(html)

def data_scraping(url):

    [html_text,b]=html_text_get(url)
    data=[]

    selector = ['span.bd36.bd18-mWeb.text-gray-700',
                'div.rg14',
                'div.Gap-sc-ilei7b.Container-sc-1lk8ybd.ikRntG.fiCVgM.badge-content',
                "span.rg16.rg14-mWeb.font-highlight.text-gray-500",
                "h2.my-auto.bd16.bd14-mWeb"]
    for i in selector:
        name = html_text.select_one(i)
        data.append(name.text)
    #price range section
    sel ="div._1weidWQshSdU3oH6Fm7DNW"
    name = html_text.select(sel)
    price = name[3]
    sel="span.sc-1kh6w3g-1.hpJBMe"
    priceadd =price.select_one(sel)
    if priceadd == None:
        data.append('')
    else:
        data.append(priceadd.text)
    # seat section    
    if len(name)==4:
        data.append('')
    else:
        seat = name[4]
        seatadd = seat.select_one(sel)
    
        if seatadd == None :
            data.append('')
        else:
            data.append(seatadd.text)
        
    #date and time separate section
    sel ="div._1weidWQshSdU3oH6Fm7DNW"
    name = html_text.select(sel)

    date_time_sec = name[0]

    sel="table.sc-1kh6w3g-8.gdNTro"
    date_time = date_time_sec.select(sel)
    date_time_dic ={}

    for i in date_time:
        date = i.td.text
        firsttime=i.td.find_next_siblings()
        time=[firsttime[0].text]
        if len(i.tr.find_next_siblings('tr'))==0:
            pass
        else:
            for j in i.tr.find_next_siblings('tr'):
                time.append(j.text)
        date_time_dic[date]=time
    data.append(date_time_dic)
    #print(date_time_dic) 
    # type section
    sel="span.sc-bdfBQB.edNVkU.rg16.rg14-mWeb.font-highlight"
    name = html_text.select(sel)
    typ =''
    for i in name:
        typ+= i.text+','    
    data.append(typ)

    # facilities header
    sel ="span.sc-1kh6w3g-11.fFYUJu"
    name = html_text.select(sel)
    facilities_header =[data[0]]
    for i in name:
        facilities_header.append(i.text)
        

    #check that have facilities or not
    sel ="div._1weidWQshSdU3oH6Fm7DNW"
    name = html_text.select(sel)
    hel=str(name[1])

    count=0
    facilities_data_own={}
    for i in facilities_header:
        if count==0:
            facilities_data_own[str(i)]=True
            count +=1
        else:
            check = hel[hel.find(i)-44-36:hel.find(i)-45]
            if 'buIyWl' in check:
                facilities_data_own[str(i)]= True
            else:
                facilities_data_own[str(i)]= False
    data.append([facilities_data_own])
    return data
    
def selenium_opendriver():
    path = 'C:/Medium_selenium/chromedriver.exe'
    driver = webdriver.Chrome(path)

    return driver

def selenium_connection_click(driver,url,click_class): 
    driver.get(url)
    time.sleep(1)
    driver.find_element_by_class_name(click_class).click()
    time.sleep(1)
    return driver

