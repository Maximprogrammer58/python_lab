# -*- coding: utf-8 -*-

import os
import csv


def read_data() -> list:
   data = []
   with open('dataset.csv', "r") as file:
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
   pass 


def division_by_week() -> None:
   pass


def get_data() -> list | None:
   pass