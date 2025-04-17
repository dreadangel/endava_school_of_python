class Animal:
    def make_noise(self)->str:
        return "Animal noise!"


class Human:
    def make_noise(self)->str:
        return "Human noise!"
    
    
class Car:
    def make_noise(self)->str:
        return "Car noise!"
    

def noise(a:Animal)-> None:
    print(a.make_noise())


def example1() -> None:
    noise(Animal())
    noise(Human())
    noise(Car())
    

def example2() -> None:
    for c in [Animal(), Car(), Human()]:
        print(f"{type(c)}: {c.make_noise()}")