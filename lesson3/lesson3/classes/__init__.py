from lesson3.classes.models import SampleClass
import lesson3.classes.dto as dtos

def class_example1() -> None:
    c = SampleClass(age=20, name="Gicu")
    print(c.__dict__)


def class_example2() -> None:
    # c = dtos.Data()
    # c.some_method()
    # c.data_some_method()
    
    f = dtos.FuncData("ggg")
    print(f)

    
def class_example3() -> None:
    c = dtos.FuncData(name="Test")
    print(c)



def class_main() -> None:
    class_example1()