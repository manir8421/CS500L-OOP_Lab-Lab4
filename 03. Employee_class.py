
# define class: Employee

class Employee:
    def __init__(self, name:str, id:int, department: str, age:int) -> None:
        self.__name = name
        self.__id = id
        self.__department = department
        self.__age = age

    # getter info: name
    @property
    def name(self) -> str:
        return self.__name
    
    # setter info: name
    @name.setter
    def name(self, name: str) -> None:
        self.__name = name   
        
    # getter info: id
    @property
    def id(self) -> int:
        return self.__id
    
    # setter info: id
    @id.setter
    def id(self, id: int) -> None:
        self.__id = id

    # getter info: department
    @property
    def department(self) -> str:
        return self.__department
    
    # setter info: department
    @department.setter
    def department(self, department: str) -> None:
        self.__department = department

    # getter info: age
    @property
    def age(self) -> int:
        return self.__age
    
    # setter info: age
    @age.setter
    def age(self, age: int) -> None:
        self.__age = age

    def __str__(self) -> str:
        return f"Employee's Name = {self.__name}, ID = {self.__id}, Department Number = {self.__department}, Age = {self.__age}"
    
    def __eq__(self, __value: object) -> bool:
        if isinstance(__value, Employee):
            return self.__name == __value.__name
        else:
            return False
        
    def __repr__(self) -> str:
        return '\n'+str(self)
    

# define class: Company

class Company:
    def __init__(self) -> None:
        self.__employees: list[Employee] = []

    # for add employee
    def add_employee(self, employee: Employee) -> None:
        self.__employees.append(employee)
    
    # for remove employee by ID
    def remove_employee(self, id: int) -> None:
        for del_emp in self.__employees:
            if del_emp.id == id:
                self.__employees.remove(del_emp)
                break
    
    # display all employee
    def display_all_employees(self) -> None:
        for all_emp in self.__employees:
            print(all_emp)

    # find employee by name
    def find_employee(self, name: str) -> list[Employee]:
        emps_found: list[Employee] = []
        for find_emp in self.__employees:
            if find_emp.name == name:
                emps_found.append(find_emp)
        return emps_found
    
    def display_employee(self, emps: list[Employee]) -> None:
        for emp in emps:
            print(emp)

    def __str__(self) -> str:
        return f"employees= {self.__employees}"
    
    def __eq__(self, __value: object) -> bool:
        if isinstance(__value, Company):
            return self.__employees == __value.__employees
        else:
            return False
        
    def __repr__(self) -> str:
        return str(self)
    
def main():

    comp = Company()        # create an instance of "Company" class to manage employee list
    
    print("\n========== Employee Management System ==========")
    
    # Main Menu option's start
    while True:             # create a infinite loop to display menu untill quit
        
        print("\nMenu: (choose anyone among e,a,d,r,q)\n")
        print("e - Enter a new employee's information")
        print("a - Display all employees information")
        print("d - Display an employee's information")
        print("r - Remove an employee's information")
        print("q - Quit")

        choice = input("\nEnter your choice: ")

        if choice == "e":
            name = input("Enter employee's name\t\t\t: ").upper()
            id = int(input("Enter employee's ID\t\t\t: "))
            department = input("Enter employee's department number\t: ").upper()
            age = int(input("Enter employee's age\t\t\t: "))
            new_empl = Employee(name, id, department, age)
            comp.add_employee(new_empl)
            print("Employee information added successfully.")

        elif choice == "a":
            print("\nAll Employees:")
            comp.display_all_employees()

        elif choice == "d":
            empl_name = input("Enter the employee's name to display: ").upper()
            empl = comp.find_employee(empl_name)
            if empl:
                print("\nEmployee Information:")
                comp.display_employee(empl)
            else:
                print("\nEmployee not found.")
                res = input("Do you want to add this employee?. (y/n): ")
                if res.lower() == 'y':
                    name = input("Enter employee's name\t\t\t: ").upper()
                    id = int(input("Enter employee's ID\t\t\t: "))
                    department = input("Enter employee's department number\t: ").upper()
                    age = int(input("Enter employee's age\t\t\t: "))
                    new_empl = Employee(name, id, department, age)
                    comp.add_employee(new_empl)
                    print("Employee information added successfully.")

        elif choice == "r":
            empid = int(input('Enter the employee id: '))
            comp.remove_employee(empid)
            print('The Employee removed!')

        elif choice == "q":
            print("\nQuit the program... Thanks")
            break

        else:
            print("Invalid choice! Please choose the right option and try again.")


if __name__ == "__main__":
    main()

    
    
    


        