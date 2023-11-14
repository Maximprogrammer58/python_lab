import datetime

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def get_processed_df(path: str) -> pd.DataFrame:
   df = pd.read_csv("D:\Python_lab\python_lab\datasets\dataset.csv")
   df.columns = ["Date", "Celsius temperature", "Pressure", "Direction", "Speed"]
   if not((df.isnull().sum()).eq(0).all()):
      df.dropna(inplace=True, ignore_index=True)
   df['Fahrenheit temperature'] = 9/5 * df['Celsius temperature'] + 32
   return df  
   
def get_statistical_info(df: pd.DataFrame, parametr: str) -> pd.Series | None:
   if parametr in df.columns:
      return df[parametr].describe()
   
def celsius_temp_filtration(df: pd.DataFrame, celsius_temp: int) -> pd.DataFrame:
   return df[df["Celsius temperature"] >= celsius_temp]

def date_filtration(df: pd.DataFrame, start_date: datetime, end_date: datetime) -> pd.DataFrame:
   pass


if __name__ == "__main__":
   df = get_processed_df("D:\Python_lab\python_lab\datasets\dataset.csv")
   print(celsius_temp_filtration(df, 20).describe())