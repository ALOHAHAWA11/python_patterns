from abc import ABC, abstractmethod

'''
 Для более детального изучения:
 https://refactoring.guru/ru/design-patterns/abstract-factory

 Напишем пример реализации абстрактной фабрики. Будем оперировать двумя типами
 продуктов: диван и стул. Оба проудкта могут быть либо в стиле арт-деко,
 либо в стиле модерн.
'''

# Создадим общие интерфейсы для каждого типа продукта


class Sofa(ABC):

    @abstractmethod
    def do_sofa_action(self) -> str:
        raise NotImplementedError


class Chair(ABC):

    @abstractmethod
    def do_chair_action(self) -> str:
        raise NotImplementedError

# Создадим интерфейс абстрактной фабрики, в котором будут иметься всем методы
# создания каждого типа продуктов. В данном случае: стул и диван.


class AbstractFactory(ABC):

    @abstractmethod
    def create_sofa(self) -> Sofa:
        raise NotImplementedError

    @abstractmethod
    def create_chair(self) -> Chair:
        raise NotImplementedError


# Реализуем классы для каждого типа продукта по каждой ешл вариации.


class ArtDecoSofa(Sofa):

    def do_sofa_action(self) -> str:
        return 'This is art deco sofa!'


class ArtDecoChair(Chair):

    def do_chair_action(self) -> str:
        return 'This is art deco chair!'


class ModernSofa(Sofa):

    def do_sofa_action(self) -> str:
        return 'This is modern sofa!'


class ModernChair(Chair):

    def do_chair_action(self) -> str:
        return 'This is modern chair!'

# Теперь реализуем классы конкретных фабрик для каждой вариации
# продукта. Создадим 2 фабрики: арт деко фабрика и модер фабрика.


class ArtDecoFactory(AbstractFactory):

    def create_chair(self) -> Chair:
        return ArtDecoChair()

    def create_sofa(self) -> Sofa:
        return ArtDecoSofa()


class ModernFactory(AbstractFactory):

    def create_chair(self) -> Chair:
        return ModernChair()

    def create_sofa(self) -> Sofa:
        return ModernSofa()


# Реализуем клиентский код, который будет создавать фабрику

class FactoryPipeline():

    def __init__(self, factory: AbstractFactory) -> None:
        self.__factory = factory

    def create_sofa(self) -> Sofa:
        self.__sofa = self.__factory.create_sofa()
        return self.__sofa

    def create_chair(self) -> Chair:
        self.__chair = self.__factory.create_chair()
        return self.__chair

# Сам клиентский код


def main():
    print('Выберите тип продукта:')
    print('1. Арт-деко;')
    print('2. Модерн.')
    factory = 0
    product_type = int(input())

    if product_type == 1:
        factory = ArtDecoFactory()
    elif product_type == 2:
        factory = ModernFactory()
    else:
        print('Выберете только предложенные варианты!')

    pipeline = FactoryPipeline(
        factory=factory
    )

    chair = pipeline.create_chair()
    print(chair.do_chair_action())
    sofa = pipeline.create_sofa()
    print(sofa.do_sofa_action())


if __name__ == '__main__':
    main()
