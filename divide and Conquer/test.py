class EnforceMethods(type):
    def __new__(cls, name, bases, dct):
        if "required_method" not in dct:
            raise TypeError(f"Class {name} must implement required_method'")
        return super().__new__(cls, name, bases, dct)

class MyClass(metaclass=EnforceMethods):
    pass
