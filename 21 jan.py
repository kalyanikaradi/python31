#!/usr/bin/env python
# coding: utf-8

# In[5]:


#missing value by loc function
import pandas as pd
import numpy as np
data=pd.read_csv('train.csv')


# In[6]:


data.loc[data['Age'].isnull()==True]


# In[7]:


##handling missing data
#1 imutation=adding values to missing parts
# 2 dropping the whole part of data


# In[8]:


data.Age.mean()


# In[9]:


np.mean(data['Age'])


# In[10]:


data['Age'].isnull().sum()


# In[11]:


data['Age'].fillna(value=30)


# In[12]:


data.fillna(method='ffill')


# In[13]:


#using loc function to impute missing on column
data.loc[data["Age"].isnull()==True,'Age']=30


# In[14]:


data.Age.isnull().sum()


# In[15]:


#sorting data
data.head()


# In[16]:


data.sort_values('Pclass',ignore_index=False)


# In[17]:


data.sort_values('Pclass',ignore_index=False,ascending=False)


# In[18]:


data.groupby(data['Pclass']).count()


# In[19]:


#data.groupby(data['Sex'])mean()
data.groupby(data['Pclass']).agg({"Fare":"count"})


# In[20]:


#changing datatype
data['Age']=data.Age.astype('float16')


# In[23]:


data.info()


# In[24]:


data['Fare']=pd.to_numeric(data.Fare,downcast='float')


# In[26]:


data.info()


# In[ ]:




