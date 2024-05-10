class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height

    def get_area(self):
        return self.width * self.height

    def get_perimeter(self):
        return 2 * self.width + 2 * self.height

    def get_diagonal(self):
        return (self.width ** 2 + self.height ** 2) ** .5

    def get_picture(self):
        if self.width > 50 or self.height > 50:
            return "Too big for picture"
        picture = ''
        for row in range(self.height):
            for col in range(self.width):
                if row == 0 or row == (self.height - 1):
                    picture += '*' if col < (self.width - 1) else '*\n'
                else:
                    if col == 0:
                        picture += '*'
                    elif col == (self.width - 1):
                        picture += '*\n'
                    else:
                        picture += ' '
        return picture

rect = Rectangle(10, 10)
print(rect.get_picture())