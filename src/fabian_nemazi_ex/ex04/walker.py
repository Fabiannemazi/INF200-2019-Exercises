import random as rd


class Walker:
    def __init__(self, initial_pos, home_pos):
        self.start = initial_pos
        self.end = home_pos
        self.steps = 0

    def move(self):
        move = (2 * rd.randint(0, 1)) - 1
        self.start = self.start + move
        self.steps += 1
        # print(self.steps)
        # print(self.get_position())

    def is_at_home(self):
        return self.start == self.end

    def get_position(self):
        return self.start

    def get_steps(self):
        return self.steps


def get_home(initial_pos, home_pos):
    walker = Walker(initial_pos, home_pos)
    while not walker.is_at_home():
        walker.move()
    return walker.get_steps()


if __name__ == '__main__':
    distances = [1, 2, 5, 10, 20, 50, 100]
    for distance in distances:
        path_lengths = [get_home(0, distance) for _ in range(5)]
        print('Distance: {} -> Path lengths: {}'.format(
            distance, sorted(path_lengths)))



