from CSV import Transactions
import input

def add():
   date_time = input.get_date_time("Enter date and time of transaction (dd/mm/yyy HH:MM): ")
   amount = input.get_amount()
   category = input.get_category()
   description = input.get_description()
   Transactions.record(date_time, amount, category, description)


Transactions.init_csv()
add()