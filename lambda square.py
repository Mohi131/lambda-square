#!/usr/bin/env python
# coding: utf-8

# In[8]:


def square_num(n):
    return n*n
l = [4,5,2,9]
result = map(square_num,l)
print(list(result))

