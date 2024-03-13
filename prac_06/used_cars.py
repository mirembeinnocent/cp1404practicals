from prac_06.car import Car


def main():

    my_car = Car(180)
    my_car.drive(30)
    print(f"Car has fuel: {my_car.fuel}")
    print(my_car)

    limo = Car(100)
    limo.add_fuel(20)
    print(f"Fuel in the limo: {limo.fuel}")

    limo.drive(115)
    print(limo)


main()
