import pandas

input_file = "student_grades.csv"
data = pandas.read_csv(input_file)

averageGrade = data['grade'].mean()

data['grade_difference_from_avg'] = data['grade'] - averageGrade

outputFile = "student_grade_differences.csv"
data.to_csv(outputFile, index=False)

print(f"Succesfully wrote to {outputFile}")
