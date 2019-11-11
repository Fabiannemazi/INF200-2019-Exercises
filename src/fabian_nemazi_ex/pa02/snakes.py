import random as rd
import numpy as np

Ladders_and_Snakes = {1: 40, 8: 10, 36: 52, 43: 62, 49: 79, 65: 82, 68: 85,
                      24: 5, 33: 3, 42: 30, 56: 37, 64: 27, 74: 12, 87: 70}

goal = 90


def single_game(num_players):
    # Number of players in the game
    positions = [0] * num_players
    # Number of moves in the game
    num_moves = 0

    while max(positions) < goal:
        for player in range(num_players):
            positions[player] += rd.randint(1, 6)
            if positions[player] in Ladders_and_Snakes:
                positions[player] = Ladders_and_Snakes.get(positions[player])
        num_moves += 1
    # Returns duration of single game
    return num_moves


def multiple_games(num_games, num_players):
    """Returns durations of a number of games."""
    return [single_game(num_players) for _ in range(num_games)]


def multi_game_experiment(num_games, num_players, seeds):
    """Returns durations of a number of games when playing with given seed. """
    rd.seed(seeds)
    return multiple_games(num_games, num_players)


def median(data):
    """
    Returns median of data.

    :param data: An iterable of containing numbers
    :return: Median of data
    """

    s_data = sorted(data)
    n = len(s_data)
    return (s_data[n // 2] if n % 2 == 1
            else 0.5 * (s_data[n // 2 - 1] + s_data[n // 2]))


if __name__ == '__main__':
    number_of_games = 100
    number_of_players = 4
    seed = 5
    number_of_moves = multi_game_experiment(number_of_games,
                                            number_of_players,
                                            seed)
    print('The shortest game was {} moves'.format(min(number_of_moves)))
    print('The longest game was {} moves'.format(max(number_of_moves)))
    print(
        'The median of the games was {} games'.format(median(number_of_moves)))
    print('The average number of games was {} games'.format(
        np.average(number_of_moves)))
    print('the std of the games was {}'.format(np.std(number_of_moves)))
