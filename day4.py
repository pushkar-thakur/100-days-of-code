import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = {'Age': [20, 30, 40, 50, 60], 'Salary': [20000, 30000, 40000, 50000, 60000], 'Experience': [1, 3, 5, 7, 9]}
df = pd.DataFrame(data)

correlation_matrix = df.corr()

plt.figure(figsize=(6, 4))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f")
plt.title("Feature Correlation Heatmap")
plt.show()
