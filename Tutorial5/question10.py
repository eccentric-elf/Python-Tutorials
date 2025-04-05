import csv

students = [
    ["Roll No", "Name", "Place", "Marks"],
    [1, "Alice", "New York", 85],
    [2, "Bob", "London", 90],
    [3, "Charlie", "Paris", 88],
    [4, "David", "Berlin", 92],
    [5, "Emma", "Tokyo", 87]
]

with open("stud.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(students)

print("stud.csv file created.")





import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats


df = pd.read_csv("stud.csv")


print("File contents:\n", df)

df.set_index("Roll No", inplace=True)
print("\nDataFrame with Roll No as index:\n", df)

print("\nDisplaying Name and Marks:\n", df[['Name', 'Marks']])

df_sorted_by_name = df.sort_values("Name")
print("\nSorted by Name:\n", df_sorted_by_name[["Name", "Marks"]])

df_sorted_by_marks = df.sort_values("Marks", ascending=False)
print("\nSorted by Marks (Descending):\n", df_sorted_by_marks[["Name", "Marks"]])


average_mark = df["Marks"].mean()
median_mark = df["Marks"].median()
mode_mark = stats.mode(df["Marks"]).mode[0]

print(f"\nAverage Marks: {average_mark}")
print(f"Median Marks: {median_mark}")
print(f"Mode Marks: {mode_mark}")


min_mark = df["Marks"].min()
max_mark = df["Marks"].max()

print(f"\nMinimum Marks: {min_mark}")
print(f"Maximum Marks: {max_mark}")


variance_marks = np.var(df["Marks"], ddof=1)
std_dev_marks = np.std(df["Marks"], ddof=1)

print(f"\nVariance of Marks: {variance_marks}")
print(f"Standard Deviation of Marks: {std_dev_marks}")


plt.hist(df["Marks"], bins=5, color="blue", edgecolor="black")
plt.xlabel("Marks")
plt.ylabel("Frequency")
plt.title("Histogram of Marks")
plt.show()


df.drop(columns=["Place"], inplace=True)
print("\nDataFrame after removing Place column:\n", df)
