#!/usr/bin/env python
# coding: utf-8

# In[127]:


from requests import get
lok={}
for j in range(1,3001,50):
    r=get(f"https://www.imdb.com/search/title/?title_type=feature,tv_movie,short&release_date=2019-01-01,2021-12-31&sort=num_votes,desc&start={j}&ref_=adv_nxt")
    from bs4 import BeautifulSoup
    soap=BeautifulSoup(r.content,'html.parser')
    h1=soap.find_all('div',class_="lister-item mode-advanced")
    h2=soap.find_all('span',class_="lister-item-year text-muted unbold")
    h3=soap.find_all('div',class_="inline-block ratings-imdb-rating")
    h4=soap.find_all('div',class_="inline-block ratings-metascore")
    h5=soap.find_all('p',class_='sort-num_votes-visible')
    if 'movien' not in lok:
        lok['movien']=[]
    for i in h1:
        moviename=h1[h1.index(i)].find('h3').find('a').text.strip()
        lok['movien'].append(moviename)
    if 'year' not in lok:
        lok['year']=[]
    for i in h2:
        year=h2[h2.index(i)].text.strip()
        lok['year'].append(year)
    if 'rank' not in lok:
        lok['rank']=[]
    for i in h3:
        rank=h3[h3.index(i)].text.strip()
        lok['rank'].append(float(rank))
    if 'metascore' not in lok:
        lok['metascore']=[]
    for i in h4 :
        metascore=h4[h4.index(i)].span.text.strip()
        lok['metascore'].append(int(metascore))
    if 'vote' not in lok:
        lok['vote']=[]
    for i in h5:
        vote=h5[h5.index(i)].find_all('span')[1].text
        v=list(vote)
        if ',' in v:
            v.remove(',')
        lok['vote'].append(int(''.join(v)))




    
   
   


# In[129]:


len(lok['vote'])


# In[130]:


import json
fname='list of movies.json'
with open(fname,'w') as f:
    json.dump(lok,f)


# In[ ]:




