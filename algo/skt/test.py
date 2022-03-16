


class Foucal:
    firstname = 0
    second = 0
    print("class id first : ",id(firstname))
    def setdata(self, first, second):
        self.first = first
        self.second = second

a = Foucal()
a.setdata(1,2)
print(id(a.firstname))
b = Foucal()
print(id(b.firstname))
# b.setdata(3,4)
# print(a.first)
# print(id(a.first))
# b = Foucal()
# b.setdata(5,6)
# print(b.first)
# print(id(b.first))
