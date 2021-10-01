# 資料結構
# Array

class Array(object):

    def __init__(self, sizeOfArray, arrayType):
        self.sizeOfArray = sizeOfArray  # equal sizeOfArray
        self.sizeOfArray = len(list(map(arrayType, range(sizeOfArray))))  # equal sizeOfArray # Change range(sizeOfArray) into arrayType
        self.arrayItem = [arrayType(0)]* self.sizeOfArray

    def __str__(self):
        return   " ".join([str(i) for i in self.arrayItem])


        

a = Array(10, int)
print(a)
print(type(a))
    


        