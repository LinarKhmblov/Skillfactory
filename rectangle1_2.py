from rectangle1 import Rectangle, Square

rect_1 = Rectangle(3, 4)
rect_2 = Rectangle(12, 5)

print(rect_1.get_ares())
print(rect_2.get_ares())

square_1 = Square(5)
square_2 = Square(10)

print(square_1.get_area_squares(),
      square_2.get_area_squares())

figures = [rect_1, rect_2, square_1, square_2]
for figure in figures:
    if isinstance(figure, Square):
        print(figure.get_area_squares())
    else:
        print(figure.get_ares())
