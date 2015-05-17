from bank_CI import BankCI
from bank_controller import BankController
from settings import DB_NAME, DB_SQL_STRUCTURE
from sql_manager import BankDatabaseManager


def main():
    manager = BankDatabaseManager.create_from_db_and_sql(DB_NAME, DB_SQL_STRUCTURE)
    controller = BankController(manager)
    command_interface = BankCI(controller)
    command_interface.main_menu()


if __name__ == '__main__':
    main()
