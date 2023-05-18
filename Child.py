class ParentClass:
    def __init__(self):
        self.parent_attribute = "Parent Attribute"

    def parent_method(self):
        print("This is a Parent Method")

class ChildClass(ParentClass):
    def __init__(self):
        super().__init__()  # Виклик конструктора батьківського класу
        self.child_attribute = "Child Attribute"

    def child_method(self):
        print("This is a Child Method")

    def exclusive_method(self):
        print("This is an Exclusive Method for Child Class")


# Створюємо об'єкт класу ChildClass
child_obj = ChildClass()

# Доступ до атрибутів та методів батьківського класу
print(child_obj.parent_attribute)  # Виведе: Parent Attribute
child_obj.parent_method()  # Виведе: This is a Parent Method

# Доступ до атрибутів та методів дочірнього класу
print(child_obj.child_attribute)  # Виведе: Child Attribute
child_obj.child_method()  # Виведе: This is a Child Method

# Виклик ексклюзивного методу дочірнього класу
child_obj.exclusive_method()  # Виведе: This is an Exclusive Method for Child Class
