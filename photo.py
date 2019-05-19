#!/usr/bin/env python
# coding: utf-8

# In[1]:


import cv2


# In[2]:


x=cv2.VideoCapture(0)


# In[3]:


ret,photo_1=x.read()


# In[4]:


ret


# In[5]:


cv2.imwrite("/root/Desktop/photo.png",photo_1)


# In[6]:


x.release()


# In[ ]:




