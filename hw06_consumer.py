#!/usr/bin/env python
# coding: utf-8

# In[1]:


from pyspark.sql import SparkSession
spark = SparkSession.builder.getOrCreate()


# In[2]:


spark


# In[3]:


# connect and stream (no output, will say connected on producer)
stream_df = (spark.readStream.format('socket')
                            .option('host', 'localhost')
                            .option('port', '22223')
                            .load())

# set up to ingest the data (no output)
json_df = stream_df.selectExpr("CAST(value AS STRING) AS payload")

writer = (
    json_df.writeStream
           .queryName('iss')
           .format('memory')
           .outputMode('append')
)

streamer = writer.start()


# In[4]:


import time

for _ in range(5):
    df = spark.sql("""
    SELECT CAST(get_json_object(payload, '$.iss_position.latitude') AS FLOAT) AS latitude,
           CAST(get_json_object(payload, '$.iss_position.longitude') AS FLOAT) AS longitude 
    FROM iss
    """)
    
    df.show(5)
    
time.sleep(5)
    
streamer.awaitTermination(timeout=3600) #seconds
print('..fully loaded')


# In[5]:


df.head()


# In[6]:


df.columns


# In[7]:


# how to get values from df's latitude list and vice versa
df.select('latitude').collect()


# In[ ]:


# sooo the dataframe is a list like ['lat','long'] but we want it to be [('lat','long'),('lat2','long2')]


# In[8]:


latitude_list = []
longitude_list = []


# In[9]:


# when iterating with zip, you get 2 variables corresponding 
# to the current val of each loop. 
# so you can get lat and long value pairs at point 0,1,2,n,n+1
for x,y in zip(df.select('latitude').collect(), df.select('longitude').collect()):
    latitude_list.append(x[0])    # add current lat val to list
    longitude_list.append(y[0])   # add current lon val to list 


# In[10]:


df.dtypes


# In[11]:


import pandas as pd
import geopandas

# geopandas wont work with original df
# ValueError = gives setting an array element with a sequence.
# so have to make new one 

new_df = pd.DataFrame(list(zip(latitude_list,longitude_list)), columns=['latitude','longitude'])

new_df.dtypes


# In[ ]:


# ******* following PLOTLY tutorial from their website ******* #


# In[12]:


# now that we have a correct dataframe type for geopandas, lets TRY 
geo_df = geopandas.GeoDataFrame(new_df, geometry=geopandas.points_from_xy(new_df.latitude,new_df.longitude))
print(geo_df.head())


# In[13]:


import plotly.express as px

# now we plot the coordinates onto a WORLD map
world = geopandas.read_file(geopandas.datasets.get_path('naturalearth_cities'))

fig = px.scatter_geo(new_df,lat='latitude',lon='longitude')
fig.update_layout(title='2022-4-13 22:43:00 EDT TO 2022-4-13 23:43:00 EDT',title_x=0.5)
fig.show()


# In[ ]:





# In[ ]:




