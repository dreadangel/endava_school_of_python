from typing import Protocol


class NoiseObject(Protocol):
    def make_noise(self)->str:
        pass


class AnimalNoise(Protocol):
    def make_noise(self)->str:
        pass
    

class Animal:
    def make_noise(self)->str:
        return "Animal noise!"


class Human:
    def make_noise(self)->str:
        return "Human noise!"

    
class Car:
    def make_noise(self)->str:
        return "Car noise!"



def noise(a:NoiseObject)-> str:
    return a.make_noise()


def example1() -> None:
    print(noise(Animal()))
    print(noise(Human()))
    print(noise(Car()))
