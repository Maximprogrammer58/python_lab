import datetime
import os
import modules.add_functions as ef


def search(date: datetime) -> list | None:
    """Getting information about the day by date from the main dataset
    Args:
      date: date of the required day
    Returns:
      information about the day or, if there is no such for, the function does not return none
    """
    for day in ef.read_data("datasets/dataset.csv"):
        if day[0] == str(date):
            return day[1:]
         

def search_by_year(date: datetime) -> list | None:
    """Getting information about the day by date from the main file by year
    Args:
      date: date of the required day
    Returns:
      information about the day or, if there is no such for, the function does not return none
    """
    directory = "datasets/data_by_year"
    for filename in os.listdir(directory):
        if (int(filename[0:4]) == date.year):
            data = ef.read_data(f"{directory}/{filename}")
            for day in data:
                if day[0] == str(date):
                    return day[1:]


def search_by_week(date: datetime) -> list | None:
    """Getting information about the day by date from the main file by week
    Args:
      date: date of the required day
    Returns:
      information about the day or, if there is no such for, the function does not return none
    """
    directory = "datasets/data_by_week"
    for filename in os.listdir(directory):
        left_date = datetime.datetime.strptime(filename[:8], '%Y%m%d').date()
        right_date = datetime.datetime.strptime(filename[9:17], '%Y%m%d').date()
        if (left_date <= date <= right_date):
            data = ef.read_data(f"{directory}/{filename}")
            for day in data:
                if day[0] == str(date):
                    return day[1:]


def search_by_date(date: datetime) -> list | None:
    """Getting information about the day by date from the main files by date and data
    Args:
      date: date of the required day
    Returns:
      information about the day or, if there is no such for, the function does not return none
    """
    data_from_x = ef.read_data(f"datasets/date_and_data/X.csv")
    for row, value in enumerate(data_from_x):
        time = "-".join(value) 
        if time == str(date):
            data_from_y = ef.read_data(f"datasets/date_and_data/Y.csv")
            return data_from_y[row]