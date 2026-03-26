# Import required libraries
import numpy as np
import matplotlib.pyplot as plt

# Create epochs list
epochs = list(range(1, 21))

# Generate synthetic loss values (decreasing trend with noise)
np.random.seed(42)
loss = np.exp(-np.array(epochs) / 5) + np.random.normal(0, 0.02, len(epochs))

# -----------------------------
# 1. Line Plot (Loss vs Epoch)
# -----------------------------
plt.figure(figsize=(8, 5))
plt.plot(epochs, loss, marker='o', color='blue', label='Loss')
plt.title('Loss vs Epoch (Line Plot)')
plt.xlabel('Epoch')
plt.ylabel('Loss')
plt.grid(True)
plt.legend()
plt.show()

# -----------------------------
# 2. Scatter Plot (Epoch vs Loss)
# -----------------------------
plt.figure(figsize=(8, 5))
plt.scatter(epochs, loss, color='red')
plt.title('Epoch vs Loss (Scatter Plot)')
plt.xlabel('Epoch')
plt.ylabel('Loss')
plt.grid(True)
plt.show()

# -----------------------------
# 3. Bar Chart (Model Accuracy Comparison)
# -----------------------------
models = ['Model A', 'Model B', 'Model C']
accuracy = [0.85, 0.90, 0.88]

plt.figure(figsize=(8, 5))
plt.bar(models, accuracy, color=['blue', 'green', 'orange'])
plt.title('Model Accuracy Comparison')
plt.xlabel('Models')
plt.ylabel('Accuracy')
plt.ylim(0, 1)
plt.grid(axis='y')
plt.show()