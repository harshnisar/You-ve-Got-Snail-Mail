from bs4 import BeautifulSoup
import re
import sys
sample = '\n\t\t\t\t\t\t28.11.2013\t\t\t\t\t\t\xa0\n\t\t\t\t\t'

#We don't want to repeat sending mails to people you have already sent in the last scrap.
# To be fetched from the database.
last_checked = object('','','')

def normalizer(text):
    text = text[0]
    
    text = text.encode('ascii','ignore')
    pat = re.compile(r'\t')
    slashless = pat.sub('',text)
    
    alphnum = re.compile(r'[A-Za-z0-9.-]*')
    
    text = alphnum.findall(slashless)    
    return text[1]





def scrapper(soup):
    list = []
    k=re.compile('evtdupcount..?')
    for ele in soup.find_all('td',class_=k):

        date  = ele.find_next_sibling()
        tdate = normalizer(date.contents)
        name  = date.find_next_sibling()
        tname = normalizer(name.contents)
        room  = name.find_next_sibling()
        troom = normalizer(room.contents)
        ob = object(tname,tdate,troom)
        list.append(ob)
        #Have you already sent mails, to here and and onwards in the list?
        if self.ob == last_checked:
            break
    return list






class object:
    name = ''
    date = ''
    room = ''
    def __init__(self,name,date,room):
        self.name = name
        self.date = date
        self.room = room
    
ob = object('harsh','12.12.13','b213')


soup = BeautifulSoup(open('snailmail.htm'))

list = scrapper(soup)

for l in list:
    print l.name

count = 0 