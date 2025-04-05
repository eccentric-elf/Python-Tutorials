import pandas as pd
df = pd.read_csv("auto.csv")
df.dropna(inplace=True)  
df.to_csv("cleaned_auto.csv", index=False) 
print("CSV file cleaned and updated.")
most_expensive = df[df["price"] == df["price"].max()]
print("Most Expensive Car Company:", most_expensive["company"].values[0])
toyota_cars = df[df["company"].str.lower() == "toyota"]
print("Toyota Car Details:\n", toyota_cars)
print("Total cars by company:\n", df["company"].value_counts())
highest_price_cars = df.loc[df.groupby("company")["price"].idxmax()]
print("Highest Priced Cars of Each Company:\n", highest_price_cars)
average_mileage = df.groupby("company")["average-mileage"].mean()
print("Average Mileage by Company:\n", average_mileage)
df_sorted = df.sort_values(by="price", ascending=False)
print("Cars Sorted by Price:\n", df_sorted)
