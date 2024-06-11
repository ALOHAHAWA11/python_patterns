'''
 Для более детального изучения:
 https://refactoring.guru/ru/design-patterns/singleton

 Напишем пример реализации паттерна "Одиночка". Суть заключается в
 предоставлении одного и того же объекта в любой точке кода.
 В примере будем создавать объект db_handler, котоорый должен
 взаимодействовать с БД. Реализация соединения с БД будет "абстрактной".
'''

# Напишем метакласс, который будет определять логику паттерна.


from typing import Any


class Singleton(type):

    _instances: dict = {}

    def __call__(cls, *args: Any, **kwargs: Any) -> Any:
        # Создаем словарь сущностей класса. Проверяем, есть ли
        # уже созданные сущности в методе вызова __call__.
        # Для обеспечения потокобезопаности можно использовать
        # threding.Lock
        if cls not in cls._instances:
            instance = super().__class__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


# Передадим, как метакласс для определения поведения класса.

class DataBaseHandler(metaclass=Singleton):

    def create_connection(self):
        return 'Connection was created'


def main():
    first_db_handler = DataBaseHandler()
    second_db_handler = DataBaseHandler()

    if id(first_db_handler) == id(second_db_handler):
        print(
            f'First handler ({id(first_db_handler)}) '
            f'is second handler ({id(second_db_handler)})'
        )


if __name__ == '__main__':
    main()
