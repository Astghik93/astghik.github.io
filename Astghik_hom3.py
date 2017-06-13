
# coding: utf-8

# In[1]:

import pandas as pd


# In[2]:

links = ["http://rate.am/am/armenian-dram-exchange-rates/banks/non-cash/2017/06/01/18-45",
        "http://rate.am/am/armenian-dram-exchange-rates/banks/non-cash/2017/06/02/20-15",
        "http://rate.am/am/armenian-dram-exchange-rates/banks/non-cash/2017/06/03/20-15",
        "http://rate.am/am/armenian-dram-exchange-rates/banks/non-cash/2017/06/04/20-15",
        "http://rate.am/am/armenian-dram-exchange-rates/banks/non-cash/2017/06/05/20-15",
        "http://rate.am/am/armenian-dram-exchange-rates/banks/non-cash/2017/06/06/20-15",
        "http://rate.am/am/armenian-dram-exchange-rates/banks/non-cash/2017/06/07/20-15"]


# In[4]:

for i in links:
    rates = pd.read_html(i)
    exr = rates[2]
    print exr[2:19]


# In[5]:

len(rates)


# In[6]:

rates1=pd.read_html("http://rate.am/am/armenian-dram-exchange-rates/banks/non-cash/2017/06/01/18-45")
rates2=pd.read_html("http://rate.am/am/armenian-dram-exchange-rates/banks/non-cash/2017/06/02/20-15")
rates3=pd.read_html("http://rate.am/am/armenian-dram-exchange-rates/banks/non-cash/2017/06/03/20-15")
rates4=pd.read_html( "http://rate.am/am/armenian-dram-exchange-rates/banks/non-cash/2017/06/04/20-15")
rates5=pd.read_html( "http://rate.am/am/armenian-dram-exchange-rates/banks/non-cash/2017/06/05/20-15")
rates6=pd.read_html(  "http://rate.am/am/armenian-dram-exchange-rates/banks/non-cash/2017/06/06/20-15")
rates7=pd.read_html("http://rate.am/am/armenian-dram-exchange-rates/banks/non-cash/2017/06/07/20-15")


# In[8]:

rates1[2]


# In[9]:

rates2[2]


# In[10]:

rates3[2]


# In[52]:

rates4[2]


# In[11]:

rates5[2]


# In[12]:

rates6[2]


# In[13]:

rates7[2]


# In[14]:

import re


# In[15]:

import requests


# In[16]:

url = "https://www.bloomberg.com/quote/SPX:IND"


# In[18]:

response = requests.get(url)


# In[19]:

type(response)


# In[20]:

print(response)


# In[21]:

SP500= response.text


# In[22]:

SP500[:500]


# In[29]:

index= re.sub(r'<|>'," ",SP500)
output=re.findall('"price"\s*([0-9]\S*)',index)


# In[30]:

print(output)


# In[31]:

import json


# In[32]:

input = '''[
    {
    "Movie":"Game of Thrones",
    "Actor":"Peter Dinklage",
    "Role":"Tyrion Lannister"    
    },
    {
    "Movie":"Vikings",
    "Actor":"Travis Fimmel",
    "Role":"Ragnar Lothbrok"  
    },
    {
    "Movie":"The last Kingdom",
    "Actor":{
            "Young Uhtred":"Tom Taylor",
            "Not that young Uhtred":"Alexander Dreymon"
            },
    "Role":"Uhtred of Bebbanburg"
    }
]'''


# In[33]:

movies = json.loads(input)


# In[34]:

type(movies)


# In[35]:

print(movies)


# In[36]:

from pprint import pprint


# In[37]:

pprint(movies)


# In[39]:

for i in movies:
        print"Movie:", i['Movie']
        print "Role:", i["Role"]
        if type(i["Actor"]) == dict:
                print "Actor 1: " , i["Actor"]['Young Uhtred']
                print "Actor 2: " , i["Actor"]['Not that young Uhtred']
        else:
            print "Actor:", i["Actor"], "\n"


# In[40]:

import pandas as pd


# In[41]:

import matplotlib.pyplot as plt


# In[45]:

air_data = pd.read_csv("AirPassengers.csv")


# In[46]:

print air_data.head(144)


# In[47]:

plt.plot(air_data['Passengers'])


# In[48]:

plt.show()


# In[49]:

import re


# In[50]:

import requests


# In[51]:

url = "http://quotes.toscrape.com/"


# In[53]:

response1=requests.get(url)


# In[54]:

type(response1)


# In[55]:

print(response1)


# In[56]:

quotes=response1.text


# In[57]:

quotes[:500]


# In[59]:

output=re.findall("href=\s*(\S*)\s*next",quotes,re.IGNORECASE)
print "http://quotes.toscrape.com"+output[0]

