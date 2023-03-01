"""Функции для работы с массивами"""


def get(array, index, default=None):
    """
    Извлекает из списка значение по указанному индексу, если индекс существует.
    Если индекс не существует, возвращает значение по умолчанию.
    Функция работает только с неотрицательными индексами.
    :param array: исходный список.
    :param index: индекс извлекаемого элемента.
    :param default: значение по-умолчанию.
    :return: значение по индексу или значение по-умолчанию.
    """
    try:
        return array[index]
    except:
        return default


def my_slice(coll, start=0, end=None):
    """
    Возвращает новый массив, содержащий копию части исходного массива.
    :param coll: исходный список.
    :param start: индекс, по которому начинается извлечение. Если индекс отрицательный,
    start указывает смещение от конца списка. По умолчанию равен нулю.
    :param end: индекс, по которому заканчивается извлечение (не включая элемент с индексом end).
    Если индекс отрицательный, end указывает смещение от конца списка. По умолчанию равен длине исходного списка.
    :return: массив элементов
    """
    length = len(coll)

    if length == 0:
        return []

    normalized_end = length if end is None else end

    normalized_start = start

    if normalized_start < 0:
        if normalized_start < -length:
            normalized_start = 0
        else:
            normalized_start += length

    return coll[normalized_start:normalized_end]

def get_val(collection, key, default='git'):
    """
    Функция возвращает значение из словаря по переданному ключу, если ключ существует.
    В ином случае возвращается значение default
    :param collection: исходный словарь
    :param key: ключ
    :param default: возращаемое значение, если ключ не найден (по-умолчанию 'git')
    :return: значение по ключу из словаря или default
    """
    return collection.get(key, default)

