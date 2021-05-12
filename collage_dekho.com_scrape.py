from requests import get
from bs4 import BeautifulSoup as b
import time,json 
def main_():   
    page=get('https://www.collegedekho.com/btech-colleges-in-india/')
    soup=b(page.content,'html.parser')
    link_=[]
    title=soup.findAll('div',class_="collegeinfo")
    for i in title: link_.append('https://www.collegedekho.com/'+i.find('div',class_='title').a['href'])
    return link_

def info(links):
    lst,d=[],{}
    for i in links:
        page=get(i)
        soup=b(page.content,'html.parser')
        d['name']=soup.find('div',class_="collegeInfo").find('h1',class_="tooltip").text.split('\n')[0].strip()
        d['phone']=soup.find('div',class_="collegeAddress").find('div',class_='data').text.split('\n')[3].strip()
        d['email']=soup.find('div',class_="collegeAddress").findAll('div',class_='data')[1].text.strip()
        d['website']=soup.find('div',class_="collegeAddress").findAll('div',class_='data')[2].text.strip()
        d['address']=soup.find('div',class_="collegeAddress").findAll('div',class_='data')[3].text.strip()
        facility=[]
        try:    
            f=soup.find('div',class_="block facilitiesBlock").find('div',class_="box").findAll('div',class_='title')
            for i in f: facility.append(i.text)
            d['facilities']=facility
        except: pass
        d['college_type']=soup.find('div',class_='block commonCarousel highlightBlock').find('td',class_="data").text
        try: d['rating']=soup.find('div',class_='reviewsBlock').find('div',class_="star-dv").text.split('\n')[1].strip()
        except: d['rating']='No Rating'
        lst.append(d.copy())
    with open('/home/muhammad_siddik_akbar/Desktop/Python/College_dekho/college.json','w') as c:
        c.write(json.dumps(lst,indent=4))
        c.close()
info(main_())