nested_list1 = [
    ['a', 'b', 'c'],
    ['d', 'e', 'f', 'h', False],
    [1, 2, None],
]

nested_list2 = [
    ['a', 'b', 'c'],
    ['d', 'e', 'f'],
    [1, 2, None],
]

class FlatIteratoPresent:
    def __init__(self, lst):
        self.lst = sum(lst, [])

    def __iter__(self):
        self.index = -1
        return self

    def __next__(self):
        self.index += 1
        if self.index == len(self.lst):
            raise StopIteration
        else:
            return self.lst[self.index]


class FlatIteratorList:
    def __init__(self, my_list):
        self.my_list = my_list

    def __iter__(self):
        self.iter_queue = []
        self.current_iter = iter(self.my_list)
        return self

    def __next__(self):
        while True:
            try:
                self.current_element = next(self.current_iter)
            except StopIteration:
                if not self.iter_queue:
                    raise StopIteration
                else:
                    self.current_iter = self.iter_queue.pop()
                    continue
            if isinstance(self.current_element, list):
                self.iter_queue.append(self.current_iter)
                self.current_iter = iter(self.current_element)
            else:
                return self.current_element


def flat_generator_present(my_list):
    for lists in my_list:
        for item in lists:
            yield item


def flat_generator_list(my_list):
    for item in my_list:
        if isinstance(item, list):
            for element in flat_generator_list(item):
                yield element
        else:
            yield item               

for item in FlatIteratoPresent(nested_list1):
    print(item)
flat_list = [item for item in FlatIteratoPresent(nested_list1)]
print(flat_list)
for item in FlatIteratorList(nested_list2):
    print(item)
flat_list2 = [item for item in FlatIteratorList(nested_list2)]
print(flat_list2)
for item in flat_generator_present(nested_list1):
    print(item)
for item in flat_generator_list(nested_list2):
    print(item)