class Car:

    def __init__(self, horse_power, make, model):
        self.horse_power = horse_power
        self.make = make
        self.model = model

    def __str__(self):
        return self.make

    def __repr__(self):
        return str(self)


def hp(car):
    return car.horse_power


def make(car):
    return car.make


def model(car):
    return car.model


def sort_by_hp(cars_list):
    y = sorted(cars_list, key=hp)
    return y


def sort_by_make(cars_list):
    x = sorted(cars_list, key=make)
    return x


def sort_desc_by_model(cars_list):
    z = sorted(cars_list, key=model)
    return z


Mustang = Car(300, "Ford", "Mustang")
Camaro = Car(320, "Chevy", "Camaro")
Civic = Car(80, "Honda", "Civic")
Corolla = Car(120, "Toyota", "Corolla")

cars = [Mustang, Camaro, Civic, Corolla]
x = sort_by_make(cars)
y = sort_by_hp(cars)
z = sort_desc_by_model(cars)
print(cars)
print(x)
print(y)
print(z)
# for car in cars:
#     print(car)
# print("\n")

# cars.sort(key=sort_by_make)
# for car in cars:
#     print(car)
# print("\n")
#
# cars.sort(key=sort_desc_by_model)
# for car in cars:
#     print(car)
# print("\n")

# new_list1 = sorted(cars, key=lambda x: x.horse_power, reverse=True)
# print(new_list1)
