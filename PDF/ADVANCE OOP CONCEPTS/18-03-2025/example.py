import copy

class MyClass:
    count = 0
    def __init__(self, attr1, attr2):
        self.attr1 = attr1
        self.attr2 = attr2
        self.attributes = [attr1, attr2]
        self.__class__.count += 1
    def __del__(self):
        print(f"Deleting an object {self}")
        self.__class__.count -= 1

    @classmethod
    def create(cls, attr1, attr2):  # factory method
        return cls(attr1, attr2)  # this is an object of the class
    def __str__(self):
        return f'{self.attr1}{self.attr2}'
obj = MyClass(1, 3)
print(MyClass.count)
del obj
print(MyClass.count)
my_object = MyClass.create("v1 ", "v2")
print(my_object)

shallow_copy = copy.copy(my_object)
deep_copy = copy.deepcopy(my_object)

print(f"Shallow copy's list: {shallow_copy.attributes}. Original's list: {my_object.attributes}")
print(f"Deep copy's list: {deep_copy.attributes}. Original's list: {my_object.attributes}")

my_object.attributes[0] = "This will change in the shallow_copy but not the deep"
print(f"Shallow copy's list: {shallow_copy.attributes}. Original's list: {my_object.attributes}")
print(f"Deep copy's list: {deep_copy.attributes}. Original's list: {my_object.attributes}")

shallow_copy.attributes[1] = "This will change in the original but not the deep copy"
print(f"Shallow copy's list: {shallow_copy.attributes}. Original's list: {my_object.attributes}")
print(f"Deep copy's list: {deep_copy.attributes}. Original's list: {my_object.attributes}")

deep_copy.attributes = [1, 2, 3, "No change in either the shallow copy or original"]
print(f"Shallow copy's list: {shallow_copy.attributes}. Original's list: {my_object.attributes}")
print(f"Deep copy's list: {deep_copy.attributes}. Original's list: {my_object.attributes}")



original = [1, 2, 3, ["sub item 1", "sub item 2", "sub item 3"]]
shallow_copy = copy.copy(original)
deep_copy = copy.deepcopy(original)

print(f"Original: {original}, shallow: {shallow_copy}, deep: {deep_copy}")

shallow_copy[3][0] = "Nested item 1"
original[3][1] = "Nested item 2"
deep_copy[3][0] = "Deep copy's nested item 1"
deep_copy[3][1] = "Deep copy's nested item 2"

print(f"Original: {original}, shallow: {shallow_copy}, deep: {deep_copy}")