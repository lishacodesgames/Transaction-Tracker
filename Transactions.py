import pandas
import csv
from datetime import datetime

CSV_FILE = "transactions.csv"
COLUMNS = ["date time", "amount", "category", "description"]
DATETIME_FORMAT = "%d/%m/%Y %H:%M"

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

   print("\nTransaction recorded successfully!")

def show_in_range(start_datetime: str, end_datetime: str) -> pandas.DataFrame:
   print()
   start = datetime.strptime(start_datetime, DATETIME_FORMAT)
   end = datetime.strptime(end_datetime, DATETIME_FORMAT)

   dataframe = pandas.read_csv(CSV_FILE)

   # convert the "date time" column to datetime objects
   dataframe["date time"] = pandas.to_datetime(dataframe["date time"], format=DATETIME_FORMAT)

   # basically a filter
   mask = (dataframe["date time"] >= start) & (dataframe["date time"] <= end)
   filtered_data: pandas.DataFrame = dataframe.loc[mask]

   if filtered_data.empty:
      print(f"No transactions found in the given date range: ({start_datetime} to {end_datetime})")
   else:
      # sum of amount column of entries with Income category
      total_income = filtered_data[filtered_data["category"] == "Income"]["amount"].sum()

      # sum of amount column of entries with Expense category
      total_expense = filtered_data[filtered_data["category"] == "Expense"]["amount"].sum()

      print(f"------ TRANSACTIONS from {start_datetime} to {end_datetime} ------\n")
      print(filtered_data.to_string(
         index=False,
         formatters={ "date time": lambda x: x.strftime(DATETIME_FORMAT) } # format each entry in column with this lambda fxn
      ))

      print("\n----------------------- SUMMARY -----------------------")
      print(f"Total Income: ${total_income}")
      print(f"Total Expense: ${total_expense}")
      print(f"Net savings: ${total_income - total_expense}")

   return filtered_data