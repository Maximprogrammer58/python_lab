import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def get_processed_df(path: str) -> pd.DataFrame:
    """Reading and processing according to the variant of data from the dataset
    Args:
      path: the path to the file for reading information
    Returns:
      Dataframe without Nan values and with the addition of the Fahrenheit temperature column
    """
    df = pd.read_csv(path)
    df.columns = ["Date", "Celsius temperature",
                  "Pressure", "Direction", "Speed"]
    df['Date'] = pd.to_datetime(df['Date'], format='%Y-%m-%d')
    if not ((df.isnull().sum()).eq(0).all()):
        df.dropna(inplace=True, ignore_index=True)
    df['Fahrenheit temperature'] = 9/5 * df['Celsius temperature'] + 32
    return df


def get_statistical_info(df: pd.DataFrame, parametr: str) -> pd.Series | None:
    """Getting statistical information
    Args:
      df: Dataframe with original values
      parametr: the name of the column of the dataframe for which the statistical description is located
    Returns:
      A series containing a statistical description
    """
    if parametr in df.columns:
        return df[parametr].describe()


def celsius_temp_filtration(df: pd.DataFrame, celsius_temp: int) -> pd.DataFrame:
    """Filtering by column temperature in degrees Celsius
    Args:
      df: Dataframe with original values
      celsius_temp: temperature in degrees Celsius
    Returns:
      Dataframe with days in which the temperature is not less than the set temperature
    """
    return df[df["Celsius temperature"] >= celsius_temp]


def date_filtration(df: pd.DataFrame, start_date: str, end_date: str) -> pd.DataFrame:
    """Filtering by date
    Args:
      df: Dataframe with original values
      start_date: Starting date
      end_date: End date
    Returns:
      Dataframe with days that range [start_date; end_date]
    """
    start_date = pd.to_datetime(start_date, format='%Y-%m-%d')
    end_date = pd.to_datetime(end_date, format='%Y-%m-%d')
    return df[(start_date <= df["Date"]) & (df["Date"] <= end_date)]


def group_by_month_with_average_temp(df: pd.DataFrame, parametr: str) -> pd.Series | None:
    """Grouping by month with calculation of the average temperature value
    Args:
      df: Dataframe with original values
      parametr: A column indicating which temperature is taken
    Returns:
      A series indicating the average value for all months
    """
    if parametr in ["Celsius temperature", 'Fahrenheit temperature']:
        return df.groupby(df.Date.dt.month)[parametr].mean()


def show_temp_graph(df: pd.DataFrame, parametr: str) -> None:
    """Show of the temperature graph for the entire period
    Args:
      df: Dataframe with original values
      parametr: A column indicating which temperature is taken
    """
    if parametr in ["Celsius temperature", 'Fahrenheit temperature']:
        fig = plt.figure(figsize=(30, 5))
        plt.ylabel(parametr)
        plt.xlabel("date")
        plt.title('Изменение температуры')
        plt.plot(df["Date"], df[parametr], color='green', linestyle='-', linewidth=2)
        plt.show()


def show_temp_graph_median_average(df: pd.DataFrame, month: int, year: int) -> None:
    """Showing the temperature graph for the specified month in
    the year and displaying the median and average values
    Args:
      df: Dataframe with original values
      month: The month for which the temperature graph is drawn
      year: The year for which the temperature graph is drawn
    """
    month_df = df[(df.Date.dt.month == month) & (df.Date.dt.year == year)]
    fig = plt.figure(figsize=(30, 5))

    fig.add_subplot(1, 3, 1)
    plt.ylabel("celsius temperature")
    plt.xlabel("date")
    plt.plot(month_df.Date.dt.day, month_df["Celsius temperature"],
             color='green', linestyle='-', linewidth=2, label='Celsius temperature')
    plt.axhline(y=month_df["Celsius temperature"].mean(), color='yellow', label="Average value")
    plt.axhline(y=month_df["Celsius temperature"].median(), color='blue', label="Median")
    plt.legend(loc=2, prop={'size': 10})

    fig.add_subplot(1, 3, 2)
    plt.ylabel("Fahrenheit temperature")
    plt.xlabel("date")
    plt.plot(month_df.Date.dt.day, month_df["Fahrenheit temperature"],
             color='red', linestyle='--', linewidth=2, label='Fahrenheit temperature')
    plt.axhline(y=month_df["Fahrenheit temperature"].mean(), color='yellow', label="Average value")
    plt.axhline(y=month_df["Fahrenheit temperature"].median(), color='blue', label="Median")
    plt.legend(loc=2, prop={'size': 10})

    plt.show()