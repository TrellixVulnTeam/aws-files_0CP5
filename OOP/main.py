from car import Car

car_1 = Car("red",10,31)
car_2 = Car("blue",35,40)
print(car_1.color,car_1.acceleration,car_1.c_speed)
print(car_2.color,car_2.acceleration,car_2.c_speed)
car_1.deaccelerate()
print(car_1.color,car_1.acceleration,car_1.c_speed)
print(car_2.color,car_2.acceleration,car_2.c_speed)
#car_1.color="black"
#print(car_1.height)
#print(car_1.color)
#print(car_2.color)
