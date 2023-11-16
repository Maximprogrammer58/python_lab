import modules.analytics as analytics


if __name__ == "__main__":
   df = analytics.get_processed_df("D:\Python_lab\python_lab\datasets\dataset.csv")
   print(analytics.date_filtration(df, "2018-11-10", "2022-12-10"))
   print(analytics.group_by_month_with_average_temp(df, "Fahrenheit temperature"))
   analytics.show_temp_graph(df, "Celsius temperature")
   analytics.show_temp_graph_median_average(df, 10, 2013)