#!/usr/bin/env python
# coding: utf-8

# #  Future Value Calculator

# In[48]:


# Lamae Maharaj 
# Risk Management 714 
# Module 2: Assignment 1

import re
Present_Value = input("Enter the amount you are investing and then press enter:")
trim = re.compile(r'[^\d.,]+')
Present_Value = trim.sub('', Present_Value)
Present_Value = Present_Value.replace(",",'')
Present_Value = float(Present_Value)
Interest_Rate = float(input("Enter the Interest Rate and then press enter:"))
Period = float(input("Amount of Time of Investment (Number of Periods) and press enter:"))
Present_Value = float(Present_Value)
Future_Value = Present_Value*(1+Interest_Rate)**Period
Future_Value = "{:.2f}".format(Future_Value)
print("Your future value is based on your inputs: $",Future_Value)


#  

# In[ ]:





# In[ ]:




