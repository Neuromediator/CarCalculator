import calculator


if __name__ == '__main__':
    calc = calculator.Calculator(years=10)
    calc.add_car(
        calculator.Car("Toyota Corolla", 120000, 7,
                       1200, 2500)
    )

    calc.add_car(
        calculator.Car("Range Rover", 650000, 3,
                       3000, 7000)
    )calc.add_car(
        calculator.Car("Audi", 500000, 3,
                       3000, 7000)
    )

    calc.print_cars()