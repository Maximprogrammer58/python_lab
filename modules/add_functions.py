import os
import csv


def read_data(path: str) -> list:
    """Getting data from a file
    Args:
      path: the path to the file for reading information
    Returns:
      list of days with weather information
    """
    data = []
    with open(path, "r", encoding="utf-8") as file:
        for line in csv.reader(file):
            data.append(line)
    return data


def growth(next_day: int, today: int) -> int:
    """Parsing data from the site by url and further adding data to the list
    Args:
      year_from: year of the beginning of parsing
      year_to: year of parsing completion
      step: step for years
    Returns:
      List of days received as a result of parsing
    """
    if next_day < today:
        return (next_day + 31) - today
    return next_day - today


def change_work_dir(name: str):
    """Decorator for changing the working directory
    Args:
      name: name of working directory
    """
    def decorator(func):
        def wrapper():
            path = os.getcwd()
            os.chdir(f"{path}{name}")
            func()
            os.chdir(path)
        return wrapper
    return decorator