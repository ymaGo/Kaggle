#!/usr/bin/env python
# coding: utf-8

# **This notebook is an exercise in the [Python](https://www.kaggle.com/learn/python) course.  You can reference the tutorial at [this link](https://www.kaggle.com/colinmorris/functions-and-getting-help).**
# 
# ---
# 

# Functions are powerful. Try writing some yourself.
# 
# As before, don't forget to run the setup code below before jumping into question 1.

# In[ ]:


# SETUP. You don't need to worry for now about what this code does or how it works.
from learntools.core import binder; binder.bind(globals())
from learntools.python.ex2 import *
print('Setup complete.')


# # 1.
# 
# Complete the body of the following function according to its docstring.
# 
# HINT: Python has a built-in function `round`.

# In[ ]:


def round_to_two_places(num):
    """Return the given number rounded to two decimal places. 
    
    >>> round_to_two_places(3.14159)
    3.14
    """
    # Replace this body with your own code.
    # ("pass" is a keyword that does literally nothing. We used it as a placeholder
    # because after we begin a code block, Python requires at least one line of code)
    return round(num,2)

# Check your answer
q1.check()


# In[ ]:


# Uncomment the following for a hint
#q1.hint()
# Or uncomment the following to peek at the solution
#q1.solution()


# # 2.
# The help for `round` says that `ndigits` (the second argument) may be negative.
# What do you think will happen when it is? Try some examples in the following cell.

# In[ ]:


# Put your test code here
round(78.63,-1)


# Can you think of a case where this would be useful?  Once you're ready, run the code cell below to see the answer and to receive credit for completing the problem.

# In[ ]:


# Check your answer (Run this code cell to receive credit!)
q2.solution()


# # 3.
# 
# In the previous exercise, the candy-sharing friends Alice, Bob and Carol tried to split candies evenly. For the sake of their friendship, any candies left over would be smashed. For example, if they collectively bring home 91 candies, they'll take 30 each and smash 1.
# 
# Below is a simple function that will calculate the number of candies to smash for *any* number of total candies.
# 
# Modify it so that it optionally takes a second argument representing the number of friends the candies are being split between. If no second argument is provided, it should assume 3 friends, as before.
# 
# Update the docstring to reflect this new behaviour.

# In[ ]:


def to_smash(total_candies,num_child=3):
    """Return the number of leftover candies that must be smashed after distributing
    the given number of candies evenly between 3 friends.
    
    >>> to_smash(91)
    1
    """
    return total_candies % num_child

# Check your answer
q3.check()


# In[ ]:


#q3.hint()


# In[ ]:


#q3.solution()


# # 4. (Optional)
# 
# It may not be fun, but reading and understanding error messages will be an important part of your Python career.
# 
# Each code cell below contains some commented buggy code. For each cell...
# 
# 1. Read the code and predict what you think will happen when it's run.
# 2. Then uncomment the code and run it to see what happens. (**Tip**: In the kernel editor, you can highlight several lines and press `ctrl`+`/` to toggle commenting.)
# 3. Fix the code (so that it accomplishes its intended purpose without throwing an exception)
# 
# <!-- TODO: should this be autochecked? Delta is probably pretty small. -->

# In[ ]:


round_to_two_places(9.9999)


# In[ ]:


x = -10
y = 5
# Which of the two variables above has the smallest absolute value?
def smallest_abs(x,y):
    tem = abs(x)
    if abs(y)<tem:
        return y
    else:
        return x
print(smallest_abs(x,y))


# In[ ]:


def f(x):
    y = abs(x)
    return y

print(f(5))


# # Keep Going
# 
# Nice job with the code. Next up, you'll learn about *conditionals*, which you'll need to **[write interesting programs](https://www.kaggle.com/colinmorris/booleans-and-conditionals)**. 

# ---
# 
# 
# 
# 
# *Have questions or comments? Visit the [course discussion forum](https://www.kaggle.com/learn/python/discussion) to chat with other learners.*
