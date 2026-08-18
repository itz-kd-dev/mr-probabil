import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Setup the sample space for two dice
die1_x = range(1, 7) # First die (X)
die2_z = range(1, 7) # Second die (Z)

# 2. Calculate the matrix of values for Y - X
# Since Y = X + Z, then Y - X = Z
data = []
for z in die2_z:
    row = []
    for x in die1_x:
        y = x + z
        # The question asks for the value of Y - X
        row.append(y - x)
    data.append(row)

# Create a DataFrame for easy plotting (Columns = Die 1, Rows = Die 2)
df = pd.DataFrame(data, index=die2_z, columns=die1_x)

# 3. Create the visualization
plt.figure(figsize=(8, 6))

# Identify which cells meet the target condition
condition_met = df >= 6

# Plot the base heatmap in gray for all outcomes
sns.heatmap(df, annot=True,
            cmap=sns.color_palette("light:gray", as_cmap=True),
            cbar_kws={'label': 'Value of Y - X'})

# Overlay a green heatmap to highlight the exact outcomes meeting the condition
sns.heatmap(df, mask=~condition_met, annot=True,
            cmap=sns.color_palette("light:green", as_cmap=True),
            cbar=False)

# Formatting the plot
plt.title(r'Visualization of Outcomes for $Y - X \geq 6$', fontsize=14, pad=15)
plt.xlabel('Outcome of First Die ($X$)', fontsize=12)
plt.ylabel('Outcome of Second Die', fontsize=12)

# Display the plot
plt.show()

# 4. Print the final calculated probability
total_outcomes = df.size
favorable_outcomes = condition_met.sum().sum()
probability = favorable_outcomes / total_outcomes

print(f"Total possible outcomes: {total_outcomes}")
print(f"Outcomes where Y - X >= 6: {favorable_outcomes}")
print(f"Probability: {favorable_outcomes}/{total_outcomes} = {probability:.3f}")
