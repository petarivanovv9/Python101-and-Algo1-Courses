import sqlite3


class CreateCompanyDatabase:

    def __init__(self):
        create_table_query = '''CREATE TABLE IF NOT EXISTS company(id INTEGER PRIMARY KEY, name TEXT, monthly_salary INTEGER, yearly_bonus INTEGER, position TEXT)'''

        self.database = sqlite3.connect("company_database")
        self.database.row_factory = sqlite3.Row
        self.cursor = self.database.cursor()
        self.cursor.execute(create_table_query)

    def add_employee(self, name, monthly_salary, yearly_bonus, position):
        self.cursor.execute('''INSERT INTO company(name, monthly_salary, yearly_bonus, position)VALUES(?,?,?,?)''', (
            name, monthly_salary, yearly_bonus, position))
        self.database.commit()

    def list_employees(self):
        return self.cursor.execute("SELECT id, name, position FROM company")

    def monthly_spendings(self):
        spendings = self.cursor.execute("SELECT monthly_salary FROM company")

        return sum([item[0] for item in spendings])

    def yearly_spendings(self):
        total_amount = self.cursor.execute(
            "SELECT monthly_salary, yearly_bonus FROM company")

        return sum([item[0] + item[1] for item in total_amount])

    def delete_employee(self, id_employee):
        employee = self.cursor.execute(
            '''SELECT name FROM company WHERE id = ?''', (id_employee))
        self.cursor.execute(
            '''DELETE FROM company WHERE id = ?''', (id_employee))
        # print (employee["name"])
        # print (employee.fetchone()[0])
        # return employee["name"]
        # print (employee.fetchone()["name"])
        # return employee.fetchone()["name"]

    def update_employee(self, id_employee, name, monthly_salary, yearly_bonus, position):
        self.cursor.execute('''UPDATE company SET name = ?,
            monthly_salary = ?,
            yearly_bonus = ?,
            position = ?
            WHERE id = ?''', (name, monthly_salary, yearly_bonus, position, id_employee))
