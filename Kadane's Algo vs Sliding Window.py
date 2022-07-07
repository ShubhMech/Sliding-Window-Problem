#!/usr/bin/env python
# coding: utf-8

# ## Sliding Window Problems
# 

# In[24]:


arr = [1,12,3,-24,13,-2,-4,15,-2.6,-1.7,15,4]


# In[25]:


k = 3
i = 0
j = 0


# In[ ]:





# In[26]:


curr_sum, max_sum = 0,0


# In[27]:


while j < len(arr)-1 :
    if j-i < k-1:
        curr_sum += arr[j] 
        max_sum = curr_sum
        j += 1
        
    elif j-i == k-1 :
        if i == 0:
            curr_sum += arr[j]
            max_sum = curr_sum
            
        else:
            curr_sum += arr[j]-arr[i-1]
            max_sum = max(curr_sum,max_sum)
            
        i += 1
        j += 1
    
    


# In[29]:


max_sum


# In[30]:


max_sum = arr[0]
curr_sum = 0
for i in range(1,len(arr)):
    curr_sum += arr[i]
    if curr_sum<=0:
        curr_sum = 0
    max_sum = max(max_sum,curr_sum)

    
    
    


# In[31]:


max_sum


# In[ ]:




