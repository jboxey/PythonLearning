# Create a Car class and Create 2 Objects of the class with attributes 5 and 5 methods

class Car:
    # attributes

    name = None
    model = None
    tyre = None
    colour = None
    weight = None
    sunroof = None

    # Methods
    def speed(self):
        print("Weight")

    def color(self):
        print("colour of car is -->" + self.colour)

    def tyre_type(self):
        print("Smooth ")

    def comfort(self):
        print("The car is comfortable -->" + self.sunroof)

    def models(self):
        return print("The model is-->" + self.model)

toyota_object = Car()
toyota_object.name = "Toyota"
toyota_object.model = "Latest 1.0"
toyota_object.colour = "Blue"
toyota_object.sunroof = "Has sunroof"
toyota_object.color()
toyota_object.comfort()


tesla_object = Car()
tesla_object.name = "Tesla"
tesla_object.model = "Latest"
tesla_object.colour = "Black"
tesla_object.color()
tesla_object.models()

