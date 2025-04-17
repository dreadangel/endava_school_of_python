import lesson3.classes as clss
import lesson3.prototypes as proto
import lesson3.decorators as deco

print("test")

def proto_example() -> None:
    proto.protos_main()


def cls_example() -> None:
    clss.class_main()


def deco_example() -> None:
    # deco.example1()
    # deco.example2()
    # deco.example3()
    deco.decorators_for_class()
    
if __name__ == "__main__":
    # proto_example()
    # cls_example()
    deco_example()