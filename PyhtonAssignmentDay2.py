
# coding: utf-8

# In[30]:


import pandas as pd
data =pd.read_csv("C:\\Users\\xschunduak\\Desktop\\Python\\Customers.csv")
data


# In[24]:


import pandas as pd
data =pd.read_csv("C:\\Users\\xschunduak\\Desktop\\Python\\Customers.csv")
print("Shape:{0}; index :{1}; columns: {2}; dtypes.ndim: {3}".format(data.shape,data.index,data.columns,data.dtypes.ndim))


# In[31]:


import pandas as pd
data =pd.read_csv("C:\\Users\\xschunduak\\Desktop\\Python\\Customers.csv")
missing_value_percentage=data.Customer_Value.isna().mean().round(4)*100
missing_value_percentage


# In[35]:


import pandas as pd
data =pd.read_csv("C:\\Users\\xschunduak\\Desktop\\Python\\Customers.csv")
data.apply(set)data.xs


# In[38]:


import pandas as pd
data =pd.read_csv("C:\\Users\\xschunduak\\Desktop\\Python\\Customers.csv")
data[data.duplicated]


# In[39]:


import pandas as pd
data =pd.read_csv("C:\\Users\\xschunduak\\Desktop\\Python\\Customers.csv")
data[data['Customer_Value']>10000]


# In[60]:


import pandas as pd
data =pd.read_csv("C:\\Users\\xschunduak\\Desktop\\Python\\Customers.csv")
data["Customer Value Segment"]=["High Value Segment" if x>25000 else "Medium Value Segment" if x>10000 and x<=25000 else "Low Value Segment" if x<10000 else "NA" for x in data["Customer_Value"]]
data


# In[64]:


import pandas as pd
data =pd.read_csv("C:\\Users\\xschunduak\\Desktop\\Python\\Customers.csv")
data["Average Revenue Per trip"]=["NA" for x in data["Customer_Value"]]
data["Balance Points"]=["NA" for x in data["Customer_Value"]]
data

