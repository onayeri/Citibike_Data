#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd

import os


# In[2]:


# 1. Create a DataFrame for the 201908-citibike-tripdata data. 
citibike_df = pd.read_csv(r"C:\Users\on080\OneDrive\Data Boot Camp\Module_14\citibike\201908-citibike-tripdata.csv")
citibike_df.head()


# In[3]:


# 2. Check the datatypes of your columns. 
citibike_df.dtypes


# In[5]:


# 3. Convert the 'tripduration' column to datetime datatype.
citibike_df["tripduration"] = pd.to_datetime(citibike_df["tripduration"], unit = 's')


# In[6]:


# 4. Check the datatypes of your columns. 
citibike_df.dtypes


# In[9]:


# 5. Export the Dataframe as a new CSV file without the index.
citibike_csv_data = citibike_df.to_csv('citibikedata.csv', index = False)


# In[10]:


citibike_df.head()


# In[ ]:




