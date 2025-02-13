'''

For this assignment please do the following:

- Read in the student_grades.csv file

- calculate the average grade for the class

- for each student record calculate the difference between the student's grade and the average grade

- write the output to a new file called student_grade_differences.csv

'''

import pandas

input_file = "student_grades.csv"
data = pandas.read_csv(input_file)

averageGrade = data['grade'].mean()

data['grade_difference_from_avg'] = data['grade'] - averageGrade

outputFile = "student_grade_differences.csv"
data.to_csv(outputFile, index=False)

print(f"Succesfully wrote to {outputFile}")
