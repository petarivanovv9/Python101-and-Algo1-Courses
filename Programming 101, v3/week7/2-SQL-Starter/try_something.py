from create_company_database import CreateCompanyDatabase
from manage_company import ManageCompany


def main():
    # db = CreateCompanyDatabase()

    # bam = db.cursor.execute('''SELECT name FROM company WHERE id = 9''')
    # print (bam)
    # print (type(bam))
    # print (bam.fetchone()["name"])
    # print (bam.keys)
    # ManageCompany.make_initial_database(db)

    # ManageCompany.command(db, "list")
    # ManageCompany.command(db, "delete")


if __name__ == '__main__':
    main()
