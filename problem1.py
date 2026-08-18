import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Grid set up karna (0 se 5 cars/bikes tak)
x_values = np.arange(6)
y_values = np.arange(6)

# 2. 2D grid banana 
X, Y = np.meshgrid(x_values, y_values)

# 3. Joint PMF calculate karna
# Z matrix me har (x, y) combination ki probability store hogi
Z = 9 / (16 * (4**(X + Y)))

# 4. Heatmap plot karna
plt.figure(figsize=(10, 8))
# annot=True values dikhane ke liye, fmt=".4f" 4 decimal places tak
ax = sns.heatmap(Z, annot=True, fmt=".4f", cmap="YlGnBu", 
                 xticklabels=x_values, yticklabels=y_values)

# 5. Axes labels aur formatting
plt.xlabel("Number of Cars (X)", fontsize=12)
plt.ylabel("Number of Bikes (Y)", fontsize=12)
plt.title("Joint PMF of Cars (X) and Bikes (Y)", fontsize=14)

# Heatmap ko origin (0,0) bottom-left me set karne ke liye
ax.invert_yaxis() 

plt.show()
