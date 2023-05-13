from typing import Any


class Car:
    def __init__(self, name):
        self._name = name
        pass

    def get_name(self):
        return self._name

    def start(self):
        print("Car is moving")
        pass

    def stop(self):
        print("Car is stopped")
        pass


car_bmw = Car('BMW')
print(car_bmw.get_name())
car_bmw.start()

car_vw = Car('VW')
print(car_vw.get_name())

print(type(car_bmw))
print(isinstance(car_bmw, Car))
print('\n')


# get all methods
print(dir(car_bmw))

print(car_bmw._name)
print(Car.get_name(car_bmw))


# add self attributes to objects
class Comment:
    def __init__(self, text):
        self.text = text
        self.votes_qty = 0
        pass

    def up_vote(self, qnt):
        self.votes_qty += qnt
        pass

    def reset_votes(self):
        self.votes_qty = 0
        pass

    # static method in class
    @staticmethod
    def merge_comments(first, second):
        return f"{first} {second}"


com_1 = Comment("Hello Taras")
print(com_1.text)
print(com_1.__dict__)

# practice
print('\n')
my_comment = Comment("my comment")
print(my_comment)
print(type(my_comment))
print(my_comment.__dict__)
print(dir(my_comment))
print('\n')
print(my_comment.text)
print(my_comment.votes_qty)
my_comment.up_vote(5)
print(my_comment.votes_qty)
my_comment.up_vote = 10

# will be error - we create new attribute and object will be cat it but not a method on base class
# my_comment.up_vote(20)

# Home Task
print('\n')


class Image:
    # class attribute example
    total_images = 0

    def __init__(self, resolution, extension, title=""):
        self.resolution = resolution
        self.extension = extension
        self.title = title
        Image.total_images += 1
        pass

    def resize(self, width, height):
        self.resolution = f"{width}x{height}"
        pass

    def change_extension(self, new_ext):
        self.extension = new_ext
        pass

    def change_title(self, new_title):
        self.title = new_title
        pass

    @staticmethod
    def print_size(image):
        print(image.resolution)


img1 = Image('1920x1080', '.jpg', "Cats and dogs")
img2 = Image('640x480', '.bmp', "Cars in the rain")
print("Total images:", Image.total_images)
print(img1.__dict__)
img1.resize(1024, 768)
print(img1.resolution)
print(img1.total_images)

# static methods in class
# class TestClass:

#     @staticmethod
#     def text_method():
#         pass


# magic methods in class - vary important
class Comment2:
    def __init__(self, text, votes=0):
        self.text = text
        self.votes_qty = votes
        pass

    def up_vote(self, qnt):
        self.votes_qty += qnt
        pass

    def reset_votes(self):
        self.votes_qty = 0
        pass

    # static method in class
    @staticmethod
    def merge_comments(first, second):
        return f"{first} {second}"

    # redefine additional (+)
    def __add__(self, other):
        return Comment2(f"{self.text} | {other.text}", self.votes_qty + other.votes_qty)

    # redefine eqivalential (==)
    def __eq__(self, other):
        return self.text == other.text and self.votes_qty == other.votes_qty


comm1 = Comment2("text 1", 2)
comm2 = Comment2("text 1", 2)

comm3 = comm1 + comm2
print(comm3.__dict__)
print(comm1 == comm2)


# legacy in classes
class ExtendedListSample(list):
    def print_list_info(self):
        print(f"List has {len(self)} elements")


my_list = ExtendedListSample([])
my_list.append(56)
my_list.print_list_info()


# practice
class ExtendedList(list):
    def print_list_info(self):
        print(f"List has {len(self)} elements")


my_list = ExtendedList([])
my_list.append(7)
my_list.append(16)
print(my_list)

print(list.__subclasses__())


# Getters and Setters
# __prop_name - starting from '__' property is private
# __method_name - starting from '__' method is private
print('\n')


class Dog:
    __name: str
    __color: str

    def __init__(self: object, name: str, color: str) -> None:
        self.__name = name
        self.__color = color
        pass

    def __get_name(self: object) -> str:
        return self.__name

    def __get_color(self: object) -> str:
        return self.__color

    def __set_color(self: object, color: str) -> None:
        self.__color = color
        pass

    def __set_name(self: object, name: str) -> None:
        self.__name = name
        pass

    name = property(__get_name, __set_name)
    color = property(__get_color, __set_color)


dd = Dog('Spanky', 'Red')
print(dd.color)
dd.color = "White"
print(dd.name)
dd.name = 156
print(dd.name)
print(dd.color)
