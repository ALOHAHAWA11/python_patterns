from abc import ABC, abstractmethod

'''
 Для детального изучения:
 https://refactoring.guru/ru/design-patterns/strategy

 Паттерн "Стратегия" предназначен для определения семейства схожих
 алгоритмов, которые помещаются в собственные классы и могут быть выбраны
 для решения какой-либо задачи.

 В данном примере будем сортировать списки разными образами.
 Вид сортировки будет выбираться в необходимом контексте через
 делегирующий объект.
'''

# Создадим единый интерфейс для всех возможных стратегий
# и делегирующего класса


class ListSortStrategy(ABC):

    @abstractmethod
    def sort_list(self, lst: list) -> list:
        raise NotImplementedError


# Определим классы видов сортировки


class BubbleSortStrategy(ListSortStrategy):

    def sort_list(self, lst: list) -> list:
        for i in range(len(lst) - 1):
            for j in range(len(lst) - 1 - i):
                if lst[i] > lst[j + 1]:
                    lst[j], lst[j + 1] = lst[j + 1], lst[j]
        return lst


class InsertSortStrategy(ListSortStrategy):

    def sort_list(self, lst: list) -> list:
        for i in range(1, len(lst)):
            key = lst[i]
            j = i-1
            while j >= 0 and key < lst[j]:
                lst[j+1] = lst[j]
                j -= 1
            lst[j+1] = key
        return lst


# Опишем делегирующий класс


class ListSortContext(ListSortStrategy):

    def __init__(self, strategy: ListSortStrategy) -> None:
        self.__strategy = strategy

    def sort_list(self, lst: list) -> list:
        return self.__strategy.sort_list(lst)


def main():
    strategy = BubbleSortStrategy()

    context = ListSortContext(strategy)

    lst = [345, 5, -23, 534, 5, 0, 1, 2, 4, -5, 4, -3]

    print('Bubble sort:', context.sort_list(lst))

    strategy = InsertSortStrategy()

    context = ListSortContext(strategy)

    lst = [-345, -5, -23, -534, -5, -0, -1, -2, -4, 5, -4, 3]

    print('Insert sort:', context.sort_list(lst))


if __name__ == '__main__':
    main()
