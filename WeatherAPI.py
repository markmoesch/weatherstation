
# coding: utf-8

# In[27]:


import numpy as np
import pandas as pd
from pandas import Series, DataFrame
from pandas import read_html

import json
import requests


# In[29]:


weather = requests.get('http://api.wunderground.com/api/3341f7c502c2a6df/history_20121202/q/CA/San_Francisco.json')


# In[38]:


json_data = weather.json()


# In[39]:


json_data


# In[24]:





# In[16]:


dframe.columns.values

