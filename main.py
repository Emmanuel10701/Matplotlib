# Matplotlib: A Comprehensive Guide
#
# This script explores all key concepts of Matplotlib, with examples using Pandas and NumPy.

# Importing Necessary Libraries
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# 1. Introduction to Matplotlib
print("# Introduction to Matplotlib\n")
print("Matplotlib is a versatile library for creating static, animated, and interactive visualizations in Python.")

# Example: Simple Line Plot
x = np.linspace(0, 10, 100)
y = np.sin(x)
plt.plot(x, y)
plt.title("Simple Line Plot")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.show()

# 2. Basic Plotting
print("# Basic Plotting\n")

# Example: Scatter Plot
x = np.random.rand(50)
y = np.random.rand(50)
sizes = np.random.rand(50) * 100
plt.scatter(x, y, s=sizes, alpha=0.5, c='blue')
plt.title("Scatter Plot Example")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.show()

# Example: Bar Plot
categories = ['A', 'B', 'C', 'D']
values = [23, 45, 56, 78]
plt.bar(categories, values, color=['red', 'blue', 'green', 'orange'])
plt.title("Bar Plot Example")
plt.xlabel("Categories")
plt.ylabel("Values")
plt.show()

# Example: Histogram
data = np.random.randn(1000)
plt.hist(data, bins=30, color='purple', alpha=0.7)
plt.title("Histogram Example")
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.show()

# 3. Customizing Plots
print("# Customizing Plots\n")

# Example: Customizing Line Styles and Colors
plt.plot(x, y, label='sin(x)', linestyle='--', color='red')
plt.title("Customized Line Plot")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.legend()
plt.grid(True)
plt.show()

# 4. Working with Subplots
print("# Working with Subplots\n")

# Example: Multiple Subplots
fig, axs = plt.subplots(2, 2, figsize=(10, 8))
axs[0, 0].plot(x, np.sin(x))
axs[0, 0].set_title("Sine Wave")
axs[0, 1].plot(x, np.cos(x))
axs[0, 1].set_title("Cosine Wave")
axs[1, 0].plot(x, np.tan(x))
axs[1, 0].set_title("Tangent Wave")
axs[1, 1].plot(x, -np.sin(x))
axs[1, 1].set_title("Negative Sine Wave")
plt.tight_layout()
plt.show()

# 5. Handling Axes and Ticks
print("# Handling Axes and Ticks\n")

# Example: Customizing Axes
plt.plot(x, y)
plt.title("Custom Axes and Ticks")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.xticks(np.arange(0, 11, 2))
plt.yticks(np.arange(-1, 2, 0.5))
plt.show()

# 6. Adding Legends and Annotations
print("# Adding Legends and Annotations\n")

# Example: Adding Annotations
plt.plot(x, y, label='sin(x)')
plt.annotate('Max', xy=(np.pi / 2, 1), xytext=(2, 0.8),
             arrowprops=dict(facecolor='black', arrowstyle='->'))
plt.title("Annotations Example")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.legend()
plt.show()

# 7. Working with Images
print("# Working with Images\n")

# Example: Displaying an Image
# Create a random image
image = np.random.rand(100, 100)
plt.imshow(image, cmap='viridis', interpolation='nearest')
plt.colorbar()
plt.title("Displaying an Image")
plt.show()

# 8. Advanced Visualizations
print("# Advanced Visualizations\n")

# Example: 3D Plot
from mpl_toolkits.mplot3d import Axes3D
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)
x, y = np.meshgrid(x, y)
z = np.sin(np.sqrt(x**2 + y**2))
ax.plot_surface(x, y, z, cmap='plasma')
plt.title("3D Surface Plot")
plt.show()

# Explore more features and practice using this comprehensive guide.
