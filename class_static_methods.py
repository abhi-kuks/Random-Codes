class Student:
    def __init__(self,name,school):
        self.name=name
        self.school=school
        self.marks=[]

    def average(self):
        return sum(self.marks) / len(self.marks)

abhi = Student('Abhishek','MIT')
abhi.marks.append(90)
abhi.marks.append(90)
abhi.marks.append(90)
abhi.marks.append(100)
print(abhi.marks)  #Instance Method

print(Student.average(abhi))

print(abhi.average())

class Foo:
    @classmethod
    def hi(self):
        print(self.__name__)

my_obj=Foo()
my_obj.hi()


class Bar:
    @staticmethod
    def hi():
        print("Hello , I don't take parameters")

an_obj=Bar()
an_obj.hi()

# --------------------------------------------------------------------------------------------------------------
# More Comprehensive understnding of @classmethods using the example given below!!!



class FixedFloat:

    def __init__(self, amount):
        self.amount = amount

    def __repr__(self):
        return f"<FixedFloat {self.amount:.2f}>"
    @classmethod
    def from_sum(cls, val1, val2):
        return cls(val1 + val2)


number = FixedFloat(18.54892)
new_no= FixedFloat.from_sum(183.4868542,785.546584)
# new_no=number.from_sum(183.4868542,785.546584)
print(new_no)
print(number)



class Euro(FixedFloat):
    def __init__(self, amount):
        super().__init__(amount)
        self.symbol = '€'

    def __repr__(self):
        return f"<Euro {self.symbol}{self.amount:.2f}>"


money= Euro(9245.746656)
print(money)
money_add= Euro.from_sum(152.165845,6465.165454)
print(money_add)


