from datetime import datetime

DATETIME_FORMAT = "%d/%m/%Y %H:%M"
CATEGORIES = {
   'I': "Income",
   'E': "Expense"
}

def format_categories() -> str: # in case more are added later, I will only have to change this
   return " or ".join([f"'{key}' for {value}" for key, value in CATEGORIES.items()])

def get_date_time(prompt, allow_today=True) -> str:
   """
   @param allow_today: Allows user to click enter and that will automatically get current time and date
   """

   print()
   date_time = input(prompt)
   if allow_today and not date_time:
      return datetime.today().strftime(DATETIME_FORMAT) # strftime converts datetime to string

   try:
      valid_date_time = datetime.strptime(date_time, DATETIME_FORMAT) # strptime converts string to datetime
      return valid_date_time.strftime(DATETIME_FORMAT)
   except ValueError:
      print("\nInvalid date format! (dd/mm/yyy HH:MM)")
      return get_date_time(prompt, allow_today) # recursive calling until user enters valid input


def get_amount() -> int:
   try:
      amount = int(input("Enter transaction amount: "))
      if(amount <= 0):
         print()
         raise ValueError("Amount cannot be negative!")
      return amount
   except ValueError as e:
      print(e)
      return get_amount()

def get_category() -> str:
   category = input(f"Enter transaction category ({format_categories()}): ").upper()
   if category not in CATEGORIES:
      print("\nInvalid category!")
      return get_category()
   else:
      return CATEGORIES[category]

def get_description() -> str:
   return input("Enter a description (optional): ")