__author__ = 'Fabian Nemazi', 'Ahmed salaad Ahmed.'
__email__ = 'Salmaaah@nmbu.no', 'fabinema@nmbu.no'

import chutes_simulation as cs
import pytest

class TestBoard:
    """
    test for board class
    """
    def test_constructor(self):
        """
        making sure you cant give invalid ladders and chutes input
        """
        b = cs.Board()
        assert(b.ladders_and_snakes == {1: 40, 8: 10, 36: 52, 43: 62, 49: 79,
                                        65: 82, 68: 85, 24: 5, 33: 3,
                                        42: 30, 56: 37,
                                        64: 27, 74: 12, 87: 70})
        c = cs.Board(ladders=[(3, 4), (5, 6)], chutes=[(10, 3), (44, 2)])
        assert(c.ladders_and_snakes == {3: 4, 5: 6, 10: 3, 44: 2})

    def test_position_adjustment(self):
        """
        checks that the adjustment function gives out correct input
        """
        b = cs.Board()
        assert(b.position_adjustment(1) == 39)
        assert(b.position_adjustment(0) == 0)


class TestPlayer:
    """
    test for player class
    """
    def test_moves(self):
        """
        testing that the function works properly
        """
        b = cs.Board()
        p = cs.Player(b)
        for _ in range(5):
            p.move()
        assert(p.moves == 5)
        assert(p.position > 0)


class TestResilientPlayer:
    """
    test for resilient player class
    """
    def test_move(self):
        """
        checks that the extra step is in play, if extra steps is 6
        the player cant have moved shorter than to step 7.
        First chute starts at 5, therefore after first move
        the player must minimum be at 7
        """
        b = cs.Board()
        p = cs.ResilientPlayer(b, extra_steps = 6)
        p.move()
        first_pos = p.position
        assert(first_pos >= 7)


class TestLazyPlayer:
    """
    test for lazy player class
    """
    def test_move(self):
        """
        testing that the move function works properly
        """
        b = cs.Board(ladders=[(40, 55), (10, 22)], chutes=[(33, 10), (44, 2)])
        p = cs.LazyPlayer(b, dropped_steps=4)
        p.move()
        assert(0 <= p.position <= 2)
        p.move()
        assert(0 <= p.position <= 4)
        p.move()
        assert( 0 <= p.position <= 6)

class TestSimulation:
    """
    Test for simulation class
    """

    def test_single_game(self):
        """checking that the function returns a tuple"""
        s = cs.Simulation([cs.Player, cs.Player])
        assert(type(s.single_game()) == tuple)

    def test_run_simulation(self):
        """checking that the size of the list is correct"""
        s = cs.Simulation([cs.Player, cs.Player])
        s.run_simulation(10)
        assert(len(s.results) == 10)

    def test_get_results(self):
        """checking if we get output of results"""
        s = cs.Simulation([cs.Player, cs.Player])
        s.run_simulation(10)
        assert(s.results != None)

    def test_winners_per_type(self):
        """checking if we have different winners in the simulation"""
        s = cs.Simulation([cs.Player, cs.LazyPlayer, cs.ResilientPlayer])
        s.run_simulation(50)
        assert(type(s.winners_per_type()) == dict)
        winners = s.winners_per_type()
        assert(winners.get('Player') > 0 )
        assert(winners.get('LazyPlayer') > 0)
        assert(winners.get('ResilientPlayer'))

    def test_durations_per_type(self):
        s = cs.Simulation([cs.Player, cs.LazyPlayer, cs.ResilientPlayer])
        s.run_simulation(10)
        w = s.durations_per_type()
        for x in w.keys():
            assert(x)

    def test_players_per_type(self):
        """test_base has already tested the essential in this func"""
        s = cs.Simulation([cs.Player, cs.LazyPlayer, cs.ResilientPlayer])
        p = s.players_per_type()

        assert all(v >= 0 for v in p.values())


















