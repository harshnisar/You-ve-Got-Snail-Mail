from bs4 import BeautifulSoup
import re
import sys
import pickle
class object:
    
    name = ''
    date = ''
    room = ''
    def __init__(self,name,date,room):
        self.name = name
        self.date = date
        self.room = room
    def equals(self,otherobj):
        return (self.date == otherobj.date) and (self.name == otherobj.name) and (self.room == otherobj.room)
#We don't want to repeat sending mails to people you have already sent in the last scrap.
# To be fetched from the database.
last_checked = object('UDIT','28.11.2013','B207')

#need to load last checked from a file
try:
    last_checked = pickle.load(open("smaildata.txt","rb"))
except:
    pass



def normalizer(text):
    text = text[0]
    
    text = text.encode('ascii','ignore')
    pat = re.compile(r'\t')
    slashless = pat.sub('',text)
    
    alphnum = re.compile(r'[A-Za-z0-9.-]*')
    
    text = alphnum.findall(slashless)    
    return text[1]





def scrapper(soup,last_checked):
    temp = ''
    list = []
    k=re.compile('evtdupcount..?')
    counter = 1
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
        if ob.equals(last_checked):
            break
        #Saving the first in the list in temp, for later storage as the last_checked
        if counter ==1:
            temp = ob
        counter +=1
    
    try:
        last_checked =  temp
        print 'i am here'
        print last_checked.name
        pickle.dump(last_checked,open('smaildata.txt','wb'))
    except:
        pass
    return list







    
ob = object('harsh','12.12.13','b213')


soup = BeautifulSoup(open('snailmail.htm'))

list = scrapper(soup,last_checked)

for l in list:
    print l.name,l.date,l.room

count = 0 