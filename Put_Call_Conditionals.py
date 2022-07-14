#!/usr/bin/env python
# coding: utf-8

# # Lamae Maharaj 
# # RM714 
# # Assignment 2 Module 3

# In[ ]:


import re
trim = re.compile(r'[^\d.,]+')
stock = input("Current Stock Price:")
stock = trim.sub('', stock)
strike = input("Option Strike Price:")
strike = trim.sub('', strike)
print("Stock price is $"+stock)
print("Strike price is $"+strike)

# Conditional Logic for Call
if stock>strike:
    print("For Call: ITM (In the Money)")
elif strike>stock:
    print("For Call: OTM (Out of the Money)")
else:
    print("For Call: ATM (At the Money)")

# Conditional Logic for Put
if stock>strike:
    print("For Put: OTM (Out of the Money)")
elif stock<strike:
    print("For Put: ITM (In the Money)")
else:
    print("For Put: ATM (At the Money)")


# In[ ]:




