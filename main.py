import datetime
import os 

import modules.parser_data as pd
import modules.division_data as dd
import modules.add_functions as ef
import modules.data_iterator as it
import modules.date_search as ds
import modules.function_next as fn


if __name__ == "__main__":
    dd.division_date_and_data()
    dd.division_by_year()
    dd.division_by_week()