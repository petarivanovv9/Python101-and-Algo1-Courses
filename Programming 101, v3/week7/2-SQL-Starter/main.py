from create_company_database import CreateCompanyDatabase
from manage_company import ManageCompany
import sys


def main():
    db = CreateCompanyDatabase()
    # ManageCompany.make_initial_database(db)

    print (20 * '<->')
    print ("Commands:")
    print ("list")
    print ("add")
    print ("monthly")
    print ("yearly")
    print ("delete")
    print ("update")
    print ("exit")

    while True:
        user_command = input("command: ")

        if (user_command == "exit"):
            sys.exit()

        ManageCompany.command(db, user_command)


if __name__ == '__main__':
    main()
