import pandas as pd
data = {
    "Name": ["Alice", "Bob", "Charlie"],
    "Age": [25, 30, 35],
}
df = pd.DataFrame(data)
df.to_excel("output.xlsx", index=False)

print("Data written to output.xlsx")
