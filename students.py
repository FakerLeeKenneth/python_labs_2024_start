import json

# Step 2: Open and read the students.json file
with open('students.json', 'r') as file:
    data = json.load(file)

# Step 3: Parse the JSON data
students = data['students']

# Step 4: Iterate through the list of students and print their details
for student in students:
    print(f"ID: {student['id']}")
    print(f"Name: {student['name']}")
    print(f"Age: {student['age']}")
    print(f"Grades: {student['grades']}")
    print()  # Print a blank line for better readability
    
# print the second student's name
print("The second student's name is:", students[1]['name'])

# print the second student's age
print("The second student's age is:", students[1]['age'])