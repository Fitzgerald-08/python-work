class Person:
    """Model information about a person"""

    def __init__(self, name, age, gender):
        """Define basic information"""
        self.name = name
        self.age = age
        self.gender = gender

    def display_info(self):
        """Display information about a person"""
        print(f"Name: {self.name.title()}\n"
              f"Age: {self.age}\n"
              f"Gender: {self.gender.title()}")

    def is_adult(self):
        """Print a message showing whether the person is an adult or not"""
        if self.age > 17:
            return f"{self.name.title()} is indeed an adult"
        else:
            return f"{self.name.title()} is not an adult"


person = Person("alex", 22, "male")
person.display_info()
print(person.is_adult())
