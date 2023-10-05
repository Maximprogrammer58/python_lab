import modules.add_functions as ef


index = -1
def next():
    global index
    data = ef.read_data(r"D:\Python_lab\python_lab\datasets\dataset.csv")
    if index < len(data) - 1:
        index += 1
        return tuple(data[index])