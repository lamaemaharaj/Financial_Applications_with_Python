#!/usr/bin/env python
# coding: utf-8

# # Lamae Maharaj 
# # RM 714 
# # Assignment 3 Module 4
# # Calculating the Geometric Averages

# In[ ]:


import numpy as np 
returns = np.array([0.04,0.06,-0.03,0.11,0.02,-0.04,0.05,0.10])
def Geom_Avg(returns):
    n = len(returns)
    for i in returns:
        i = i+1
        new_returns = np.array([])
        new_returns = np.append(new_returns,i)
        Prod = np.prod(new_returns)
        Geom_Avg = (Prod**(1/n))-1
    print(Geom_Avg)
Geom_Avg(returns)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




