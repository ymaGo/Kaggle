#!/usr/bin/env python
# coding: utf-8

# **This notebook is an exercise in the [Pandas](https://www.kaggle.com/learn/pandas) course.  You can reference the tutorial at [this link](https://www.kaggle.com/residentmario/indexing-selecting-assigning).**
# 
# ---
# 

# # Introduction
# 
# In this set of exercises we will work with the [Wine Reviews dataset](https://www.kaggle.com/zynicide/wine-reviews). 

# Run the following cell to load your data and some utility functions (including code to check your answers).

# In[ ]:


import pandas as pd

reviews = pd.read_csv("../input/wine-reviews/winemag-data-130k-v2.csv", index_col=0)
pd.set_option("display.max_rows", 5)

from learntools.core import binder; binder.bind(globals())
from learntools.pandas.indexing_selecting_and_assigning import *
print("Setup complete.")


# Look at an overview of your data by running the following line.

# In[ ]:


reviews.head()


# # Exercises

# ## 1.
# 
# Select the `description` column from `reviews` and assign the result to the variable `desc`.

# In[ ]:


# Your code here
desc = reviews['description']
print(type(desc))
# Check your answer
q1.check()


# Follow-up question: what type of object is `desc`? If you're not sure, you can check by calling Python's `type` function: `type(desc)`.

# In[ ]:


#q1.hint()
#q1.solution()


# ## 2.
# 
# Select the first value from the description column of `reviews`, assigning it to variable `first_description`.

# In[ ]:


first_description = reviews['description'][0]
first_description = reviews.descrption.iloc[0]

# Check your answer
q2.check()
first_description


# In[ ]:


#q2.hint()
#q2.solution()


# ## 3. 
# 
# Select the first row of data (the first record) from `reviews`, assigning it to the variable `first_row`.

# In[ ]:


first_row = reviews.iloc[0]

# Check your answer
q3.check()
first_row


# In[ ]:


#q3.hint()
#q3.solution()


# ## 4.
# 
# Select the first 10 values from the `description` column in `reviews`, assigning the result to variable `first_descriptions`.
# 
# Hint: format your output as a pandas Series.

# In[ ]:


first_descriptions = reviews['description'][:10]
first_descriptions = reviews.description.iloc[:10]

# Check your answer
q4.check()
first_descriptions


# In[ ]:


#q4.hint()
#q4.solution()


# ## 5.
# 
# Select the records with index labels `1`, `2`, `3`, `5`, and `8`, assigning the result to the variable `sample_reviews`.
# 
# In other words, generate the following DataFrame:
# 
# ![](https://i.imgur.com/sHZvI1O.png)

# In[ ]:


sample_reviews = reviews.iloc[[1,2,3,5,8]]

# Check your answer
q5.check()
sample_reviews


# In[ ]:


#q5.hint()
#q5.solution()


# ## 6.
# 
# Create a variable `df` containing the `country`, `province`, `region_1`, and `region_2` columns of the records with the index labels `0`, `1`, `10`, and `100`. In other words, generate the following DataFrame:
# 
# ![](https://i.imgur.com/FUCGiKP.png)

# In[ ]:


# df = reviews[['country','province','region_1','region_2']].iloc[[0,1,10,100]]

cols = ['country','province','region_1','region_2']
indices = [0,1,10,100]
df = reviews.loc[indices,cols]
# Check your answer
q6.check()
df


# In[ ]:


q6.hint()
q6.solution()


# ## 7.
# 
# Create a variable `df` containing the `country` and `variety` columns of the first 100 records. 
# 
# Hint: you may use `loc` or `iloc`. When working on the answer this question and the several of the ones that follow, keep the following "gotcha" described in the tutorial:
# 
# > `iloc` uses the Python stdlib indexing scheme, where the first element of the range is included and the last one excluded. 
# `loc`, meanwhile, indexes inclusively. 
# 
# > This is particularly confusing when the DataFrame index is a simple numerical list, e.g. `0,...,1000`. In this case `df.iloc[0:1000]` will return 1000 entries, while `df.loc[0:1000]` return 1001 of them! To get 1000 elements using `loc`, you will need to go one lower and ask for `df.iloc[0:999]`. 

# In[ ]:


df = reviews.loc[:99,['country','variety']]

# Check your answer
q7.check()
df


# In[ ]:


#q7.hint()
#q7.solution()


# ## 8.
# 
# Create a DataFrame `italian_wines` containing reviews of wines made in `Italy`. Hint: `reviews.country` equals what?

# In[ ]:


italian_wines = reviews.loc[reviews.country=='Italy']

# Check your answer
q8.check()


# In[ ]:


#q8.hint()
#q8.solution()


# ## 9.
# 
# Create a DataFrame `top_oceania_wines` containing all reviews with at least 95 points (out of 100) for wines from Australia or New Zealand.

# In[ ]:


top_oceania_wines = reviews.loc[((reviews.country=='Australia') | (reviews.country=='New Zealand')) & (reviews.points>=95) ]
# top_oceania_wines = reviews.loc[(reviews.country.isin(['Australia','New Zealand']))&(reviews.points>=95) ]
# Check your answer
q9.check()
top_oceania_wines


# In[ ]:


q9.hint()
q9.solution()


# # Keep going
# 
# Move on to learn about **[summary functions and maps](https://www.kaggle.com/residentmario/summary-functions-and-maps)**.

# ---
# 
# 
# 
# 
# *Have questions or comments? Visit the [course discussion forum](https://www.kaggle.com/learn/pandas/discussion) to chat with other learners.*
