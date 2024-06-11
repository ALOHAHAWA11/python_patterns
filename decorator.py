from abc import ABC, abstractmethod

'''
 Для более детального изучения:
 https://refactoring.guru/ru/design-patterns/decorator

 Напишем пример реализации паттерна декоратор. Суть декоратора заключается в
 многократной модификации поведения какой-либо сущности.

 Предположим, что у нас есть базовый класс, который может записывать и читать
 данные. Мы хотим добавить дополнительное поведение для класса. К примеру,
 мы хотим чтобы данные не только записались в файл, но были зашифрованы
 и/или сжаты. При чтении можно делать обратные действия.
'''

# Реализуем общий интерфейс для базового класса и базового класса
# декоратора.


class DataSource(ABC):

    @abstractmethod
    def write_data(self, data: str):
        raise NotImplementedError

    @abstractmethod
    def read_data(self) -> str:
        raise NotImplementedError


# Создадим класс базового объекта, реализуем в нем логику чтения/записи в файл


class FileDataSource(DataSource):

    def __init__(self, filename: str) -> None:
        self.__filename = filename

    def write_data(self, data: str):
        with open(self.__filename, 'w+') as file:
            file.write(data)

    def read_data(self) -> str:
        with open(self.__filename, 'r') as file:
            return file.readline()


# Создадим класс базового декоратора, в котором должна быть ссылка на
# декорируемый объект. ДЕЛЕГИРУЕМ действия вложенному объекту


class DataSourceDecorator(DataSource):

    def __init__(self, data_source: DataSource) -> None:
        self.__wrappee = data_source

    def write_data(self, data: str):
        self.__wrappee.write_data(data)

    def read_data(self) -> str:
        return self.__wrappee.read_data()


# Создадим конкретные декораторы, наследуюя их от базового

class EncryptionDecorator(DataSourceDecorator):

    def write_data(self, data: str):
        data = data + 'encrypted'
        super().write_data(data)

    def read_data(self) -> str:
        return super().read_data()[:-9]


class CompressionDecorator(DataSourceDecorator):

    def write_data(self, data: str):
        data = data + 'compressed'
        super().write_data(data)

    def read_data(self) -> str:
        return super().read_data()[:-10]


# Используя флаги и декораты, можем изменять поведение декорируемого объекта

def main():
    is_enable_encryption = True
    is_enable_compress = True

    source = FileDataSource('data.data')
    if is_enable_compress:
        source = CompressionDecorator(source)
    if is_enable_encryption:
        source = EncryptionDecorator(source)

    source.write_data('TEST')
    print(source.read_data())


if __name__ == '__main__':
    main()
