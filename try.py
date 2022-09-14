#!/usr/bin/env python
# coding: utf-8

# In[161]:


import pandas as pd


# In[162]:


dataframe = pd.read_csv("training_data.txt")
dataframe.to_csv('training_data.csv',index =None)


# In[163]:


df=dataframe
df


# In[164]:


StandardDeviation = list(df.std())
StandardDeviation


# In[165]:


mean = list(df.mean())
mean


# In[166]:


df.hist();

