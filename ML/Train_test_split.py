#!/usr/bin/env python
# coding: utf-8

# In[33]:


import pandas as pd


# In[34]:


dataset=pd.read_csv('Salary_Data.csv')
dataset.head()


# In[5]:


#want to predict :DV : y
# predictor : IV : X-> must be 2-d so we do not write dataset.iloc[: ,0](it is 1-d) instead 
# we write like dataset.iloc[: ,0:1]


# In[35]:


X = dataset.iloc[: ,0:1]


# In[36]:


X.shape


# In[37]:


y = dataset.iloc[: ,1]


# In[38]:


from sklearn.model_selection import train_test_split


# In[39]:


X_train, X_test, y_train, y_test=train_test_split(X,y,test_size=0.30,random_state=42)


# In[40]:


len(X_train)


# In[41]:


len(X_test)


# In[42]:


from sklearn.linear_model import LinearRegression


# In[43]:


model = LinearRegression()


# In[44]:


#model trained
#experience
#linear alzebra formula : y = b+wx

model.fit(X_train,y_train)


# In[45]:


X_test


# In[46]:


y_test


# In[47]:


y_pred=model.predict([[7]])


# In[49]:


print(y_pred)


# In[51]:


import matplotlib.pyplot as plt


# In[52]:


plt.scatter(X_test,y_test)


# In[53]:


plt.plot(X_test,y_test)


# In[ ]:




