#!/usr/bin/env python
# coding: utf-8

# In[4]:


#importing modules, reading in CSV files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
df_FBI=pd.read_csv(r"C:\Users\rocam\Documents\FBI.csv", sep=',')
df_CRIME=pd.read_csv(r"C:\Users\rocam\Documents\CRIME.csv", sep=',')


# In[5]:


df_FBI


# In[6]:


df_CRIME


# In[7]:


#DQ Checks below
df_FBI.info()


# In[8]:


df_FBI.describe()


# In[9]:


df_CRIME.info()


# In[10]:


df_CRIME.describe()

