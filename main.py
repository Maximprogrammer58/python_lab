import modules.parser_data as pd
import modules.division_data as dd
import datetime


if __name__ == "__main__":
    dd.division_by_year()
    dd.division_date_and_data()
    print(dd.get_data(datetime.date(2022, 10, 3)))
   
