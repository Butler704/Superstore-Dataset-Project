#!/usr/bin/env python
# coding: utf-8

# ### Project Super Store

# #### In this project the Regional Sales manager for the South asks you to run a report for the following:
# 
# #### Which State in the South  region produced the highest profit ?
# 
# #### Whats the highest selling category ?
# 
# #### Whats the highest selling sub-category ?
# 
# #### Whats the worst selling Category ?
# 
# #### Where do we rank in sales amongst the other regions ?
# 
# 
# 
# 

# In[125]:


import pandas as pd
import matplotlib.pyplot as plt


# In[16]:


df=pd.read_csv("SampleSuperstore.csv")
df.head()


# ##### How many rows and columns are in this dataset?

# In[17]:


df.shape


# ##### What are the Data types for each column ?

# In[18]:


df.dtypes


# ##### Are there any duplicate values in this data set ? 

# In[19]:


df.duplicated().sum()


# ##### Drop any duplicate values from the dataset

# In[20]:


df.drop_duplicates(keep='first',inplace=True)
df.shape


# ##### Are there any null values in this dataset?

# In[21]:


df.isna().sum()


# ##### Filter out the df to only show data from the south region 

# In[22]:


south=df.loc[df['Region']=='South',] # Created a variable to only show datain the southern region
south.Region.unique()


# ##### How many sales were made in the South region ?

# In[23]:


south.Region.value_counts()


# ##### Whats the total profit for the sales region ?

# In[24]:


south.Profit.sum().round(decimals=2)


# ##### Which State in the south had the highest profit ?

# In[25]:


south.groupby("State")[['Profit']].sum().sort_values(by='Profit',ascending=False)


# ###### What was the highest selling category in the south ?

# In[26]:


south.groupby("Category")[['Profit']].sum().sort_values(by='Profit',ascending=False).round(decimals=2)


# ##### Whats percentage did each category make up of the total profit ?¶

# In[95]:


((south.groupby("Category")[['Profit']].sum().sort_values(by='Profit',ascending=False).round(decimals=2)/south_total)*100).round(decimals=2).rename(columns={"Profit":"% of Total_Profit"})


# ###### What was the highest selling sub-category in the south ?

# In[27]:


south.groupby("Sub-Category")[['Profit']].sum().sort_values(by='Profit',ascending=False).round(decimals=2)


# ##### What was the highest selling sub-category in the south by Category ?

# In[71]:


south.groupby(["Category","Sub-Category"])[['Profit']].sum().sort_values(by=["Category",'Profit'],ascending=[True,False]).round(decimals=2)


# ##### Whats the  the average profit and quantity of each sub-category sorted by Category and Profit ?
# 

# In[94]:


south.groupby(["Category","Sub-Category"])[['Profit','Quantity']].mean().round(decimals=2).sort_values(by=['Category','Profit'],ascending=[True,False])


# ##### How do we compare to the other regions Profit ?

# In[101]:


df.groupby('Region').Profit.sum().sort_values(ascending=False).round(decimals=2)


# In[154]:


df.groupby('Region').Profit.sum().sort_values(ascending=False).round(decimals=2).plot(kind='bar')


# ##### How do we compare to the other regions Sales ?

# In[103]:


df.groupby('Region').Category.count().sort_values(ascending=False).round(decimals=2)


# In[151]:


df.groupby('Region').Category.count().sort_values(ascending=False).round(decimals=2).plot.line()


# ##### How do we compare to the other regions sales totals ?

# In[140]:


df.groupby('Region').Sales.sum().round(decimals=2).sort_values(ascending=False)


# In[159]:


df.groupby('Region').Sales.sum().round(decimals=2).sort_values(ascending=False).plot(kind='barh')
plt.xlabel=("Sales_Total")


# ##### Export Df into a CSV file called "Superstore_Final"

# In[ ]:


df.to_csv('Superstore_Final.csv')


# ##### Link to Tableau Dashboard:
# 
# ##### https://public.tableau.com/authoring/SuperStoreDashboard_16573367878550/Dashboard1#1
