# Define a class
class Dog():

    # Utilize the Python constructor to initialize the object
    def __init__(self, name, color):
        self.name = name
        self.color = color

# Create an instance of a class
dog = Dog('Fido', 'brown')

# Print the object's attributes
print(dog.name)
print(dog.color)
