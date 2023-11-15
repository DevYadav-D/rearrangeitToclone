def smart_divide(func):
    def inner(a,b):
        print("dividing", a, "by", b)
        if b == 0:
            print("cannont divide by 0!")
            return
        return func(a,b)
    return inner

@smart_divide
def divide(a,b):
    return a/b

value1 = divide(15,3)
print(value1)

value2 = divide(5,0)
print(value2)