from math import pi, sqrt

class Figure:
    def __init__(self, color, sides, filed, sides_count = 0):
        self.sides_count = sides_count
        self.__sides = sides
        self.__color = list(color)
        self.filed = bool(filed)
        if self.sides_count == sides_count:
            self.__sides = int(sides)
        else:
            self.__sides = 1


    def get_color(self):
        return self.__color

    def __is_color(self, r, g, b):
        if 0 <= r <= 255 and 0 <= g <= 255 and 0 <= b <= 255:
            return True

    def set_color(self, r, g, b):
        if self.__is_color(r, g, b):
            self.__color = [r, g, b]

    def get_sides(self):
        self.ls = []
        for i in range(self.sides_count):
            self.ls.append(self.__sides)
        return self.ls

    def __len__(self):
        if isinstance(self.sides_count, int):
            return self.__sides * self.sides_count

    def set_sides(self, *new_sides):
        # counter = 0
        # if len(new_sides) > 1:
        #     for side in new_sides:
        #         counter += 1
        #         if counter == self.sides_count:
        #             self.sides = new_sides
        # elif len(new_sides) == 1 and self.sides_count == 1:
        #     self.sides = new_sides

        if len(new_sides) == self.sides_count:
            if self.sides_count == 1:
                self.__sides = new_sides[0] 
            else:
                new_sides


class Circle(Figure):
    def __init__(self, color, sides, filed, sides_count = 1):
        super().__init__(color, sides, filed, sides_count)
        self.sides_count = 1
        self.__radius = int(sides)/(2 * pi)

    
    def get_radius(self):
        return self.__radius

    def get_square(self):
        return math.pi * self.__radius ** 2


class Triange(Figure):
    def __init__(self, color, sides, filed, sides_count = 3):
        super().__init__(color, sides, filed, sides_count)
        self.sides_count = 3
        self.__a = int(sides[0])
        self.__b = int(sides[1])
        self.__c = int(sides[2])
        self.__height = sqrt(self.__a ** 2 - (self.__c ** 2 / 4))
        
        
    def get_square(self):
        return self.__a * self.__height / 2


class Cube(Figure):
    def __init__(self, color, sides, filed, sides_count = 12):
        super().__init__(color, sides, filed, sides_count)
        self.sides_count = 12

    # def set_sides(self, *new_sides):
    #     super().set_sides(*new_sides)
    #     ls = []
    #     for i in range(1, 13):
    #         ls.append(new_sides)
    #     self.sides = ls
                        
    def get_volume(self):
        self.sides = self.get_sides()[0]
        return self.sides ** 3            
            

circle1 = Circle((200, 200, 100), 10, True) # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6, True)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77) # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15) # Не изменится
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5) # Не изменится
print(cube1.get_sides())
circle1.set_sides(15) # Изменится
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())
