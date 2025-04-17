
def hello(a:int,b:int) -> int:
    return  a+b

def func(a: str):
    for c in a:
        yield c



def contect(a: str):
    for c in a:
        yield c


if __name__ == "__main__":
    g = func("asasasas")
    v = next(g)
    print(v)
    v = next(g)
    print(v)
    v = next(g)
    print(v)
    v = next(g)
    print(v)
