class  Matrix:

    def __init__(self, lists):
        self.lists = lists


    def __str__(self):
        return "\n".join(map(str,self.lists))

    def __add__(self, second_matr):
        result = []
        for i in range(len(self.lists)):
            result.append([])
            for j in range(len(self.lists[i])):
                result[i].append(self.lists[i][j]+second_matr.lists[i][j])
        return Matrix(result)

a = [[1,2,3],
     [4,5,6],
     [7,8,9]]
b = [[9,8,7],
     [6,5,4],
     [3,2,1]]
m1 = Matrix(a)
m2 = Matrix(b)
print(m1+m2)