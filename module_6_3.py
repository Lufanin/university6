# class Horse:
#     def __init__(self):
#         self.x_distance = 0
#         self.sound = 'Frrr'
#
#     def run(self, dx):
#         self.x_distance += dx
#
#
# class Eagle:
#     def __init__(self):
#         self.sound = 'I train, eat, sleep, and repeat'
#         self.y_distance = 0
#
#     def fly(self, dy):
#         self.y_distance += dy
#
#
# class Pegasus(Horse, Eagle):
#     def __init__(self):
#         Horse.__init__(self)
#         Eagle.__init__(self)
#
#     def move(self, dx, dy):
#         self.run(dx)
#         self.fly(dy)
#
#     def get_pos(self):
#         return (self.x_distance, self.y_distance)
#
#     def voice(self):
#         print(self.sound)
#
#
# print(Pegasus.mro())
# p1 = Pegasus()
#
# print(p1.get_pos())
# p1.move(10, 15)
# print(p1.get_pos())
# p1.move(-5, 20)
# print(p1.get_pos())
#
# p1.voice()

class Horse:
    def __init__(self):
        super().__init__()
        self.x_distance = 0
        self.sound = 'Frrr'

    def run(self, dx):
        self.x_distance += dx


class Eagle:
    def __init__(self):
        self.y_distance = 0
        self.sound = 'I train, eat, sleep, and repeat'

    def fly(self, dy):
        self.y_distance += dy


class Pegasus(Horse, Eagle):
    def __init__(self, dx=0, dy=0, sound=''):
        super().__init__()  # Вызов инициализаторов родительских классов
        Eagle.__init__(self)  # Явно вызываем инициализатор класса Eagle
        self.fly(dy)
        if sound:  # Если звук передан, используем его
            self.sound = sound

    def move(self, dx, dy):
        self.run(dx)
        self.fly(dy)

    def get_pos(self):
        return (self.x_distance, self.y_distance)

    def voice(self):
        return self.sound


p1 = Pegasus()

print(p1.get_pos())
p1.move(10, 15)
print(p1.get_pos())
p1.move(-5, 20)
print(p1.get_pos())

# Выводим звук в конце
print(p1.voice())  # Это вернет 'I train, eat, sleep, and repeat'