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
    def prnt(self):
      print self.name,self.date,self.room
#We don't want to repeat sending mails to people you have already sent in the last scrap.
# To be fetched from the database.
#last_checked = object('UDIT','28.11.2013','B207')

#need to load last checked from a file
try:
    #print oh
    
      
    last_checked = pickle.load(open("smaildata.txt","rb"))
    print type(last_checked)
    print last_checked
except:
    print 'in except'
    last_checked = object('1','','')
    
if str(raw_input('Refresh last_checked? (Y|N)')).upper()=='Y':
  last_checked = object('1','','')

def normalizer(text):
    text = text[0]
    text = text.encode('ascii','ignore')
    pat = re.compile(r'\t')
    slashless = pat.sub('',text)
    alphnum = re.compile(r'[A-Za-z0-9.-]*')
    
    text = alphnum.findall(slashless)    
    return text[2]





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
        troom = troom.replace('-','')
        #print  'up was troom'
        ob = object(tname,tdate,troom)
        #Have you already sent mails, to here and and onwards in the list?
        if ob.equals(last_checked):
	    #last_checked.prnt()
	    #ob.prnt()
	    print 'Job is done already till %s' %(last_checked.name)
            break
        list.append(ob)
        #Saving the first in the list in temp, for later storage as the last_checked
        if counter ==1:
            temp = ob
        counter +=1
    
    try:
	print type(last_checked)
        last_checked =  temp
        pickle.dump(last_checked,open('smaildata.txt','wb'))
    except:
        pass
    return list







    
ob = object('harsh','12.12.13','b213')

#TODO: Need to download the page here




import urllib2
page= urllib2.urlopen('http://hostel.daiict.ac.in/index.php?option=com_eventtableedit&view=default&Itemid=2')
html = page.read()
#print html
soup = BeautifulSoup(html)

list = scrapper(soup,last_checked)

for l in list:
#We need to call the script GAS from here
    print l.name,l.date,l.room
    
    ## google apps url. Removed now. Won't work now.
    url = '////'
    print url
    page= urllib2.urlopen(url)

count = 0 
