# -*- coding: utf-8 -*-

__author__ = 'Fabian Nemazi'
__email__ = 'fabinema@nmbu.no'


class LCGRand:
    def __init__(self, seeds):
        self.seeds = seeds
        self.slope = 7 ** 5
        self.congruence_class = 2 ** 31 - 1

    def rand(self):
        self.seeds = (self.slope*self.seeds) % self.congruence_class
        return self.seeds

    def random_sequence(self, length):
        return RandIter(self, length)

    def infinite_random_sequence(self):
        while True:
            yield self.rand()


class RandIter:
    def __init__(self, random_number_generator, length):
        self.generator = random_number_generator
        self.length = length
        self.num_generated_numbers = None

    def __iter__(self):
        if self.num_generated_numbers is not None:
            raise RuntimeError
        self.num_generated_numbers = 0
        return self

    def __next__(self):
        if self.num_generated_numbers is None:
            raise RuntimeError()
        if self.num_generated_numbers == self.length:
            raise StopIteration
        point = self.generator.rand()
        self.num_generated_numbers += 1
        return point

    def infinite_random_sequence(self):
        self.generator.infinite_random_sequence()

