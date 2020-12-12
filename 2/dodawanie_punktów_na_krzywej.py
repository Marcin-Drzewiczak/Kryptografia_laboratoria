def point_addition(x1, y1, x2, y2, p):
    alpha = ((y2 - y1)*(x2-x1)) ** -1 % p
    x3 = (alpha**2 - x1 - x2) % p
    y3 = (alpha*(x1 - x3) - y1) % p
    return x3, y3


#czy punkt należy do krzywej eliptycznej
def is_this_point_on_ecliptic_curve(x:int,y:int,A:int,B:int,p:int):
    print("P(" + str(x) + "," + str(y) + ")\n")
    y=y%p
    print("P mod " + str(p) + " = P(" + str(x) + "," + str(y) + ")\n")
    fx=((x**3)%p+(A*x)%p+B%p)%p
    print("y^2 = [(" + str(x) + "^3) + " + str(A) + " * " + str(x) + " + " + str(B) + "] mod " + str(p) + " = " + str(fx) + "\n")
    if((y**2)%p==fx):
        return True
    else:
        return False


if __name__ == "__main__":

    point1 = [9, 7]
    point2 = [13, 11]
    mod = 19
    # wynik: 17, 15 lub 17, 4

    print(point_addition(point1[0], point1[1], point2[0], point2[1], mod))