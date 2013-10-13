import unittest

import tigreship

class TestPlayer:
    def __init__(self):
        self.target_called = False
        self.hit_called = False
        self.missed_called = False
        self.sunk_ship = None

    def target(self):
        self.target_called = True
        return 0, 0

    def hit(self, x, y):
        self.hit_called = True

    def missed(self, x, y):
        self.missed_called = True

    def sunk(self, ship):
        self.sunk_ship = ship

class TestGrid(tigreship.Grid):
    hits = None
    sunk_ship = None

    def fire(self, x, y):
        if TestGrid.hits is not None:
            return TestGrid.hits, TestGrid.sunk_ship
        else:
            return tigreship.Grid.fire(self, x, y)

    @classmethod
    def will_hit(cls, hits, ship=None):
        cls.hits = hits
        cls.sunk_ship = ship

class TigreshipTest(unittest.TestCase):
    def setUp(self):
        self.first_player = TestPlayer()
        self.second_player = TestPlayer()
        self.game = tigreship.Tigreship(self.first_player, self.second_player,
                                        grid=TestGrid)

    def test_first_player_asked_target(self):
        self.game.play_turn(0)
        self.assertTrue(self.first_player.target_called)

    def test_second_player_asked_target(self):
        self.game.play_turn(1)
        self.assertTrue(self.second_player.target_called)

    def test_hit(self):
        TestGrid.will_hit(True, None)
        self.game.play_turn(0)
        self.assertTrue(self.first_player.hit_called)

    def test_miss(self):
        TestGrid.will_hit(False)
        self.game.play_turn(0)
        self.assertTrue(self.first_player.missed_called)

    def test_sink(self):
        ship = tigreship.Ship('Test', 3)
        TestGrid.will_hit(True, ship)
        self.game.play_turn(0)
        self.assertEqual(ship, self.first_player.sunk_ship)

class GridTest(unittest.TestCase):
    def setUp(self):
        self.ship = tigreship.Ship('Test', 3)
        self.grid = tigreship.Grid()

    def test_place_outside_grid(self):
        placements = [(-1, 0, 'horizontal'),
                      (9, 0, 'horizontal'),
                      (0, -1, 'horizontal'),
                      (0, 11, 'horizontal'),
                      (-1, 0, 'vertical'),
                      (0, -1, 'vertical'),
                      (11, 0, 'vertical'),
                      (0, 9, 'vertical'),
                     ]
        for x, y, orientation in placements:
            self.assertFalse(self.grid.can_place(self.ship, x, y, orientation))

    def test_place_inside_grid(self):
        placements = [(0, 0, 'horizontal'),
                      (7, 0, 'horizontal'),
                      (0, 9, 'horizontal'),
                      (0, 0, 'vertical'),
                      (0, 7, 'vertical'),
                      (9, 0, 'vertical'),
                     ]
        for x, y, orientation in placements:
            self.assertTrue(self.grid.can_place(self.ship, x, y, orientation))

    def test_place_over(self):
        self.grid.place_ship(self.ship, 2, 2, 'horizontal')
        placements = [(0, 2, 'horizontal'),
                      (2, 2, 'horizontal'),
                      (4, 2, 'horizontal'),
                      (2, 0, 'vertical'),
                      (2, 2, 'vertical'),
                      (4, 0, 'vertical'),
                     ]
        for x, y, orientation in placements:
            self.assertFalse(self.grid.can_place(self.ship, x, y, orientation))

    def test_fire_hit(self):
        self.grid.place_ship(self.ship, 2, 2, 'horizontal')
        targets = [(2, 2), (3, 2), (4, 2)]
        for x, y in targets:
            hit, sunk_ship = self.grid.fire(x, y)
            self.assertTrue(hit)

    def test_fire_miss(self):
        self.grid.place_ship(self.ship, 2, 2, 'horizontal')
        targets = [(2, 1), (4, 1), (1, 2), (5, 2), (2, 3), (4, 3)]
        for x, y in targets:
            hit, sunk_ship = self.grid.fire(x, y)
            self.assertFalse(hit)
            self.assertIsNone(sunk_ship)

    def test_sink(self):
        self.grid.place_ship(self.ship, 2, 2, 'horizontal')
        hit, sunk_ship = self.grid.fire(2, 2)
        self.assertIsNone(sunk_ship)
        hit, sunk_ship = self.grid.fire(3, 2)
        self.assertIsNone(sunk_ship)
        hit, sunk_ship = self.grid.fire(4, 2)
        self.assertEqual(self.ship, sunk_ship)

    def test_all_sunk(self):
        self.grid.place_ship(self.ship, 2, 2, 'horizontal')
        hit, sunk_ship = self.grid.fire(2, 2)
        self.assertFalse(self.grid.all_sunk())
        hit, sunk_ship = self.grid.fire(3, 2)
        self.assertFalse(self.grid.all_sunk())
        hit, sunk_ship = self.grid.fire(4, 2)
        self.assertTrue(self.grid.all_sunk())

    def test_invalid_target(self):
        targets = [(-1, 0), (0, -1), (10, 0), (0, 10)]
        for x, y, in targets:
            hit, sunk_ship = self.grid.fire(x, y)
            self.assertFalse(hit)

if __name__ == '__main__':
    unittest.main()
