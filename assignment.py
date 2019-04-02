#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 31 14:46:03 2019

@author: manzars
"""




from urllib.parse import urljoin
from googletrans import Translator
from bs4 import BeautifulSoup
import requests
url = "http://www.veia.org.vn/download/2018/hoivien2018/DS%20hoi%20vien%20VEIA_2018_Website.htm"
file = open('assignment.csv', 'w')
header = 'Company name, Email\n'
translator = Translator()

file.write(header)
with requests.Session() as session:
    response = session.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    for frame in soup.findAll(['frame', {'name': 'frSheet'}]):
        frame_url = urljoin(url, frame["src"])

        response = session.get(frame_url)
        frame_soup = BeautifulSoup(response.content, 'html.parser') 
        x = frame_soup.findAll('tr')
        break
    
    
k = 0 
for element in x:
    #time.sleep(0.5)
   # print('here')
    if(3 < k < 110):
        if(k != 20 and k != 54 and k != 67):
            tag = element.findAll('td')
            name = ''
            email = []
            try:
                name = tag[1].text.replace('\n', '').replace('\r', '')
                tran = translator.translate(name).text.replace(',', '')
                file.write(tran + ',')
                print(name)
            except:
                name = 'NaN'
                file.write(name + ',')
            try:
                email = tag[4]
                em = email.text.split('\n')
                l = len(em)
                i = 0
                email = []
                for msg in em:
                    email.append(str(msg.replace('\n', '').replace('\r', '').replace('\xa0', '')))
                stri = ''
                for i in range(l):
                    if(i != l-1):
                        stri += str(email[i]).replace(',', '').replace(';', '').replace('/', '') + '|'
                    else:
                        stri += str(email[i]).replace(',', '').replace(';', '').replace('/', '')
                if(len(stri) > 5):
                    file.write(stri + '\n')
                else:
                    file.write('NaN' + '\n')
            except:
                print('NaN')
    k+=1
    
    
file.close()
    
    
import pandas
f = pandas.read_csv('assignment.csv')

    
    
    
    
    
    str(msg.replace('\n', '').replace('\r', '').replace('\xa0', ''))
    
    
    
    
    
'''
k = 0 
for element in x:
    time.sleep(2)
    if(3 < k < 110):
        try:
            name = element.findAll('td', {'class': 'xl91'})
            name = name[0].text.replace('\r\n', '').replace('\n', '')
            print(name)
        except:
            try:
                name = element.findAll('td', {'class': 'xl92'})
                name = name[0].text.replace('\r\n', '').replace('\n', '')
                print(name)
            
                
            except:
                print('NaN')
        
        
        
        
        
    k+=1
    
    
    
'''
    
    
    
#name = x.findAll('td', {'class': 'xl91'})
#name[0].text.replace('\r\n', '').replace('\n', '')

#telephone = x[9].findAll('td', {'class': 'xl93', 'class': 'xl97'})
# p.replace('\n', '').replace('\r', '').replace('\xa0', '').replace(' ', '').split('iệnthoại:')[1].split('Fax')[0]
    
    
#email = x[9].findAll('td', {'class': 'xl95'})
#p = email[0].text
#email = p.replace('\xa0', '').replace('\r', '').replace('\n', '').split('    ')

20, 54,67, 
    
