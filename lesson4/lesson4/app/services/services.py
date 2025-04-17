

def capital_case(x:str) -> str:
    return x.capitalize()


def divide(a: int, b: int) -> float:
    if b == 0:
        raise ZeroDivisionError("You can't divide by zero!")
    return a / b