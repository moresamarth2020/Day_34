#!/usr/bin/env python
# coding: utf-8

# # How importing in python works
# Importing in Python is the process of loading code from a Python module into the current script. This allows you to use the functions and variables defined in the module in your current script, as well as any additional modules that the imported module may depend on.
# To import a module in Python, you use the import statement followed by the name of the module. For example, to import the math module, which contains a variety of mathematical functions, you would use the following statement:

# In[1]:


import math


# Once a module is imported, you can use any of the functions and variables defined in the module by using the dot notation. For example, to use the sqrt function from the math module, you would write:

# In[2]:


result = math.sqrt(9)
print(result)


# In[4]:


a = int(input("Enter a number:"))
a = math.sqrt(a)
print(a)


# In[5]:


a = int(input("Enter a number:"))

print(math.sqrt(a))


# ### from keyword
# You can also import specific functions or variables from a module using the from keyword. For example, to import only the sqrt function from the math module, you would write:

# In[6]:


from math import sqrt
result=sqrt(9)
print(result)


# You can also import multiple functions or variables at once by separating them with a comma:

# In[7]:


from math import sqrt,pi
result = sqrt(9)
print(result)
print(pi)


# In[16]:


from math import sqrt,pi
a = int(input("Enter a Number:"))
a = sqrt(a),pi
print(a)


# ### importing everything
# It's also possible to import all functions and variables from a module using the * wildcard. However, this is generally not recommended as it can lead to confusion and make it harder to understand where specific functions and variables are coming from.

# In[9]:


from math import *
result=sqrt(8)
print(result)


# In[10]:


from math import *

result = sqrt(9)
print(result)  # Output: 3.0

print(pi)  # Output: 3.141592653589793


# ## The "as" keyword

# In[32]:


import math as m
result = m.sqrt(9), m.pi
print(result)


# ### The dir function
# Finally, Python has a built-in function called dir that you can use to view the names of all the functions and variables defined in a module. This can be helpful for exploring and understanding the contents of a new module.

# In[38]:


import math

print(dir(math))


# In[44]:


print(math.nan,type(nan))


# This will output a list of all the names defined in the math module, including functions like sqrt and pi, as well as other variables and constants.
# In summary, the import statement in Python allows you to access the functions and variables defined in a module from within your current script. You can import the entire module, specific functions or variables, or use the * wildcard to import everything. You can also use the as keyword to rename a module, and the dir function to view the contents of a module.

# In[55]:


# here we used a created sam.py file to importe
from Sam import Wellcome, Sam
Wellcome()
print(Sam)


# In[56]:


from Sam import *
Wellcome()
print(Sam)


# In[57]:


from Sam import Wellcome
Wellcome()
print(Sam)


# In[58]:


import Sam as hr
hr.Wellcome()
print(hr.Sam)


# In[ ]:





# In[ ]:




