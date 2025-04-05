import pandas as pd
df = pd.read_csv("employee.csv")
print("\nFirst 7 Records:\n", df.head(7))
print("\nEmployee Names in Alphabetical Order:\n", df["name"].sort_values().tolist())
highest_salary_employee = df[df["salary"] == df["salary"].max()]
print("\nEmployee with Highest Salary:\n", highest_salary_employee["name"].values[0])
male_employees = df[df["gender"] == "Male"]["name"].tolist()
print("\nMale Employees:\n", male_employees)
unique_teams = df["team"].unique()
print("\nTeams Employees Belong To:\n", unique_teams)
