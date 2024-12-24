import mysql.connector
from tkinter import *
from tkinter import messagebox

# Database connection
con = mysql.connector.connect(
    host="localhost",
    user="root",
    password="@diksha#76680",
    database="employee_payroll",
    auth_plugin="mysql_native_password"
)

cursor = con.cursor()

# Function to check if an employee exists
def check_employee(employee_id):
    sql = 'SELECT * FROM employees WHERE id=%s'
    cursor.execute(sql, (employee_id,))
    result = cursor.fetchall()  # Ensure the result is fetched
    if result:
        return True
    else:
        return False

# Add Employee
def add_employee():
    try:
        Id = int(id_entry.get())
        Name = name_entry.get()
        Post = position_entry.get()
        Salary = float(salary_entry.get())
        Bonus = float(bonus_entry.get())
        Deduction = float(deduction_entry.get())
        NetSalary = Salary + Bonus - Deduction
        
        if check_employee(Id):
            messagebox.showwarning("Duplicate Employee", "Employee already exists.")
            return

        sql = 'INSERT INTO employees (id, name, position, salary, bonus, deduction, net_salary) VALUES (%s, %s, %s, %s, %s, %s, %s)'
        data = (Id, Name, Post, Salary, Bonus, Deduction, NetSalary)
        cursor.execute(sql, data)
        con.commit()
        messagebox.showinfo("Success", "Employee added successfully.")
        clear_entries()

    except Exception as e:
        messagebox.showerror("Error", str(e))

# Update Employee
def update_employee():
    try:
        Id = int(id_entry.get())
        Name = name_entry.get()
        Post = position_entry.get()
        Salary = float(salary_entry.get())
        Bonus = float(bonus_entry.get())
        Deduction = float(deduction_entry.get())
        NetSalary = Salary + Bonus - Deduction
        
        if not check_employee(Id):
            messagebox.showwarning("Not Found", "Employee not found.")
            return

        sql = 'UPDATE employees SET name=%s, position=%s, salary=%s, bonus=%s, deduction=%s, net_salary=%s WHERE id=%s'
        data = (Name, Post, Salary, Bonus, Deduction, NetSalary, Id)
        cursor.execute(sql, data)
        con.commit()
        messagebox.showinfo("Success", "Employee updated successfully.")
        clear_entries()

    except Exception as e:
        messagebox.showerror("Error", str(e))

# Delete Employee
def delete_employee():
    try:
        Id = int(id_entry.get())
        if not check_employee(Id):
            messagebox.showwarning("Not Found", "Employee not found.")
            return

        sql = 'DELETE FROM employees WHERE id=%s'
        cursor.execute(sql, (Id,))
        con.commit()
        messagebox.showinfo("Success", "Employee deleted successfully.")
        clear_entries()

    except Exception as e:
        messagebox.showerror("Error", str(e))

# View Employee
def view_employee():
    try:
        Id = int(id_entry.get())
        sql = 'SELECT * FROM employees WHERE id=%s'
        cursor.execute(sql, (Id,))
        result = cursor.fetchall()

        if result:
            employee = result[0]
            name_var.set(employee[1])
            position_var.set(employee[2])
            salary_var.set(employee[3])
            bonus_var.set(employee[4])
            deduction_var.set(employee[5])
            net_salary_var.set(employee[6])
        else:
            messagebox.showwarning("Not Found", "Employee not found.")

    except Exception as e:
        messagebox.showerror("Error", str(e))

# Clear Entry Fields
def clear_entries():
    id_entry.delete(0, END)
    name_entry.delete(0, END)
    position_entry.delete(0, END)
    salary_entry.delete(0, END)
    bonus_entry.delete(0, END)
    deduction_entry.delete(0, END)
    net_salary_entry.delete(0, END)

# Tkinter GUI Setup
root = Tk()
root.title("Employee Payroll Management System")
root.geometry("500x600")

# Labels and Entries
Label(root, text="Employee ID").grid(row=0, column=0, padx=10, pady=10)
id_entry = Entry(root)
id_entry.grid(row=0, column=1)

Label(root, text="Employee Name").grid(row=1, column=0, padx=10, pady=10)
name_entry = Entry(root)
name_entry.grid(row=1, column=1)

Label(root, text="Position").grid(row=2, column=0, padx=10, pady=10)
position_entry = Entry(root)
position_entry.grid(row=2, column=1)

Label(root, text="Salary").grid(row=3, column=0, padx=10, pady=10)
salary_entry = Entry(root)
salary_entry.grid(row=3, column=1)

Label(root, text="Bonus").grid(row=4, column=0, padx=10, pady=10)
bonus_entry = Entry(root)
bonus_entry.grid(row=4, column=1)

Label(root, text="Deduction").grid(row=5, column=0, padx=10, pady=10)
deduction_entry = Entry(root)
deduction_entry.grid(row=5, column=1)

Label(root, text="Net Salary").grid(row=6, column=0, padx=10, pady=10)
net_salary_entry = Entry(root, state="readonly")
net_salary_entry.grid(row=6, column=1)

# Buttons
Button(root, text="Add Employee", bg="yellow",  command=add_employee).grid(row=7, column=0, padx=10, pady=10)
Button(root, text="Update Employee", bg="lightblue",command=update_employee).grid(row=7, column=1, padx=10, pady=10)
Button(root, text="Delete Employee", bg="green",command=delete_employee).grid(row=8, column=0, padx=10, pady=10)
Button(root, text="View Employee", bg="red",command=view_employee).grid(row=8, column=1, padx=10, pady=10)

# Variables to display employee info
name_var = StringVar()
position_var = StringVar()
salary_var = DoubleVar()
bonus_var = DoubleVar()
deduction_var = DoubleVar()
net_salary_var = DoubleVar()

# Display Employee Information (for view)
Label(root, text="Name").grid(row=9, column=0, padx=10, pady=10)
Label(root, textvariable=name_var).grid(row=9, column=1)

Label(root, text="Position").grid(row=10, column=0, padx=10, pady=10)
Label(root, textvariable=position_var).grid(row=10, column=1)

Label(root, text="Salary").grid(row=11, column=0, padx=10, pady=10)
Label(root, textvariable=salary_var).grid(row=11, column=1)

Label(root, text="Bonus").grid(row=12, column=0, padx=10, pady=10)
Label(root, textvariable=bonus_var).grid(row=12, column=1)

Label(root, text="Deduction").grid(row=13, column=0, padx=10, pady=10)
Label(root, textvariable=deduction_var).grid(row=13, column=1)

Label(root, text="Net Salary").grid(row=14, column=0, padx=10, pady=10)
Label(root, textvariable=net_salary_var).grid(row=14, column=1)

root.mainloop()

# Close cursor and connection when the program ends
cursor.close()
con.close()