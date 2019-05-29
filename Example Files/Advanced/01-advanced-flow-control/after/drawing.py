
from functools import singledispatch


class Shape:

    def __init__(self, solid):
        self.solid = solid


class Parallelogram(Shape):

    def __init__(self, pa, pb, pc, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.pa = pa
        self.pb = pb
        self.pc = pc

    def intersects(self, shape):
        # Delegate to the generic function, swapping arguments
        return intersects_with_parallelogram(shape, self)


class Triangle(Shape):

    def __init__(self, pa, pb, pc, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.pa = pa
        self.pb = pb
        self.pc = pc

    def intersects(self, shape):
        # Delegate to the generic function, swapping arguments
        return intersects_with_triangle(shape, self)


class Circle(Shape):

    def __init__(self, center, radius, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.center = center
        self.radius = radius

    def intersects(self, shape):
        # Delegate to the generic function, swapping arguments
        return intersects_with_circle(shape, self)


# Added solution to double dispatch exercise e.g. triangle and parallelogram!


@singledispatch
def intersects_with_parallelogram(shape, parallelogram):
    raise TypeError("Don't know how to compute intersection of {!r} with {!r} and {!r}"
                    .format(parallelogram, shape))


@intersects_with_parallelogram.register(Circle)
def _(shape, parallelogram):
    return parallelogram_intersects_circle(parallelogram, shape)


@intersects_with_parallelogram.register(Parallelogram)
def _(shape, parallelogram):
    return parallelogram_intersects_parallelogram(parallelogram, shape)


@intersects_with_parallelogram.register(Triangle)
def _(shape, parallelogram):
    return parallelogram_intersects_triangle(parallelogram, shape)


@singledispatch
def intersects_with_triangle(shape, triangle):
    raise TypeError("Don't know how to compute intersection of {!r} with {!r} and {!r}"
                    .format(triangle, shape))


@intersects_with_triangle.register(Circle)
def _(shape, triangle):
    return triangle_intersects_circle(triangle, shape)


@intersects_with_triangle.register(Parallelogram)
def _(shape, triangle):
    return triangle_intersects_parallelogram(triangle, shape)


@intersects_with_triangle.register(Triangle)
def _(shape, triangle):
    return triangle_intersects_triangle(triangle, shape)


@singledispatch
def intersects_with_circle(shape, circle):
    raise TypeError("Don't know how to compute intersection of {!r} with {!r}"
                    .format(circle, shape))


@intersects_with_circle.register(Circle)
def _(shape, circle):
    return circle_intersects_circle(circle, shape)


@intersects_with_circle.register(Parallelogram)
def _(shape, circle):
    return circle_intersects_parallelogram(circle, shape)


@intersects_with_circle.register(Triangle)
def _(shape, circle):
    return circle_intersects_triangle(circle, shape)


@singledispatch
def draw(shape):
    raise TypeError("Don't know how to draw {!r}".format(shape))


@draw.register(Circle)
def _(shape):
    print("\u25CF" if shape.solid else "\u25A1")


@draw.register(Parallelogram)
def _(shape):
    print("\u25B0" if shape.solid else "\u25B1")


@draw.register(Triangle)
def _(shape):
    # Draw a triangle
    print("\u25B2" if shape.solid else "\u25B3")


def parallelogram_intersects_circle(parallelogram, shape):
    pass


def parallelogram_intersects_parallelogram(parallelogram, shape):
    pass


def parallelogram_intersects_triangle(parallelogram, shape):
    pass


def triangle_intersects_circle(triangle, shape):
    pass


def triangle_intersects_parallelogram(triangle, shape):
    pass


def triangle_intersects_triangle(triangle, shape):
    pass


def circle_intersects_circle(circle, shape):
    pass


def circle_intersects_parallelogram(circle, shape):
    pass


def circle_intersects_triangle(circle, shape):
    pass


def main():
    shapes = [Circle(center=(0, 0), radius=5, solid=False),
              Parallelogram(pa=(0, 0), pb=(2, 0), pc=(1, 1), solid=False),
              Triangle(pa=(0, 0), pb=(1, 2), pc=(2, 0), solid=True)]

    for shape in shapes:
        draw(shape)


if __name__ == '__main__':
    main()
