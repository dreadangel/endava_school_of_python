import lesson3.decorators.sample as sample
import lesson3.decorators.class_deco as class_deco
import lesson3.decorators.deco_class as deco_class


def example1() -> None:
    sample.multiply(1,2)


def example2() -> None:
    print(class_deco.multiply_together(1,2))


def example3() -> None:
    print(class_deco.sum_together(1,2))


def decorators_for_class():
    deco_class.example()