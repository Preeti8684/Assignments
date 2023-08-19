#!/usr/bin/env python
# coding: utf-8

# In[2]:


list=[]
n=int(input("Enter size of list"))
for i in range(0,n):
    e=int(input("Enter element of list"))
    list.append(e)
print("Positive no. in list are:")
for i in list:
    if i>=0:
        print(i,end=" ")


# In[ ]:




