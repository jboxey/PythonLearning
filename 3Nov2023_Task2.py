# Create a Class Person , Two Objects by taking (name, age, address) Input from users and print details in the end.

class Person:
    name = None
    age = None
    address = None

    def details(self):
        print("The name of person is -->", self.name)
        print("The age of person is -->", self.age)
        print("The address of person is -->", self.address)

    def person_details(self, name, age, address):
        print(" The details of person are ", name, age, address)




person_1 = Person()
person_1.name = input("Enter your name")
person_1.age = input("Enter your age")
person_1.address = input("Enter your details")
person_1.details()


person_2 = Person()
person_2.person_details(name = input("Enter your name \n "), age = int(input("Enter your age \n")),
                        address=(input("Enter your address \n")))

