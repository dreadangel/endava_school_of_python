class Base:
    """Sample class."""

    def some_method(self) -> None:
        print(type(self))


class Functional:
    def some_func(self) -> None:
        print(type(self))


class Data(Base, Functional):
    def data_some_method(self) -> None:
        print(type(self))
        
    def _data_some_method(self) -> None:
        print(type(self))
    
    
class FuncData(Base):
    name: str = ""
    
    def __init__(self, name:str):
        self.name = name
        
    def data_some_method(self) -> None:
        print(type(self))
    
    def __str__(self):
        return f"{type(self)}:{self.name}"
