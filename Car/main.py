from OOP.Car.get_car_info import get_car_info

lexus = get_car_info('570','2200 kg', '190hp', '410nm', '240km/h', 'black')
print(lexus.car_info())
print(lexus.start_engine())
print(lexus.stop_engine())