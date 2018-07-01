
# coding: utf-8

# In[1]:


1 #integer
2.0 #float


# In[2]:


1


# In[3]:


2 ** 4 #exponential 


# In[4]:


4 % 2


# In[5]:


4 // 2


# In[6]:


'bob the builder'


# In[7]:


"Wendy's"


# In[8]:


x = 'Hello'
print(x)


# In[9]:


num = 12
name = 'Sam'
print('my number is {} and my name is {}'.format(num,name))


# In[10]:


str = ['sky']
print(str[0])


# In[18]:


st1 = 'abcdefghi'
print(st1[3:6])


# In[19]:


new_list = ['a','b','c']


# In[20]:


new_list.append('d')


# In[22]:


new_list
new_list[0]


# In[23]:


nes_list = [1,2,3,[4,5]]


# In[24]:


nes_list[3][1]


# In[25]:


dicti = {'name': 'Kevin', 'age': 24}
dicti['name']


# In[26]:


ind_citi = {'Karnataka':['Bangalore','Mangalore']}
print(ind_citi['Karnataka'][0])


# In[28]:


nes_dic = {'k1':{'innerk':[1,3,4]}}
nes_dic['k1']['innerk'][0]


# In[31]:


tups = (1,2,3)
print(tups[0])


# In[32]:


seaa = {1,2,2,2,2,2,2,4,4,4,4,5,5,5,5,6} #sets are collection of unique elements


# In[33]:


seaa


# In[34]:


seaa.add(7)


# In[35]:


seaa


# In[36]:


1==2


# In[37]:


2==2


# In[40]:


(1<2) and (3<4)
(1>2) or (3<4)


# In[42]:


if 1 > 2:
    print('awesome')
else:
    print('not awesome')


# In[43]:


country = 'India'
if country == 'UK':
    print('Hmmm')
elif country == 'India':
    print('Hmmm * 2')
else:
    print('no hmmms for you')

