def main_1():
    class Rectangle:
        def __init__(self, length, breadth, unit_cost=0):
            self.length = length
            self.breadth = breadth
            self.unit_cost = unit_cost

        def get_perimeter(self):
            return 2 * (self.length + self.breadth)

        @staticmethod
        def get_area():
            return 90

        def calculate_cost(self):
            area = self.get_area()
            return area * self.unit_cost

    # breadth = 120 cm, length = 160 cm, 1 cm^2 = Rs 2000
    r = Rectangle(160, 120, 2000)
    print("Area of Rectangle: %s cm^2" % (r.get_area()))
    print("Cost of rectangular field: Rs. %s " % (r.calculate_cost()))


def main_2():
    # parent class
    class Bird:

        def __init__(self):
            print("Bird is ready")

        def whoisThis(self):
            print("Bird")

        def swim(self):
            print("Swim faster")

    # child class
    class Penguin(Bird):

        def __init__(self, h):
            # call super() function
            super().__init__()
            print("Penguin is ready")
            print("penguin has height", h)

        def whoisThis(self):
            print("Penguin")

        def run(self):
            print("Run faster")

    peggy = Penguin("12m")
    peggy.whoisThis()
    peggy.swim()
    peggy.run()


main_2()
