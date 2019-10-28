__author__ = 'Fabian Nemazi'
__email__ = 'fabinema@nmbu.no'


class LCGRand:
    def __init__(self, seeds):
        self.seeds = seeds

    def rand(self):
        a = 7**5
        m = 2**31-1
        self.seeds = (a*self.seeds) % m
        return self.seeds


class ListRand:
    def __init__(self, list_of_numbers):
        self.list = list_of_numbers
        self.next = 0

    def rand(self):
        if len(self.list) <= self.next:
            raise RuntimeError
        random_number = self.list[self.next]
        self.next += 1
        return random_number


if __name__ == '__main__':
    lcg = LCGRand(200)
    random = ListRand([5, 12, 77, 1, 199, 2, 6, 9])
    print("drawing random numbers")
    fmt = "{:>10} {:>10}"
    print(fmt.format("ListRNG", "LCG"))
    for _ in range(5):
        print(fmt.format(lcg.rand(), random.rand()))



