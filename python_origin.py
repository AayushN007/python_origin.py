# Python Creator Tribute Program

class Python:

    def __init__(self):
        self.creator = "Guido van Rossum"
        self.name = "Python"
        self.reason = "Named after Monty Python comedy group"

    def show_details(self):
        print("Programming Language:", self.name)
        print("Created by:", self.creator)
        print("Name Inspiration:", self.reason)


python = Python()

python.show_details()

print("\nRespect to Guido van Rossum for creating Python")