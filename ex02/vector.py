class VectorException(Exception):
    def __init__(self, message):
        super().__init__(message)


def add_vec(l_vec, r_vec):
    if not l_vec.size == r_vec.size:
        raise VectorException("Can't add vector of different size")
    return Vector([l_nbr + r_nbr for l_nbr, r_nbr in zip(l_vec.values, r_vec.values)])


def sub_vec(l_vec, r_vec):
    if not l_vec.size == r_vec.size:
        raise VectorException("Can't subtract vector of different size")
    return Vector([l_nbr - r_nbr for l_nbr, r_nbr in zip(l_vec.values, r_vec.values)])


def div_vec(a, b):
    pass


def mul_vec(vec, other):
    if isinstance(other, int):
        return Vector([nbr * other for nbr in vec.values])
    elif isinstance(other, Vector):
        if not vec.size == other.size:
            raise VectorException("Can't multiply vector of different size")
        return sum([l_nbr * r_nbr for l_nbr, r_nbr in zip(vec.values, other.values)])


class Vector():
    def __init__(self, init):
        if isinstance(init, list):
            self.values = [float(nbr) for nbr in init]
            self.size = len(init)
        elif isinstance(init, int):
            self.values = [float(nbr) for nbr in range(init)]
            self.size = init
        elif isinstance(init, tuple) and len(init) == 2:
            self.values = [float(nbr) for nbr in range(*init)]
            self.size = len(self.values)

    def __str__(self):
        return str(self.values)

    def __repr__(self):
        return self.__dict__

    def __add__(self, rs):
        return add_vec(self, rs)

    def __radd__(self, ls):
        return add_vec(ls, self)

    def __sub__(self, rs):
        return sub_vec(self, rs)

    def __rsub__(self, ls):
        return sub_vec(ls, self)

    def __truediv__(self, rs):
        return div(self, rs)

    def __rtruediv__(self, ls):
        return div(ls, self)

    def __mul__(self, rs):
        return mul_vec(self, rs)

    def __rmul__(self, ls):
        return mul_vec(ls, self)
