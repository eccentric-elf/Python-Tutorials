import csv


sales_data = [
    ["month_number", "facecream", "facewash", "toothpaste", "bathingsoap", "shampoo", "moisturizer", "total_units", "total_profit"],
    [1, 2500, 1500, 5200, 9200, 1200, 1500, 20900, 211000],
    [2, 2630, 1200, 5100, 6100, 2100, 1200, 18330, 183400],
    [3, 2140, 1340, 4550, 9550, 1890, 1710, 21180, 201900],
    [4, 3400, 1130, 5870, 8870, 1770, 1900, 22940, 222700],
    [5, 3600, 1740, 4560, 7760, 1560, 1500, 20720, 209600],
    [6, 2760, 1550, 4890, 6100, 2340, 1760, 19400, 200500],
    [7, 2980, 1120, 5430, 7300, 1990, 1340, 20160, 210700],
    [8, 3700, 1320, 5320, 7300, 2160, 1850, 21650, 215000],
    [9, 3540, 1780, 6100, 8900, 1500, 2100, 23920, 231000],
    [10, 2650, 1450, 5200, 9550, 1340, 2100, 22290, 217600],
    [11, 2300, 1290, 4800, 7700, 2360, 1890, 20340, 199400],
    [12, 2400, 1310, 5300, 8650, 1560, 1800, 21200, 212500]
]


with open("sales.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(sales_data)

print("sales.csv file created.")

import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv("sales.csv")


plt.scatter(df["month_number"], df["toothpaste"], color='blue', marker='o', label="Toothpaste Sales")
plt.xlabel("Month Number")
plt.ylabel("Toothpaste Sales")
plt.title("Toothpaste Sales Data Per Month")
plt.xticks(df["month_number"])
plt.legend()
plt.grid(True)
plt.show()


plt.figure(figsize=(8, 5))
plt.bar(df["month_number"] - 0.2, df["facecream"], width=0.4, color='red', label="Face Cream Sales")
plt.bar(df["month_number"] + 0.2, df["facewash"], width=0.4, color='green', label="Face Wash Sales")
plt.xlabel("Month Number")
plt.ylabel("Sales Units")
plt.title("Face Cream & Face Wash Sales Data")
plt.xticks(df["month_number"])
plt.legend()
plt.show()


total_sales = df[["facecream", "facewash", "toothpaste", "bathingsoap", "shampoo", "moisturizer"]].sum()

plt.figure(figsize=(7, 7))
plt.pie(total_sales, labels=total_sales.index, autopct="%1.1f%%", colors=["red", "green", "blue", "purple", "orange", "yellow"])
plt.title("Total Sales Distribution for the Year")
plt.show()
