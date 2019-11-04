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


class Simulation:
    def __init__(self, start, home, seeds):
        self.start = start
        self.home = home
        self.seed = rd.seed(seeds)

    def single_walk(self):
        rd.seed(self.seed)
        single_walker = Walker(self.start, self.home)
        while not single_walker.is_at_home():
            single_walker.move()
        return single_walker.get_steps()

    def run_simulation(self, num_walks):
        return [self.single_walk() for _ in range(num_walks)]


if __name__ == '__main__':
    print(Simulation(0, 10, 12345).run_simulation(20))
    print(Simulation(0, 10, 12345).run_simulation(20))
    print(Simulation(0,10, 54321).run_simulation(20))
    print(Simulation(10, 0, 12345).run_simulation(20))
    print(Simulation(10, 0, 12345).run_simulation(20))
    print(Simulation(10, 0, 54321).run_simulation(20))







