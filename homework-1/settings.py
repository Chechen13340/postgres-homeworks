from pathlib import Path

ROOT_PATH = Path(__file__).parent
OPERATION_PATH_CUSTOMERS = Path.joinpath(ROOT_PATH, 'north_data', 'customers_data.csv')
OPERATION_PATH_EMPLOYEES = Path.joinpath(ROOT_PATH, 'north_data', 'employees_data.csv')
OPERATION_PATH_ORDERS = Path.joinpath(ROOT_PATH, 'north_data', 'orders_data.csv')

