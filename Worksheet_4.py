#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Question 1.1
import numpy as np

arr1 = np.arange(5, 26)
print(arr1)


# In[2]:


# Question 1.2
arr2 = np.random.randint(10, 51, size=(3, 4))
print(arr2)


# In[3]:


# Question 2.1
print("Shape:", arr1.shape)
print("Size:", arr1.size)
print("Data type:", arr1.dtype)


# In[4]:


# Question 2.2
print("Shape:", arr2.shape)
print("Size:", arr2.size)
print("Data type:", arr2.dtype)


# In[5]:


# Question 3.1
array1 = np.array([2, 4, 6, 8, 10])
array2 = np.array([1, 3, 5, 7, 9])
print("Array1:", array1)
print("Array2:", array2)


# In[6]:


# Question 3.2
print("Addition:", array1 + array2)
print("Subtraction:", array1 - array2)
print("Multiplication:", array1 * array2)
print("Division:", array1 / array2)


# In[7]:


# Question 4.1
arr3 = np.arange(1, 10).reshape(3, 3)
print(arr3)


# In[8]:


# Question 4.2
print(arr3 * 5)


# In[9]:


# Question 5.1
arr4 = np.arange(10, 26).reshape(4, 4)
print(arr4)


# In[10]:


# Question 5.2
print("Second row:", arr4[1])
print("Last column:", arr4[:, -1])


# In[11]:


# Question 5.3
arr4[0] = 0
print(arr4)


# In[12]:


# Question 6.1
arr5 = np.random.randint(20, 41, 10)
print(arr5)


# In[13]:


# Question 6.2
print(arr5[arr5 > 30])


# In[14]:


# Question 7.1
arr6 = np.arange(11, 23)
print(arr6)


# In[15]:


# Question 7.2
reshaped = arr6.reshape(3, 4)
print(reshaped)


# In[16]:


# Question 8.1
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])
print("Matrix A:\n", A)
print("Matrix B:\n", B)


# In[17]:


# Question 8.2
print("Matrix multiplication:\n", np.dot(A, B))
print("Transpose of A:\n", A.T)


# In[18]:


# Question 9.1
arr7 = np.random.randint(10, 61, 15)
print(arr7)


# In[19]:


# Question 9.2
print("Mean:", np.mean(arr7))
print("Median:", np.median(arr7))
print("Standard deviation:", np.std(arr7))


# In[20]:


# Question 10.1
A = np.array([[2, 1, 3], [0, 5, 6], [7, 8, 9]])
print("Matrix A:\n", A)


# In[21]:


# Question 10.2
det = np.linalg.det(A)
inv = np.linalg.inv(A)
eigenvalues, eigenvectors = np.linalg.eig(A)
print("Determinant:", det)
print("Inverse:\n", inv)
print("Eigenvalues:", eigenvalues)
print("Eigenvectors:\n", eigenvectors)


# In[22]:


# Question 11.1
positions = np.array([[0,0], [2,3], [4,7], [7,10], [10,15]])
dist = np.linalg.norm(positions[-1] - positions[0])
print("Euclidean distance:", dist)


# In[23]:


# Question 11.2
steps = np.diff(positions, axis=0)
total_distance = np.sum(np.linalg.norm(steps, axis=1))
print("Total distance traveled:", total_distance)

