import numpy as np

np.random.seed(0)
samples=100
features=5
data = np.random.randn(samples,features)
mean=data.mean(axis=0)
std=data.std(axis=0)
normalized = (data - mean) / std
print(normalized)
sliced_index=int(0.8*samples)
training_set=normalized[:sliced_index]
test_set=normalized[sliced_index:]
Original_value=normalized[0,0]
training_set[0,0]=999
modified_value=normalized[0,0]
print("Original data shape:",data.shape)
print("Mean Shape:",mean.shape)
print("Training data Shape",training_set.shape)
print("Test Data Shape:",test_set.shape)
print("Note: Modifying the slice affected the original array")
