import modules.add_functions as ef


index = -1


def next() -> tuple:
    """A function that returns data for the next date in order from the dataset.csv file at each subsequent call
    Returns:
    A tuple with information about this day
    """
    global index
    data = ef.read_data(r"D:\Python_lab\python_lab\datasets\dataset.csv")
    if index < len(data) - 1:
        index += 1
    return tuple(data[index])
