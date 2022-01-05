#!/usr/bin/env python
# coding: utf-8

# **This notebook is an exercise in the [Pandas](https://www.kaggle.com/learn/pandas) course.  You can reference the tutorial at [this link](https://www.kaggle.com/residentmario/summary-functions-and-maps).**
# 
# ---
# 

# # Introduction
# 
# Now you are ready to get a deeper understanding of your data.
# 
# Run the following cell to load your data and some utility functions (including code to check your answers).

# In[ ]:


import pandas as pd
pd.set_option("display.max_rows", 5)
reviews = pd.read_csv("../input/wine-reviews/winemag-data-130k-v2.csv", index_col=0)

from learntools.core import binder; binder.bind(globals())
from learntools.pandas.summary_functions_and_maps import *
print("Setup complete.")

reviews.head()


# # Exercises

# ## 1.
# 
# What is the median of the `points` column in the `reviews` DataFrame?

# In[ ]:


median_points = reviews.points.median()

# Check your answer
q1.check()


# In[ ]:


#q1.hint()
#q1.solution()


# ## 2. 
# What countries are represented in the dataset? (Your answer should not include any duplicates.)

# In[ ]:


countries = reviews.country.unique()

# Check your answer
q2.check()


# In[ ]:


#q2.hint()
#q2.solution()


# ## 3.
# How often does each country appear in the dataset? Create a Series `reviews_per_country` mapping countries to the count of reviews of wines from that country.

# In[ ]:


reviews_per_country = reviews.country.value_counts()

# Check your answer
q3.check()


# In[ ]:


#q3.hint()
#q3.solution()


# ## 4.
# Create variable `centered_price` containing a version of the `price` column with the mean price subtracted.
# 
# (Note: this 'centering' transformation is a common preprocessing step before applying various machine learning algorithms.) 

# In[ ]:


centered_price = reviews.price-reviews.price.mean()

# Check your answer
q4.check()


# In[ ]:


#q4.hint()
#q4.solution()


# ## 5.
# I'm an economical wine buyer. Which wine is the "best bargain"? Create a variable `bargain_wine` with the title of the wine with the highest points-to-price ratio in the dataset.
bargain_wine = reviews.points/

# Check your answer
q5.check()
# The cell above doesn't work.

# 

# In[ ]:


reviews['ptp'] = reviews.points/reviews.price
reviews_max = reviews.ptp.idxmax(axis=0, skipna=True)
bargain_wine = reviews.title[reviews_max]

# Check your answer
q5.check()


# In[ ]:


q5.hint()
q5.solution()


# ## 6.
# There are only so many words you can use when describing a bottle of wine. Is a wine more likely to be "tropical" or "fruity"? Create a Series `descriptor_counts` counting how many times each of these two words appears in the `description` column in the dataset.

# In[ ]:


des_tro = sum(reviews.description.map(lambda p: 'tropical' in p))
des_fru = sum(reviews.description.map(lambda p: 'fruity' in p))
# des_data = {'tropical':des_tro,'fruity':des_fru}
# descriptor_counts = pd.Series(data=des_data,index=['tropical','fruity'])
descriptor_counts = pd.Series({'tropical':des_tro,'fruity':des_fru})
# Check your answer
q6.check()


# In[ ]:


q6.hint()
q6.solution()


# ## 7.
# We'd like to host these wine reviews on our website, but a rating system ranging from 80 to 100 points is too hard to understand - we'd like to translate them into simple star ratings. A score of 95 or higher counts as 3 stars, a score of at least 85 but less than 95 is 2 stars. Any other score is 1 star.
# 
# Also, the Canadian Vintners Association bought a lot of ads on the site, so any wines from Canada should automatically get 3 stars, regardless of points.
# 
# Create a series `star_ratings` with the number of stars corresponding to each review in the dataset.

# In[ ]:


def star_rating(row):
    if row.country=='Canada' or row.points>=95:
        row.points=3
    elif row.points>=85:
        row.points=2
    else:
        row.points=1
    return row

star_ratings = reviews.apply(star_rating,axis=1).points

# Check your answer
q7.check()


# map and apply will creat new Series or DataFrame. we need the start_ratings of the new but not the point of the original one. if you code as star_ratings = reviewers.points, you will get the original record. Therefore you should directly assigned the .apply results to the star_ratings.

# In[ ]:


q7.hint()
q7.solution()


# this give me deeper impressions that the .apply map function will creat new DataFrame or Series, it don't need any variable to stored the result.

# I think the output of above code is DataFrame but not Series.

# # Keep going
# Continue to **[grouping and sorting](https://www.kaggle.com/residentmario/grouping-and-sorting)**.

# ---
# 
# 
# 
# 
# *Have questions or comments? Visit the [course discussion forum](https://www.kaggle.com/learn/pandas/discussion) to chat with other learners.*
