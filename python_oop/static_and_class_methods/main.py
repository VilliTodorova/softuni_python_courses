class MyClass:
    class_var = 0

    @classmethod
    def class_method(cls, arg):
        cls.class_var = arg


MyClass.class_method(10)