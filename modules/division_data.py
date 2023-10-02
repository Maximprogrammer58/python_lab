import csv
import datetime
import os


def read_data() -> list:
   data = []
   with open('dataset.csv', "r", encoding="utf-8") as file:
      for line in csv.reader(file):
         data.append(line)
   return data


def division_date_and_data() -> None:
   data = read_data()
   path = os.getcwd()
   os.chdir(f"{path}\datasets\date_and_data")
   with open('X.csv', 'w', newline="") as file:
        writer = csv.writer(file)
        writer.writerows([map(int, i[0].split("-")) for i in data])
   with open('Y.csv', 'w', newline="") as file:
        writer = csv.writer(file)
        writer.writerows([i[1:] for i in data])
   os.chdir(path)
        
        
def division_by_year() -> None:
   data = read_data()
   path = os.getcwd()
   os.chdir(f"{path}\datasets\data_by_year")
   year_list = []
   for day in data:
      year_list.append(int(day[0].split("-")[0]))
   year_list = sorted(list(set(year_list)))
   a = 0
   b = 0
   for year in year_list:
      data_year = []
      for day in data:
         if year == int(day[0].split("-")[0]):
            data_year.append(day)
      a = "".join(data_year[0][0].split("-"))
      b = "".join(data_year[len(data_year) - 1][0].split("-"))
      with open(f"{a}_{b}.csv", 'w', encoding="utf-8", newline="") as file:
         writer = csv.writer(file)
         writer.writerows(data_year)
   os.chdir(path)     
       

def division_by_week() -> None:
   pass


def get_data(date: datetime) -> list | None:
   for i in read_data():
      if i[0] == str(date):
         return i[1:]