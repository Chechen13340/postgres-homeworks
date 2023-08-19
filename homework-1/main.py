"""Скрипт для заполнения данными таблиц в БД Postgres."""
import os

from function import get_data
import psycopg2
from settings import OPERATION_PATH_ORDERS, OPERATION_PATH_EMPLOYEES, OPERATION_PATH_CUSTOMERS

pass_sql = os.getenv('PASSWORD_SQL')
conn = psycopg2.connect(host='localhost', database='north', user='postgres', password=pass_sql)
try:
    with conn:
        with conn.cursor() as cur:
            for row in get_data(OPERATION_PATH_ORDERS):
                cur.execute(
                    "INSERT INTO orders VALUES (%s, %s, %s, %s, %s)",
                    (row['order_id'], row['customer_id'], row['employee_id'], row['order_date'], row['ship_city']))

            for row in get_data(OPERATION_PATH_EMPLOYEES):
                cur.execute(
                    "INSERT INTO employees VALUES (%s, %s, %s, %s, %s, %s)",
                    (row['employee_id'], row['first_name'], row['last_name'], row['title'], row['birth_date'],
                     row['notes']))

            for row in get_data(OPERATION_PATH_CUSTOMERS):
                cur.execute(
                    "INSERT INTO customers VALUES (%s, %s, %s)",
                    (row['customer_id'], row['company_name'], row['contact_name']))

finally:
    conn.close()
