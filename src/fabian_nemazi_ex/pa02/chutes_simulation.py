import random


class Board:
    Default_ladders = [(1, 40), (8, 10), (36, 52), (43, 62),
                       (49, 79), (65, 82), (68, 85)]

    Default_chutes = [(24, 5), (33, 3), (42, 30), (56, 37), (64, 27),
                      (74, 12), (87, 70)]

    Goal = 90

    def __init__(self, ladders=None, chutes=None, goal=None):
        # If ladders input is None we will assign the values to the defaults
        # follows the same principle all the way
        if ladders is None:
            ladders = Board.Default_ladders
        if chutes is None:
            chutes = Board.Default_chutes
        self.goal = Board.Goal if goal is None else goal
        # We are asking the user for input, therefore we want to check if the
        # input are valid. Checking for valid ladders and snake format.
        for start, ending in ladders:
            # Iterating through a list with tupples
            if start >= ending:
                raise ValueError(
                    "invalid input, ladders must always lead forward")
        for start, ending in chutes:
            if start <= ending:
                raise ValuError(
                    "invalid input, snakes must always lead downwards")
        if self.goal <= 0:
            raise ValueError("the goal must be higher than 0")
        # Creating a dictionary of the ladders and snakes
        self.ladders_and_snakes = {start: end
                                   for start, end in ladders + chutes}

    def goal_reached(self, position):
        """
        Method goal_reached() shall return true if it
        is passed a position at or beyond the goal.
        """
        return position >= self.goal

    def position_adjustment(self, position):
        """
        handle changes in position due to snakes and ladders.
        It accepts a position as argument and returns the number of
        positions the player must move forward, to get to the correct position.
        If the player is not at the start of a chute or ladder,
        the method returns 0.

        """
        new_position = self.ladders_and_snakes.get(position, position)

        return new_position - position


class Player:
    def __init__(self, board):
        self._board = board
        self.position = 0
        self.moves = 0

    def move(self):
        """
        The move() method moves the player by implementing a die cast,
        the following move and, if necessary,
        a move up a ladder or down a chute.
        It does not return anything"""
        self.position += random.randint(1, 6)
        self.moves += 1
        self.position += self._board.position_adjustment(self.position)


class ResilientPlayer(Player):
    def __init__(self, board, extra_steps=1):
        super().__init__(board)
        self.extra_steps = extra_steps

    def move(self):
        """
        the move() method is the same as in the class Player.
        The little difference is that a resilient player is to
        take extra steps after a dice is thrown
        returns nothing
        """
        self.position += random.randint(1, 6) + self.extra_steps
        self.position += self._board.position_adjustment(self.position)
        self.moves += 1


class LazyPlayer(Player):
    def __init__(self, board, dropped_steps=1):
        super().__init__(board)
        self.dropped_steps = dropped_steps

        if dropped_steps >= 5:
            raise ValuError(
                "The input is invalid. "
                "The player will never move forward "
                "with a input higher than 5")

    def move(self):
        self.position += max(0, random.randint(1, 6) - self.dropped_steps)
        self.position += self._board.position_adjustment(self.position)
        self.moves += 1


class Simulation:
    def __init__(self, player_field, board=None, seed=12345,
                 randomize_players=False):
        self.player_field = player_field
        self.player_types = frozenset(pc.__name__ for pc in player_field)
        self.board = board if board is not None else Board()
        self.randomize = randomize_players
        self.results = []

        random.seed(seed)

    def single_game(self):
        """
        Returns winner type and number of steps for single game.

        :returns: (number_of_steps, winner_class) tuple
        """

        players = [players(self.board) for players in self.player_field]
        if self.randomize:
            random.shuffle(players)

        while True:
            for player in players:
                player.move()
                if player._board.goal_reached(player.position):
                    return player.moves, type(player).__name__

    def run_simulation(self, number_of_games):
        """
        run_simulation() runs a given number of games and
        stores the results in the Simulation object. It returns nothing."""
        for _ in range(number_of_games):
            self.results.append(self.single_game())

    def get_results(self):
        """
        get_results() returns all results generated by
        run_simulation() calls so far as a list of result tuples"""
        return self.results

    def winners_per_type(self):
        """
        winners_per_type() returns a dictionary
        mapping player types to the number of wins,
        """
        winner_types = list(zip(*self.results))[1]
        return {player_type: winner_types.count(player_type)
                for player_type in self.player_types}

    def durations_per_type(self):
        """
        durations_per_type() returns a dictionary mapping player types to
        lists of game durations for that type"""
        return {player_type: [win for win, types in self.results
                              if types == player_type]
                for player_type in self.player_types}

    def players_per_type(self):
        """
        players_per_type returns a dictionary showing
        how many players of each type participate
        """
        return {player_type.__name__: self.player_field.count(player_type)
                for player_type in frozenset(self.player_field)}


if __name__ == "__main__":
    print('**** First Simulation: Single player, standard board ****')
    sim = Simulation([Player])
    print(sim.single_game())

    sim.run_simulation(10)
    print(sim.players_per_type())
    print(sim.winners_per_type())
    print(sim.durations_per_type, "ddd")

    print('\n**** Second Simulation: Four players, standard board ****')
    sim = Simulation([Player, Player, LazyPlayer, ResilientPlayer])
    print(sim.single_game())

    sim.run_simulation(10)
    print(sim.players_per_type())
    print(sim.winners_per_type())
    print(sim.durations_per_type)

    print('\n**** Third Simulation: Four players, small board ****')
    my_board = Board(ladders=[(3, 10), (5, 8)], chutes=[(9, 2)], goal=20)
    sim = Simulation([Player, Player, LazyPlayer, ResilientPlayer],
                     board=my_board)
    print(sim.single_game())

    sim.run_simulation(10)
    print(sim.players_per_type())
    print(sim.winners_per_type())
    print(sim.durations_per_type)




#c = Board(ladders=)