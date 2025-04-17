def log_methods(cls):
    for name, value in vars(cls).items():
        if callable(value):
            setattr(cls, name, log_method(value))
    return cls


def log_method(func):
    def wrapper(*args, **kwargs):
        print(f"Calling method: {func.__name__}")
        return func(*args, **kwargs)
    return wrapper


# @log_methods
class MyClass:
    
    @log_method
    def my_method(self):
        print("Hello from my_method!")
        
        
def example():
    my_instance = MyClass()
    my_instance.my_method()