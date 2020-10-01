"""
create a list to store 5 numbers (float)
capture user input 5 times for their grades
each time we capture new input we append the number to the list
sort the list ascending, then splice the item starting at index 2
once we have the 3 highest number in the list, we sum them up and divide by 3
outut a message to the user
end
"""
"""
create list

 5x (capture input
    append number to list)

print to user
"""
grades = []

grade = input("enter the 1st grade: ")
grades.append(float(grade))

grade = input("enter the 2nd grade: ")
grades.append(float(grade))

grade = input("enter the 3rd grade: ")
grades.append(float(grade))

grade = input("enter the 4th grade: ")
grades.append(float(grade))

grade = input("enter the 5th grade: ")
grades.append(float(grade))

grades.sort()
grades = grades[2:]
grades = sum(grades)
result = grades / 3

print("Average Grade {0:.2f}%".format(result))
