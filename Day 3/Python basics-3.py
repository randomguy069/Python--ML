
# coding: utf-8

# In[4]:


#for loops
seq = [1,2,3,4,5]
for num in seq:
    print(num)


# In[7]:


#while loop
i =1
while i < 5:
    print('i is {}'.format(i))
    i+= 1


# In[9]:


for x in range(0,4):
    print(x)


# In[10]:


list(range(10))


# In[11]:


x= [1,2,3,4]
out=[]
for bob in x:
    out.append(bob**2)


# In[12]:


print(out)


# In[13]:


[num**2 for num in x]


# In[14]:


def my_func(param1):
    return (param1**2)

print(my_func(2))

    


# In[15]:


def namz(defname='Default'):
    """
    Some text
    """
    return("Hello"+defname)

print(namz("Edward"))


# In[17]:


print(namz())


# In[18]:


namz


# In[19]:


def times2(var):
    return (var * 2)
print(times2(3))


# In[20]:


seq = [1,2,3,4,5]
map(times2,seq)


# In[24]:


list(map(lambda num: num *3,seq)) #the lambda multiplies 3


# In[26]:


list(filter(lambda num: num%2 == 0, seq)) #filters out the even nos


# In[30]:


s = 'Hello my name is Logan'
s.lower()


# In[29]:


s.upper()


# In[31]:


s.split() #splitting into white space


# In[34]:


twit = 'Go Sports! #Sports'
twit.split('#')


# In[35]:


d = {'k1':1, 'k2':2}
d.keys()


# In[36]:


d.items()


# In[37]:


d.values()


# In[38]:


lst = [12,3,5]
lst.pop() #last item wil be deleted


# In[39]:


frst = lst.pop(0)


# In[40]:


print(frst)


# In[41]:


lst


# In[42]:


'x' in [1,2,3,4]
'x' in ['x','y']


# In[43]:


x = [(1,2),(3,4),(5,6)]
x[0][0]


# In[44]:


for item in x:
    print(item)


# In[45]:


for (a,b) in x:
    print(b)


# In[46]:


for (a,b) in x:
    print(a)

