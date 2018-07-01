
# coding: utf-8

# In[5]:


import numpy as np


# In[3]:


my_list = [1,2,3]
my_list


# In[6]:


arr = np.array(my_list) #casting to numpy array


# In[8]:


my_mat = [[1,2,3],[4,5,6],[7,8,9]]
np.array(my_mat)


# In[10]:


np.arange(0,11) #creating a numpy array from 0 to 10


# In[11]:


np.arange(0,11,2) #returns even numbers


# In[12]:


np.zeros(3) #numpy array of 0's


# In[13]:


np.zeros((5,5)) #numpy arrays of 5 col and 5 row


# In[14]:


np.ones((3,3)) #numpy array of 1's


# In[17]:


np.linspace(0,5,100) #evenly spaced array with 100 digits


# In[18]:


np.eye(3)#creating identity matrix


# In[19]:


np.random.rand(5)#creating an array of values b/w 0's and 1's (uniform distribution)


# In[20]:


np.random.rand(5,5) #creates a 5 X5 matrix 


# In[21]:


np.random.randn(2)   #2 gaussian distribution numbers generated


# In[22]:


np.random.randn(2,2)


# In[26]:


np.random.randint(0,99,(3,3)) #generates a 3 X 3 matrix with integers from 0 to 99


# In[27]:


arr = np.arange(25)


# In[28]:


arr


# In[29]:


ranarr = np.random.randint(0,50,10)


# In[30]:


ranarr


# In[31]:


arr.reshape(5,5) #reshapes the array with the dimensions as mentioned


# In[32]:


ranarr.max() #returns max value of array


# In[33]:


ranarr.min()#returns  min value of array


# In[34]:


ranarr.argmax() #returns index location of max value


# In[35]:


ranarr.argmin() #returns minimum location of min value


# In[36]:


arr = arr.reshape(5,5)


# In[37]:


arr


# In[38]:


arr.shape #returns dimensions


# In[39]:


type(arr)


# In[40]:


arr.dtype #type of values in array

