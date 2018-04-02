# Define the Film class
class Film():

    # A required function to initialize the class object
    def __init__(self, name, length, release_year, language):
        self.name = name
        self.length = length
        self.release_year = release_year
        self.language = language

# An object belonging to the Film class
star_wars = Film("Star Wars", 121, 1977, "English")


# Define the Expert class
class Expert():
    
    # A required function to initialize the class object
    def __init__(self, name):
        self.name = name

    # A method that takes another object as its argument
    def boast(self, obj):

        # Print out Expert object's name
        print("Hi. My name is", self.name)
        
        # Print out the name of the Film class object
        print("I know a lot about", obj.name)
        print("It is", obj.length, "minutes long")
        print("It was released in", obj.release_year)
        print("It is in", obj.language)
