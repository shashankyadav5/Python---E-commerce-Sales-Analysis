#!/usr/bin/env python
# coding: utf-8

# # E- Commerce Sales Analysis

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np


# In[8]:


df = pd.read_excel (r'C:\Users\Admin\Downloads\archive\Superstore in  the USA.xlsx')


# In[11]:


df.head(5)


# In[12]:


df.shape


# In[13]:


df.isnull().sum()


# # Ship Mode
# 

# In[14]:


df['Ship Mode'].value_counts()


# In[23]:


x = df['Ship Mode'].value_counts().index
y = df['Ship Mode'].value_counts().values


# In[38]:


plt.figure(figsize=(5,4))
plt.pie(y,labels=x,autopct='%0.2f%%')
plt.show()


# In[46]:


plt.figure(figsize=(6,7))
sns.countplot(x='Ship Mode', data=df, hue='Category')
plt.show()


# # Segment

# In[48]:


plt.figure(figsize=(5,4))
sns.countplot(x='Segment',data=df)
plt.show()


# # Category

# In[51]:


plt.figure(figsize=(4,4))
sns.countplot(x='Category',data=df)
plt.show()


# # Order Date

# In[61]:


df['order year']=df['Order Date'].dt.year


# In[62]:


df.info()


# In[63]:


df['order year'].value_counts()


# In[64]:


plt.figure(figsize=(4,4))
sns.countplot(x='order year',data=df)
plt.show()


# # Category by Profit

# In[65]:


sns.barplot(x = 'Category' , y='Profit',data=df,estimator='sum')
plt.show()


# # State by Sales

# In[68]:


df['State'].value_counts()[:5]


# # Region by Sales

# In[75]:


plt.figure(figsize=(6,4))
sns.barplot(x = 'Region', y='Sales',data=df,estimator='sum')
plt.show()

