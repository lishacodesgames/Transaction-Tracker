import pandas
import csv

CSV_FILE = "transactions.csv"
COLUMNS = ["date time", "amount", "category", "description"]

def init_csv() -> None:
   try:
      pandas.read_csv(CSV_FILE)
   except FileNotFoundError:
      # create csv file with columns, each column data is separated by commas 
      print("Creating transactions.csv...")
      dataframe = pandas.DataFrame(columns=COLUMNS)
      dataframe.to_csv(CSV_FILE, index=False) # index is basically row labels

def record(date_time, amount, category, description="") -> None:
   new_entry = {
      "date time": date_time,
      "amount": amount,
      "category": category,
      "description": description
   }

   # newline = '' makes sure newlines are interpreted as \n and not translated to \r\n on windows 
   with open(CSV_FILE, 'a', newline='') as file:
      writer = csv.DictWriter(file, fieldnames=COLUMNS)
      writer.writerow(new_entry)
   print("Transaction recorded successfully!")