import modules.add_functions as ef


class DataIterator:
   def __init__(self):
      self.data = ef.read_data(r"D:\Python_lab\python_lab\datasets\dataset.csv")
      self.index = -1
          
   def __iter__(self):
      return self
   
   def __next__(self) -> tuple:
      if self.index < len(self.data) - 1:
         self.index += 1
         return tuple(self.data[self.index])
      else:
         raise StopIteration