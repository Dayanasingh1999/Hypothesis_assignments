#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import scipy.stats as stats
import pandas as pd


# In[16]:


from scipy.stats import ttest_1samp, ttest_ind, ttest_rel


#  Assume Null hyposthesis as Ho: μ1 = μ2 (There is no difference in diameters of cutlets between two units).
# 
# Thus Alternate hypothesis as Ha: μ1 ≠ μ2 (There is significant difference in diameters of cutlets between two units) 2 Sample 2 Tail test applicable

# In[17]:


cut = pd.read_csv("Cutlets.csv")


# In[18]:


UnitA = pd.Series(cut.iloc[:,0])
UnitA


# In[21]:


UnitB = pd.Series(cut.iloc[:,1])
UnitB


# In[22]:


ttest_ind(UnitA.dropna(), UnitB.dropna(), alternative='two-sided')


# ## p-value is greater than α = 0.05 ( 5% significance level). Hence, we accept the null hypothesis

# In[ ]:





# In[ ]:




