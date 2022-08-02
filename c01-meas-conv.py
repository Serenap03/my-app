

print('Below are various mathematical programs for challenge problem 1.')

# Test imput using 212 degrees Fahrenheit

def to_celsius(F):
    return((F-32) * 5/9)
def main():
    print(to_celsius(212))
main()

#Test input using 100 degress Celsius
def to_fahrenheit(C):
    return ((C * 9/5)+32)
def main():
    print(to_fahrenheit(100))
main()


import math
# Test imput using values x^2-7x+10=0
def plus_quadratic(a,b,c):
    return (-b + (b ** 2 - 4 * a * c) ** 0.5) / (2 * a)

def main():
    print(plus_quadratic(1,-7,10))

main()

def minus_quadratic(a,b,c):
    return (-b - (b ** 2 - 4 * a * c) ** 0.5) / (2 * a)
def main():
    print(minus_quadratic(1,-7,10))
main()

print('The roots are x = 5, x = 2.')











import math

#Test input uses points (1,1) and (1,5)
def distance(x1, x2, y1, y2):
    return math.sqrt(math.pow(x2 - x1, 2) + math.pow(y2 - y1, 2))
def main():
    print(distance(1, 4, 1, 5))


def height_to_cm(feet, inches):
    return (feet * 30.48)+ (inches * 2.54)
def main():
    print(height_to_cm(5,8))
main()

def weight_to_kg(lbs):
    return (lbs * 0.4536)
def main():
    print(weight_to_kg(153))
main()

