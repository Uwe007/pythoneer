# -*- coding: utf-8 -*-
"""
Created on Fri Feb 16 16:45:42 2018

@author: Uwe
"""

def clear_all():
    """Clears all the variables from the workspace of the spyder application."""
    gl = globals().copy()
    for var in gl:
        if var[0] == '_': continue
        if 'func' in str(globals()[var]): continue
        if 'module' in str(globals()[var]): continue
    del globals()[var]
if __name__ == "__main__":
    clear_all()
###############################################################################
## MAKING A SCRAPE SCRIPT BASED ON BeautifulSoup: #############################
###############################################################################

import requests
page = requests.get("http://www.mediamarkt.nl/nl/category/_smartphones-483222.html?ga_query=smartphones")
from bs4 import BeautifulSoup
soup = BeautifulSoup(page.content, 'html.parser')

#lookup strings ##############################################################
vp="var product" # lookup string 
n="name" # lookup string 
i="id" # lookup string 
p="price" # lookup string 
b="brand" # lookup string 
e="ean" # lookup string 
d25="dimension25" # lookup string  
d26="dimension26" # lookup string 
d24="dimension24" # lookup string 
c="category" # lookup string 
d9="dimension9" # lookup string 
d10="dimension10" # lookup string 
quotes='"'
dp=":"
comma=","
end="</"

# class="timeframe timeframe-no-animation" data-cutoff="2018-02-16T22:59Z" data-cutoff-human="23:59" data-timeframe-delay="0"></p>
#"name":"SAMSUNG Galaxy J3 2017 16 GB Zwart","id":"1527884","price":"169.00","brand":"SAMSUNG","ean":"8806088917146","dimension25":"InStock","dimension26":1.99,"dimension24":21.00,"category":"Telecom & Navigatie","dimension9":"Mobiele telefoons","dimension10":"Smartphones"};</script><div class="product-wrapper" data-age-rating="0" data-gtm-impression-event="EEC_PRODUCT_IMPRESSION" data-gtm-impression-event-ext="product1527884" data-modelnumber="1527884" data-reco-pid="MMNL1527884">

#  n="name"  
position=0 # startvalue
name=[]
while soup.text.find(vp,position)>=0: 
    name.append(soup.text[soup.text.find(quotes,soup.text.find(quotes,soup.text.find(n,soup.text.find(vp,position)))+1)+1 : soup.text.find(quotes,soup.text.find(quotes,soup.text.find(quotes,soup.text.find(n,soup.text.find(vp,position)))+1)+1)])
    position = soup.text.find(quotes,soup.text.find(quotes,soup.text.find(n,soup.text.find(vp,position)))+1)+1

#  i="id"  
position=0 # startvalue
id=[]
while soup.text.find(vp,position)>=0: 
    id.append(soup.text[soup.text.find(quotes,soup.text.find(quotes,soup.text.find(i,soup.text.find(vp,position)))+1)+1 : soup.text.find(quotes,soup.text.find(quotes,soup.text.find(quotes,soup.text.find(i,soup.text.find(vp,position)))+1)+1)])
    position = soup.text.find(quotes,soup.text.find(quotes,soup.text.find(i,soup.text.find(vp,position)))+1)+1

#  p="price"  
position=0 # startvalue
price=[]
while soup.text.find(vp,position)>=0: 
    price.append(soup.text[soup.text.find(quotes,soup.text.find(quotes,soup.text.find(p,soup.text.find(vp,position)))+1)+1 : soup.text.find(quotes,soup.text.find(quotes,soup.text.find(quotes,soup.text.find(p,soup.text.find(vp,position)))+1)+1)])
    position = soup.text.find(quotes,soup.text.find(quotes,soup.text.find(p,soup.text.find(vp,position)))+1)+1

#  b="brand"  
position=0 # startvalue
brand=[]
while soup.text.find(vp,position)>=0: 
    brand.append(soup.text[soup.text.find(quotes,soup.text.find(quotes,soup.text.find(b,soup.text.find(vp,position)))+1)+1 : soup.text.find(quotes,soup.text.find(quotes,soup.text.find(quotes,soup.text.find(b,soup.text.find(vp,position)))+1)+1)])
    position = soup.text.find(quotes,soup.text.find(quotes,soup.text.find(b,soup.text.find(vp,position)))+1)+1

