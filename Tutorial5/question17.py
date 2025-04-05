with open("student.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(students_data)

print("student.csv file has been created successfully!")

import pandas as pd
df = pd.read_csv("student.csv")
average_cgpa = df["CGPA"].mean()
print(f"\nAverage CGPA of all students: {average_cgpa:.2f}")

high_cgpa_students = df[df["CGPA"] > 9]
print("\nStudents with CGPA > 9:\n", high_cgpa_students)

high_cgpa_cse_students = df[(df["Branch"] == "CSE") & (df["CGPA"] > 9)]
print("\nCSE Students with CGPA > 9:\n", high_cgpa_cse_students)
max_cgpa_student = df[df["CGPA"] == df["CGPA"].max()]
print("\nStudent with Maximum CGPA:\n", max_cgpa_student)
avg_cgpa_per_branch = df.groupby("Branch")["CGPA"].mean()
print("\nAverage CGPA of each Branch:\n", avg_cgpa_per_branch)
