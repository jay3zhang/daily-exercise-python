# -*- coding: utf-8 -*-
#变量和命名

#车辆数目
cars = 100
#一辆车的车内空间
space_in_a_car = 4
#司机人数
drivers = 30
#乘客人数
passengers = 90
#剩余的车/没被开的车
cars_not_driven = cars - drivers
#驾驶中的车
cars_driven = drivers
#车容量/可载总人数
carpool_capacity = cars_driven * space_in_a_car
#每辆车的平均乘客数
average_passengers_per_car = passengers / cars_driven
print "There are", cars, "cars available."
print "There are only", drivers, "drivers available."
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car, "in each car."
print "Hey %s there." % "you"

