n = int(input("Enter the number of employee"))
employee = {}
for i in range(n):
    name = input("Enter the name of employee")
    salary = input("Enter the salary of Employee")
    employee[name] = salary

print(employee)

while True:
    name = input("Enter the name of the employee whose salary need to be searched")
    salary = employee.get(name, -1)
    if salary == -1:
        print("Employee doesn't exist")
    else:
        print("The salary of the Employee {} is {}".format(name, salary))
    choice = input("if you want to Search more employee enter [Y|N]")
    if choice == 'N':
        break
