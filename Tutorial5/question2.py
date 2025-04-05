import pandas as pd
data = [
    {"Name": "Alice", "Age": 25},
    {"Name": "Bob", "Age": 30},
    {"Name": "Charlie", "Age": 35},
]
df = pd.DataFrame(data)
df.set_index("Name", inplace=True)
print(df)
