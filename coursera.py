# -*- coding: utf-8 -*-
"""
Created on Sat May 16 20:11:40 2020

@author: PC
"""



def f(x):
    function=-5*x**5+67*x**2-47
    return function

print(f(0))
print(f(1))
print(f(2))
print(f(3))
    
def project_to_distance(point_x, point_y, distance):
    dist_to_origin = (point_x ** 2 + point_y ** 2) ** 0.5
    scale = distance / dist_to_origin
    print (point_x * scale, point_y * scale)

project_to_distance(2, 7, 4)


def do_stuff():
    """
    Example of print vs. return
    """
    print("Hello world")
    return "Is it over yet?"
    print("Goodbye cruel world!")

print(do_stuff())

def future_value(present_value, annual_rate, periods_per_year, years):
    """
    Input: the numbers present_value, annual_rate, periods_per_year, years
    Output: future value based on formula given in question
    """
    rate_per_period = annual_rate / periods_per_year
    periods = periods_per_year * years

    FV=present_value*(1+rate_per_period)*periods
    return(future_value)
    

print(future_value(500, 0.4, 10, 10))


def future_value(present_value, annual_rate, periods_per_year, years):
    """
    Input: the numbers present_value, annual_rate, periods_per_year, years
    Output: future value based on formula given in question
    """
    rate_per_period = annual_rate / periods_per_year
    periods = periods_per_year * years

    FV=present_value*((1+rate_per_period)**periods)
    
    return(FV)
    

print(future_value(1000, .02, 365, 4))





def area(a):
    area_triangle=a**2*(3**0.5)/4
    return(area_triangle)
    
print(area(5))
