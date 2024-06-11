from abc import ABC, abstractmethod

'''
 Для более детального изучения:
 https://refactoring.guru/ru/design-patterns/proxy

 Представим, что у нас есть некоторый класс, который делает 
 очень нагрузкоемкую работу. Очевидно, мы не хотим инициализировать
 объект этого класса тогда, когда он нам не нужен; мы бы, наоборот,
 хотели создавать объект этого класса тогда, когда
 это действительно необходимо.

 В данной задаче нам может помочь паттерн "Заместитель". Его идея заключается
 в том, чтобы объект-посредник(proxy) инициализировал тяжелый объект.

 В примере изобразим выгрузку очень огромного объема данных из БД при создании
 объекта. Плюс будем проверять, может ли вообще пользователь получать эти
 данные.
'''

# Определим общий интерфейс для "тяжелого" класса и посрденика


class Connector(ABC):

    @abstractmethod
    def get_huge_data(self) -> str:
        raise NotImplementedError

# Определим "тяжелый" класс


class DatabaseHandler(Connector):

    def get_huge_data(self) -> str:
        return 'Getting very HUGE data...'

# Определим класс заместитель


class ProxyDatabaseHandler(Connector):

    def __init__(self, handler: Connector, role: str) -> None:
        # Получаем объект тяжелого класса
        # Получаем доступ пользователя
        self.__handler = handler
        self.__role = role

    def get_huge_data(self) -> str:
        if self.__role in ('ADMIN', 'USER'):
            return self.__handler.get_huge_data()
        else:
            return 'Permission denied'


def main():
    handler = DatabaseHandler()
    proxy = ProxyDatabaseHandler(handler, 'ADMIN')
    print(proxy.get_huge_data())


if __name__ == '__main__':
    main()
