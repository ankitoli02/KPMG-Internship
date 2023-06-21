#!/usr/bin/env python
# coding: utf-8

# # Task 1 - Data Quality Assessment

# # Assessment of data quality and completeness in preparation for analysis

# # Introduction :

# Sprocket Central Pvt Ltd , a medium size bikes & cycling accessories organisation, has approached Tony Smith (Partner) in KPMG’s Lighthouse & Innovation Team. Sprocket Central Pty Ltd is keen to learn more about KPMG’s expertise in its Analytics, Information & Modelling team.
# 
# Smith discusses KPMG’s expertise in this space. In particular, he speaks about how the team can effectively analyse the datasets to help Sprocket Central Pty Ltd grow its business.
# 
# Primarily, Sprocket Central Pty Ltd needs help with its customer and transactions data. The organisation has a large dataset relating to its customers, but their team is unsure how to effectively analyse it to help optimise its marketing strategy.
# 
# However, in order to support the analysis, you speak to the Associate Director for some ideas and she advised that “the importance of optimising the quality of customer datasets cannot be underestimated. The better the quality of the dataset, the better chance you will be able to use it drive company growth.”

# # The client provided KPMG with 3 datasets:
# 
# 1. Customer Demographic
# 2. Customer Addresses
# 3. Transactions data in the past 3 months

# In[48]:


import pandas as pd
import numpy as np


# # 1. Exploring Transaction Column

# In[49]:


transactions = pd.read_excel(r"C:\Users\PRAVIN OLIVKAR\Downloads\KPMG_VI_New_raw_data_update_final.xlsx",sheet_name='Transactions',header=1)


# In[50]:


transactions.head()


# In[51]:


transactions.describe()


# In[52]:


transactions.shape


# In[53]:


transactions.info()


# In[54]:


transactions.isnull().sum()


# In[55]:


transactions.duplicated().sum()


# In[56]:


transactions.nunique()


# In[57]:


transactions.columns


# In[58]:


transactions['online_order'].value_counts()


# In[59]:


transactions['brand'].value_counts().head(10)


# In[60]:


transactions['product_line'].value_counts()


# In[61]:


transactions['product_class'].value_counts()


# In[62]:


transactions['product_size'].value_counts()


# # #We can also notice that the 'product_first_sold_date' column is of float datatype which has to be changed to date format.

# In[63]:


transactions['product_first_sold_date'] = pd.to_datetime(transactions['product_first_sold_date'], unit='s')


# In[64]:


transactions['product_first_sold_date'].head() #checking after updation


# # 2. Exploring NewCustomerList column

# In[65]:


NewCustomerList = pd.read_excel(r"C:\Users\PRAVIN OLIVKAR\Downloads\KPMG_VI_New_raw_data_update_final.xlsx",sheet_name='NewCustomerList',header=1)


# In[66]:


NewCustomerList.info()


# In[67]:


NewCustomerList.describe()


# In[68]:


NewCustomerList.isnull().sum()


# In[69]:


NewCustomerList.head()


# In[70]:


#we have to drop irrelevent columns from the dataset
NewCustomerList.drop(['Unnamed: 16','Unnamed: 17','Unnamed: 18','Unnamed: 19','Unnamed: 20'],axis=1,inplace=True)


# In[71]:


#checking that column has dropped or not
NewCustomerList.columns


# In[72]:


NewCustomerList.duplicated().sum()


# In[73]:


#Checking for uniquness of each column
NewCustomerList.nunique()


# In[74]:


NewCustomerList['gender'].value_counts()


# In[75]:


# Renaming the U in gender column as Unspecified
NewCustomerList['gender'] = NewCustomerList['gender'].replace('U','Unspecified')


# In[76]:


# Checking the output
NewCustomerList[NewCustomerList.gender == "Unspecified"]


# In[77]:


NewCustomerList['job_industry_category'].value_counts()


# In[78]:


NewCustomerList['past_3_years_bike_related_purchases'].sum()


# In[79]:


NewCustomerList['owns_car'].value_counts()


# In[80]:


NewCustomerList['state'].value_counts()


# # 3. Customer Demographic 

# In[81]:


Customer_Demo = pd.read_excel(r"C:\Users\PRAVIN OLIVKAR\Downloads\KPMG_VI_New_raw_data_update_final.xlsx",sheet_name='CustomerDemographic',header=1)


# In[82]:


Customer_Demo.info()


# In[83]:


Customer_Demo.shape


# In[84]:


Customer_Demo.describe()


# In[85]:


Customer_Demo.nunique()


# In[86]:


Customer_Demo.isnull().sum()


# In[87]:


Customer_Demo.head()


# In[88]:


#Checking for duplicate data
Customer_Demo.duplicated().sum()


# In[89]:


Customer_Demo['gender'].value_counts()


# The 'default' column seems to have some random text entries in it. And it seems to serve no purpose so it can be dropped from the table. The 'gender' column has entries for male and female specifies by 4 values : 'Male', 'Female', 'M', 'F' and it also has an entry 'U' which means 'Unidentified'. So we will group these data and make them more consistent and correct.

# In[90]:


Customer_Demo = Customer_Demo.drop('default', axis=1)


# In[91]:


Customer_Demo['gender'] = Customer_Demo['gender'].replace('F','Female').replace('M','Male').replace('Femal','Female').replace('U','Unidentified')


# In[92]:


#checking output
Customer_Demo['gender'].value_counts()


# In[93]:


Customer_Demo['owns_car'].value_counts()


# # 4. Customer Address 

# In[94]:


CustomerAddress = pd.read_excel(r"C:\Users\PRAVIN OLIVKAR\Downloads\KPMG_VI_New_raw_data_update_final.xlsx",sheet_name='CustomerAddress',header=1)


# In[95]:


CustomerAddress.shape


# In[96]:


CustomerAddress.describe()


# In[97]:


CustomerAddress.info()


# In[98]:


CustomerAddress.isnull().sum()


# In[99]:


CustomerAddress.duplicated().sum()


# In[100]:


CustomerAddress.nunique()


# In[101]:


CustomerAddress.columns


# In[103]:


CustomerAddress['postcode'].value_counts().head(10)


# In[104]:


CustomerAddress['country'].value_counts()


# In[105]:


CustomerAddress['property_valuation'].value_counts()


# # Conclusion :

# The given data is analysed and investigated in all aspects to inspect the Quality of data with respect to all qualities mentioned in the Data Quality Framework Table
# 
# Accuracy
# 
# Completeness
# 
# Uniqueness
# 
# Validity
# 
# Consistency
# 
# Relevancy
# 
# Timeliness

# In[ ]:




