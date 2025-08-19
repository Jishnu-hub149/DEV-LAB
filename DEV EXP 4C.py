import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

df = sns.load_dataset("tips")

print(df.head())

sns.set(style="whitegrid")

plt.figure(figsize=(6, 4))
sns.scatterplot(data=df, x="total_bill", y="tip", hue="sex", style="time")
plt.title("Scatter Plot: Total Bill vs Tip")
plt.show()

plt.figure(figsize=(6, 4))
sns.boxplot(data=df, x="day", y="total_bill", palette="Set2")
plt.title("Box Plot: Total Bill by Day")
plt.show()

plt.figure(figsize=(6, 4))
sns.countplot(data=df, x="day", hue="sex")
plt.title("Count Plot: Number of Customers by Day and Sex")
plt.show()

plt.figure(figsize=(6, 4))
sns.violinplot(data=df, x="day", y="tip", inner="quartile", palette="muted")
plt.title("Violin Plot: Tip Distribution by Day")
plt.show()

sns.pairplot(df, hue="sex", palette="coolwarm")
plt.suptitle("Pair Plot of All Numerical Columns", y=1.02)
plt.show()

plt.figure(figsize=(6, 4))
sns.heatmap(df.corr(), annot=True, cmap="YlGnBu", linewidths=0.5)
plt.title("Heatmap: Correlation Matrix")
plt.show()
