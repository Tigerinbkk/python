class Car:

    color = ""
    brand = ""
    number_of_wheels = 4
    number_of_seats = 4
    maxspeed = 0


def __init__(self, color, brand, number_of_wheels, number_of_seats, maxspeed):

    self.color = color
    self.brand = brand
    self.number_of_seats = number_of_seats
    self.number_of_wheels = number_of_wheels
    self.maxspeed = maxspeed


def setcolor(self, x):
    self.color = x


def setbrand(self, x):
    self.brand = x


def setmaxspeed(self, x):
    self.maxspeed = x


def printdata(self):
    print(" Color of this car is ", self.color)
    print(" brand of this car is ", self.brand)
    print(" maxspeed of this car is ", self.maxspeed)


def __del__(self):
    print()
