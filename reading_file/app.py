employees_file = open("./reading_file/employees.txt", "r") # mode - r = read, w = writing, a = append, r+ = read and writing
print(employees_file.readable()) 
print(employees_file.readline())
print(employees_file.readline()) 
print(employees_file.readlines()[0]) 
#readable tells True or False
#readline is reading the first line.

for employee in employees_file.readlines():
    print(employee)



employees_file.close() # open comes with close


employees_file = open("./reading_file/employees.txt", "a")

#employees_file.write("Toby - Human Resources") #adding again if process again
employees_file.write("\nKelly - Customer Service")



employees_file.close() # open comes with close


employees_file = open("./reading_file/index.html", "w") # 2 is overwriting or you can create new file with new name file and type


employees_file.write("<p>This is HTML</p>")



employees_file.close() # open comes with close