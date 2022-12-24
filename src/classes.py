#!/usr/bin/python3

# Подключаем наследованные классы. Так как они наследуются от Animal
# мы уже непосредственно в этих модулях подключили Animal, подключение
# Animal здесь уже не требуется
from Dog import Dog
from Cat import Cat

some_cat = Cat('male')
some_dog = Dog('female')

some_cat.meow()
some_dog.bark()
