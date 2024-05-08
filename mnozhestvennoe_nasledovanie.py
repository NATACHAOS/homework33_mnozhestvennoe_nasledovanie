class Vehicle:
    vehicle_type = "none"


class Car:
    price = 1000000

    def horse_powers(self):
        return [600]


class Nissan(Car, Vehicle):
    vehicle_type = "yes"
    price = 1200000

    def horse_powers(self):
        return [750]

    def __str__(self):
        print(self.vehicle_type, self.price)


my_nissan = Nissan()
print(my_nissan.horse_powers())
my_nissan.__str__()
