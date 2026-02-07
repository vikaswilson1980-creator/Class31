from abc import ABC,abstractmethod
class Absclass(ABC):
    def print(self,x):
        print("past value : ",x)
    @abstractmethod 
    def task(self):
        print("We are inside Absclass")
class testclass(Absclass):
    def task(self):
        print("We are inside testclass")
objtest = testclass()
objtest.task()
objtest.print(100)

