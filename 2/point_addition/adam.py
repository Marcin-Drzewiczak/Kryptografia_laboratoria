from collections import namedtuple


class PointAddition:
    def __init__(self, p, a, b):
        self.p = p
        self.a = a
        self.b = b

        # The point at infinity (origin for the group law).
        self.O = 'Origin'

    def valid(self, P):
        """
        Determine whether we have a valid representation of a point
        on our curve.  We assume that the x and y coordinates
        are always reduced modulo p, so that we can compare
        two points for equality with a simple ==.
        """
        if P == self.O:
            return True
        else:
            return (
                (self.get_power_optimal(P.y, 2) - (self.get_power_optimal(P.x, 3) + a*P.x + b)) % self.p == 0 and
                0 <= P.x < self.p and 0 <= P.y < self.p)

    def inv_mod_p(self, x):
        """
        Compute an inverse for x modulo p, assuming that x
        is not divisible by p.
        """
        if x % self.p == 0:
            raise ZeroDivisionError("Impossible inverse")
        return self.get_power_optimal(x, self.p-2)

    def ec_inv(self, P):
        """
        Inverse of the point P on the elliptic curve y^2 = x^3 + ax + b.
        """
        if P == self.O:
            return P
        return Point(P.x, (-P.y) % self.p)

    def ec_add(self, P, Q):
        """
        Sum of the points P and Q on the elliptic curve y^2 = x^3 + ax + b.
        """
        if not self.valid(P):
            raise ValueError("Invalid input: %s, %s" % (P.x, P.y))
        if not self.valid(Q):
            raise ValueError("Invalid input: %s, %s" % (Q.x, Q.y))

        # Deal with the special cases where either P, Q, or P + Q is
        # the origin.
        if P == self.O:
            result = Q
        elif Q == self.O:
            result = P
        elif Q == self.ec_inv(P):
            result = self.O
        else:
            # Cases not involving the origin.
            if P == Q:
                dydx = (3 * self.get_power_optimal(P.x, 2) + a) * self.inv_mod_p(2 * P.y)
            else:
                dydx = (Q.y - P.y) * self.inv_mod_p(Q.x - P.x)
            x = (self.get_power_optimal(dydx, 2) - P.x - Q.x) % p
            y = (dydx * (P.x - x) - P.y) % p
            result = Point(x, y)

        # The above computations *should* have given us another point
        # on the curve.
        assert self.valid(result)
        return result

    def get_power_optimal(self, a, n):
        res = 1
        a = a % self.p
        while n > 0:
            if n % 2:
                res = (res * a) % self.p
                n = n - 1
            else:
                a = (a ** 2) % self.p
                n = n // 2
        return res % p


if __name__ == "__main__":
    # Create a simple Point class to represent the affine points.
    Point = namedtuple("Point", "x y")

    # point1 = [9, 7]
    # point2 = [13, 11]
    # wynik: 17, 15

    # Choose a particular curve and prime.  We assume that p > 3.
    # Y2=X3+1 nad F7
    p = 7
    a = 0
    b = 1

    field = PointAddition(p, a, b)

    print(field.ec_add(Point(1, 3), Point(2, 4)))
    # wynik: 5, 0 na prezentacji

    print(field.ec_add(Point(1, 3), Point(1, 3)))
    # wynik: 0, 1 na prezentacji
