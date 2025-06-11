import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# --- Part 1: NumPy Operations ---
arr1 = np.array([1, 2, 3, 4, 5])
arr2 = np.array([[1, 2, 3], [4, 5, 6]])

print("Original Array:", arr1)
print("Array + 5:", arr1 + 5)
print("Array * 2:", arr1 * 2)  
print("Square Root:", np.sqrt(arr1))  
print("Sliced Array:", arr1[1:4])
print("Reshaped 2D Array:\n", arr2.reshape(3, 2))
print("Transpose of arr2:\n", arr2.T)  
print("Sum of arr2:", np.sum(arr2))  
print("Mean of arr1:", np.mean(arr1))  
print("Standard Deviation:", np.std(arr1))  

# --- Part 2: Pandas DataFrame Operations ---
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
    'Age': [25, 30, 35, 40, 45],
    'Score': [85, 90, 88, 92, 95],
    'Passed': [True, True, False, True, True]
}
df = pd.DataFrame(data)

print("\nDataFrame:")
print(df)

print("\nDataFrame Info:")
print(df.info())

print("\nStatistics:")
print(df.describe())

print("\nData sorted by Age:")
print(df.sort_values(by='Age', ascending=False))  

print("\nFiltering students with score > 90:")
print(df[df['Score'] > 90]) 

print("\nAdding a new column (Grade based on Score):")
df['Grade'] = pd.cut(df['Score'], bins=[0, 80, 90, 100], labels=['C', 'B', 'A'])
print(df)

print("\nGroupby (Average Age per Grade):")
print(df.groupby('Grade', observed=True)['Age'].mean())  


# --- Part 3: Matplotlib Plots ---

plt.figure(figsize=(6,4))
plt.plot(df['Name'], df['Score'], marker='o', linestyle='--', color='blue')
plt.title('Scores of Students')
plt.xlabel('Name')
plt.ylabel('Score')
plt.grid(True)
plt.show()

plt.figure(figsize=(6,4))
plt.bar(df['Name'], df['Age'], color='orange', edgecolor='black')
plt.title('Age of Students')
plt.xlabel('Name')
plt.ylabel('Age')
plt.show()

plt.figure(figsize=(6,4))
plt.pie(df['Score'], labels=df['Name'], autopct='%1.1f%%', startangle=90, colors=['red', 'blue', 'green', 'purple', 'orange'])
plt.title('Score Distribution')
plt.show()

plt.figure(figsize=(6,4))
plt.hist(df['Score'], bins=5, edgecolor='black', alpha=0.7)
plt.title('Histogram of Scores')
plt.xlabel('Score Range')
plt.ylabel('Frequency')
plt.show()

plt.figure(figsize=(6,4))
plt.scatter(df['Age'], df['Score'], color='magenta', marker='s')
plt.title('Age vs Score')
plt.xlabel('Age')
plt.ylabel('Score')
plt.grid(True)
plt.show()
