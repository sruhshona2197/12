

# 11. Property Decorator
class Temperature:
    def __init__(self, c):
        self._c = c

    @property
    def celsius(self):
        return self._c

t = Temperature(36)
print(t.celsius)


# 12. Operator Overloading
class Number:
    def __init__(self, x):
        self.x = x

    def __add__(self, other):
        return self.x + other.x

n1 = Number(10)
n2 = Number(20)
print(n1 + n2)


# 13. Private Method
class Secret:
    def __hidden(self):
        return "Hidden"

    def show(self):
        return self.__hidden()

s = Secret()
print(s.show())


# 14. Composition
class Engine:
    def start(self):
        return "Engine started"

class Car:
    def __init__(self):
        self.engine = Engine()

c = Car()
print(c.engine.start())


# 15. Aggregation
class Teacher:
    def __init__(self, name):
        self.name = name

class School:
    def __init__(self, teacher):
        self.teacher = teacher

t = Teacher("Ali")
s = School(t)
print(s.teacher.name)
