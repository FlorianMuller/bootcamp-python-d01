from vector import Vector, VectorException


def test_vector():
    # Init with list
    vec = Vector([1, 2, 3])
    print(vec.__dict__)

    # Init with size
    vec = Vector(10)
    print(vec.__dict__)

    # Init with range
    vec = Vector((40, 42))
    print(vec.__dict__)

    # Add
    print(Vector(3) + Vector((10, 13)))

    # Add with diffrent size
    try:
        print(Vector(3) + Vector(5))
    except VectorException as e:
        print(e)
    
    # Sub
    print(Vector(3) - Vector((10, 13)))

    # Sub with diffrent size
    try:
        print(Vector(3) - Vector(5))
    except VectorException as e:
        print(e)

    # Mul with scalar
    print(Vector(4) * 4)

    # Mul with Vector
    print(Vector(4) * Vector(4))
    
    # Sub with diffrent size
    try:
        print(Vector(3) * Vector(5))
    except VectorException as e:
        print(e)


if __name__ == "__main__":
    test_vector()
