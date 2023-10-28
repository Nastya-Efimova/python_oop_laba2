
class Car:
    color = None  # цвет автомобиля
    fuel = None  # количество топлива
    capacity = None # вместимость
    endurance = None # прочность


    def go(self):
        # Команда ехать:
        pass

    def turn(self):
        # Команда поворачивать:
        pass

    def stop(self):
        # Команда остановиться:
        pass

    def info(self):
        # Команда вывода информации
        print("Машина_1 - Цвет: ", myCar.color,  "\nТопливо: ", myCar.fuel, "\nВместимость: ",myCar.capacity, "\nПрочность: ", myCar.endurance)
        print("\nМашина_2 - Цвет: ", myCar2.color,  "\nТопливо: ", myCar2.fuel, "\nВместимость: ",myCar2.capacity, "\nПрочность: ", myCar2.endurance)



myCar = Car()
myCar.color = 'red'  # красим в красный цвет
myCar.fuel = 50    # заливаем топливо
myCar.capacity = 5
myCar.endurance = 100

myCar2 = Car()
myCar2.color = 'blue'
myCar2.fuel = 55   # заливаем топливо
myCar2.capacity = 10
myCar2.endurance = 90

myCar.go()
myCar.turn()
myCar.stop()

myCar.info()

