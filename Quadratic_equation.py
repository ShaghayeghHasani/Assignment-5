import math

def equation ():
    a = float(input("Enter the amount of a: "))
    b = float(input("Enter the amount of b: "))
    c = float(input("Enter the amount of c: "))

    d = b ** 2 - 4 * a * c

    if d < 0:
        print("The equation has no real solutions")
    elif d == 0:
        x = (-b + math.sqrt(b ** 2 - 4 * a * c)) / (2 * a)
        print("The equation has one solution: ", x)
    else:
        x1 = (-b + math.sqrt(b ** 2 - 4 * a * c)) / (2 * a)
        x2 = (-b - math.sqrt(b ** 2 - 4 * a * c)) / (2 * a)
        print("The equation has two solutions: " , x1, "and ", x2)
        
equation()