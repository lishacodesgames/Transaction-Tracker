import pandas
import csv
from datetime import datetime

# files in python act like namespaces.
# The syntax in main would be the same if I made a class 'CSV' of classmethods
# or imported CSV.py that contained free functions
# I'm using class for learning purposes

class Transactions:
   FILE = "transactions.csv" # static class variable
   COLUMNS = ["date", "amount", "category", "description"]
   DATETIME_FORMAT = "%d/%m/%Y %H:%M"

   @classmethod # basically like static
   def init_csv(cls): # cls = the class itself
      try:
         pandas.read_csv(cls.FILE)
      except FileNotFoundError:
         # create csv file with columns, each column data is separated by commas 
         print("Creating transactions.csv...")
         dataframe = pandas.DataFrame(columns=cls.COLUMNS)
         dataframe.to_csv(cls.FILE, index=False) # index is basically row labels

   @classmethod
   def record(cls, date, amount, category, description=""):
      new_entry = {
         "date": date,
         "amount": amount,
         "category": category,
         "description": description
      }

      # newline = '' makes sure newlines are interpreted as \n and not translated to \r\n on windows 
      with open(cls.FILE, 'a', newline='') as file:
         writer = csv.DictWriter(file, fieldnames=cls.COLUMNS)
         writer.writerow(new_entry)
      print("Transaction recorded successfully!")