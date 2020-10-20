# Exercise 1
# Writing a class that describes a bus
widow= Tk()


class Bus:


count = 0


def __init__(self, number_of_seats, color, driver_name):
self.number_of_seats = number_of_seats
self.color = color
self.driver_name = driver_name
self.update_count()

def change_of_color(self, color):
self.color = color

def update_count(self):
Bus.count = Bus.count + 1



bus1 = Bus(64,"Yellow", "akon")
bus2 = Bus(64, "Blue", "drake")
bus3 = Bus(56, "Green", "sun-el musician")
bus4 = Bus(78, "Red", "jody")

print("My name is", bus2.driver_name)
print("The color of my bus is", bus2.color)
print("It is a", bus2.number_of_seats,"seater")
print(Bus.count)
