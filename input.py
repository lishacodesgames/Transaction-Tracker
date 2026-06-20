from datetime import datetime

DATETIME_FORMAT = "%d/%m/%Y %H:%M"
CATEGORIES = { 'I': "Income", 'E': "Expense" }

def get_date_time(prompt, allow_today=True):
   """
   @param allow_today: Allows user to click enter and that will automatically get current time and date
   """
   date_time = input(prompt)
   if allow_today and not date_time:
      return datetime.today().strftime(DATETIME_FORMAT)
   
   try:
      valid_date_time = datetime.strptime(date_time, DATETIME_FORMAT)
      return valid_date_time.strftime(DATETIME_FORMAT)
   except ValueError:
      print("Invalid date format! (dd/mm/yyy HH:MM)")
      return get_date_time(prompt, allow_today)


def get_amount():
   try:
      amount = float(input("Enter transaction amount: "))
      if(amount <= 0):
         raise ValueError("Amount cannot be negative!")
      return amount
   except ValueError as e:
      print(e)
      return get_amount()

def get_category():
   category = input("Enter transaction category ('I' for Income, 'E' for Expense): ").upper()
   if category not in CATEGORIES:
      print("Invalid category! ('I' or 'E')")
      return get_category()
   else:
      return CATEGORIES[category]

def get_description():
   return input("Enter a description (optional): ")