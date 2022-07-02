class CyclicIterator:
    def __init__(self, obj):
        self.obj = obj
        self.iter = iter(obj)

    def __iter__(self):
        return self

    def __next__(self):
        try:
            return next(self.iter)
        except StopIteration:
            self.iter = iter(self.obj)
            return next(self.iter)



cyclic_iterator = CyclicIterator(range(3))
for i in cyclic_iterator:
    print(i)


# for i in '':
#     print(i)
