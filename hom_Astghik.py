
# coding: utf-8

# In[3]:

numberlist= input ("Input some numbers seprated by a comma: ")
def avg(numberlist):
    return sum(numberlist) / len(numberlist)
print avg(numberlist) 


# In[4]:

numberlist2= input ("Input some numbers seprated by a comma: ")
occurrances = input ("Inpute the number of occurrences")
def avg(numberlist2):
    return sum(numberlist2[len(numberlist2)-occurrances:])/occurrances
print avg(numberlist2)


# In[9]:

import random


# In[10]:

random.randint(1,100)


# In[11]:

x = 47
if x in range (50,100):
    print ("win")
elif x in range (1,51):
    print("loss")
elif x==100:
    print ("draw")
else:
    print("something is false")


# In[13]:

import pandas_datareader.data as web


# In[15]:

stocks = web.DataReader(["WMT","TM","DIS"],"google")


# In[20]:

stocklist=["WMT","TM","DIS"]
for f in stocklist:
    data=web.DataReader(f,"google")
    print  data.head(7)


# In[18]:

import matplotlib.pyplot as plt


# In[23]:

stockist=["WMT","DIS","TM"]
for f in stocklist:
    data=plt.plot(web.DataReader(f, 'google')["Close"])
    print(plt.show())


# In[ ]:



