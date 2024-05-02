def even_parameters(func):

    def wrapper(*args, **kwargs):
        for el in args:
            if isinstance(el, int):
                if el % 2 == 0:
                    continue
            return "Please use only even numbers!"
        else:
            return func(*args, **kwargs)

    return wrapper

@even_parameters
def add(a, b):
    return a + b

print(add(2, 4))
print(add("Peter", 1))
