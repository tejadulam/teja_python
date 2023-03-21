# -Create an employee database with fields as emp_id, emp_name, emp_salary, emp_phone,(assign the id starting from 1001)
# ------ Question 5-----
datbase = []
n = int(input("enter no of records: "))
for id in range(1001,1001+n):
    name = input("enter name: ")
    salary = float(input("enter salary: "))
    phno = int(input("enter phno: "))
    record = (id,name,salary,phno)
    datbase.append(record)
    print()
print(datbase)