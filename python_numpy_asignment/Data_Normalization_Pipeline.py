import numpy as np 
np.random.seed(0)
data=np.random.randint(0,50,4) 
mean=data.mean(axis=0)
std=data.std(axis=0)
normalized = (data - mean) / std
reshaped_data= data.reshape(2,2)
print("Original Data:",data)
print("Mean:",mean)
print("Standard Deviation:",std)
print("Normalized Data:",normalized)
print("Reshaped Data Shape:",reshaped_data.shape)