#  e="ean"  
position=0 # startvalue
ean=[]
while soup.text.find(vp,position)>=0: 
    ean.append(soup.text[soup.text.find(quotes,soup.text.find(quotes,soup.text.find(e,soup.text.find(vp,position)))+1)+1 : soup.text.find(quotes,soup.text.find(quotes,soup.text.find(quotes,soup.text.find(e,soup.text.find(vp,position)))+1)+1)])
    position = soup.text.find(quotes,soup.text.find(quotes,soup.text.find(e,soup.text.find(vp,position)))+1)+1

#  d25="dimension25"   
position=0 # startvalue
dimension25=[]
while soup.text.find(vp,position)>=0: 
    dimension25.append(soup.text[soup.text.find(quotes,soup.text.find(quotes,soup.text.find(d25,soup.text.find(vp,position)))+1)+1 : soup.text.find(quotes,soup.text.find(quotes,soup.text.find(quotes,soup.text.find(d25,soup.text.find(vp,position)))+1)+1)])
    position = soup.text.find(quotes,soup.text.find(quotes,soup.text.find(d25,soup.text.find(vp,position)))+1)+1

#  d26="dimension26"  
position=0 # startvalue
dimension26=[]
while soup.text.find(vp,position)>=0: 
    dimension26.append(soup.text[soup.text.find(dp,soup.text.find(quotes,soup.text.find(d26,soup.text.find(vp,position)))+1)+1 : soup.text.find(comma,soup.text.find(quotes,soup.text.find(quotes,soup.text.find(d26,soup.text.find(vp,position)))))])
    position = soup.text.find(dp,soup.text.find(quotes,soup.text.find(d26,soup.text.find(vp,position)))+1)+1

#  d24="dimension24"  
position=0 # startvalue
dimension24=[]
while soup.text.find(vp,position)>=0: 
    dimension24.append(soup.text[soup.text.find(dp,soup.text.find(quotes,soup.text.find(d24,soup.text.find(vp,position)))+1)+1 : soup.text.find(comma,soup.text.find(quotes,soup.text.find(quotes,soup.text.find(d24,soup.text.find(vp,position)))))])
    position = soup.text.find(dp,soup.text.find(quotes,soup.text.find(d24,soup.text.find(vp,position)))+1)+1

#  c="category"  
position=0 # startvalue
category=[]
while soup.text.find(vp,position)>=0: 
    category.append(soup.text[soup.text.find(quotes,soup.text.find(quotes,soup.text.find(c,soup.text.find(vp,position)))+1)+1 : soup.text.find(quotes,soup.text.find(quotes,soup.text.find(quotes,soup.text.find(c,soup.text.find(vp,position)))+1)+1)])
    position = soup.text.find(quotes,soup.text.find(quotes,soup.text.find(c,soup.text.find(vp,position)))+1)+1

#  d9="dimension9"  
position=0 # startvalue
dimension09=[]
while soup.text.find(vp,position)>=0: 
    dimension09.append(soup.text[soup.text.find(quotes,soup.text.find(quotes,soup.text.find(d9,soup.text.find(vp,position)))+1)+1 : soup.text.find(quotes,soup.text.find(quotes,soup.text.find(quotes,soup.text.find(d9,soup.text.find(vp,position)))+1)+1)])
    position = soup.text.find(quotes,soup.text.find(quotes,soup.text.find(d9,soup.text.find(vp,position)))+1)+1

#  d10="dimension10" 
position=0 # startvalue
dimension10=[]
while soup.text.find(vp,position)>=0: 
    dimension10.append(soup.text[soup.text.find(quotes,soup.text.find(quotes,soup.text.find(d10,soup.text.find(vp,position)))+1)+1 : soup.text.find(quotes,soup.text.find(quotes,soup.text.find(quotes,soup.text.find(d10,soup.text.find(vp,position)))+1)+1)])
    position = soup.text.find(quotes,soup.text.find(quotes,soup.text.find(d10,soup.text.find(vp,position)))+1)+1

import pandas as pd
mediamarkt_smartphones= pd.DataFrame({"name":name,"id" :id,"price" :price,"brand" :brand,"ean" :ean,"dimension25":dimension25,"dimension26" :dimension26,"dimension24" :dimension24,"category" :category,"dimension09" :dimension09,"dimension10":dimension10})

# watch
print(mediamarkt_smartphones)




