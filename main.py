import modules.analytics as analytics


if __name__ == "__main__":
   df = analytics.get_processed_df("D:\Python_lab\python_lab\datasets\dataset.csv")
   print(df)