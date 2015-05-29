from __future__ import print_function
from collections import namedtuple
import sys

Ship = namedtuple('Ship', ['name', 'length'])
SHIPS = [
    Ship('Aircraft Carrier', 5),
    Ship('Battleship', 4),
    Ship('Submarine', 3),
    Ship('Destroyer', 3),
    Ship('Patrol Boat', 2),
    ]


class Grid:
    def __init__(self):
        self.grid = [[None for i in range(10)] for j in range(10)]

    def place_ship(self, ship, x, y, orientation):
        if orientation not in ['vertical', 'horizontal']:
            return False
        if not self.can_place(ship, x, y, orientation):
            return False
        for i in range(ship.length):
            self.grid[x][y] = ship
            if orientation == 'horizontal':
                x += 1
            elif orientation == 'vertical':
                y += 1
        return True

    def can_place(self, ship, x, y, orientation):
        for i in range(ship.length):
            if x < 0 or x >= 10:
                return False
            if y < 0 or y >= 10:
                return False
            if self.grid[x][y] is not None:
                return False
            if orientation == 'horizontal':
                x += 1
            elif orientation == 'vertical':
                y += 1
            else:
                return False
        return True

    def sunk(self, ship):
        for x in range(10):
            for y in range(10):
                if self.grid[x][y] == ship:
                    return False
        return True

    def fire(self, x, y):
        if x < 0 or x > 9 or y < 0 or y > 9:
            return False, None
        ship = self.grid[x][y]
        hit = ship is not None
        self.grid[x][y] = None
        if hit and self.sunk(ship):
            return True, ship
        return hit, None

    def all_sunk(self):
        for x in range(10):
            for y in range(10):
                if self.grid[x][y] is not None:
                    return False
        return True


class Tigreship:
    def __init__(self, first_player, second_player, grid=Grid):
        self.players = [first_player, second_player]
        self.grids = [grid(), grid()]

    def start(self):
        self.setup()
        turn = 0
        while True:
            self.play_turn(turn)
            if self.winning(turn):
                break
            turn = 1 - turn
        print("Player %d won!" % (turn + 1))

    def setup(self):
        for player, grid in zip(self.players, self.grids):
            for ship in SHIPS:
                while True:
                    x, y, orientation = player.place_ship(ship)
                    if grid.place_ship(ship, x, y, orientation):
                        break

    def play_turn(self, turn):
        player = self.players[turn]
        grid = self.grids[1 - turn]
        x, y = player.target()
        print("Player %d fires at %s-%d" % (turn + 1, chr(x + 65), y + 1))
        hit, sunk_ship = grid.fire(x, y)
        if hit:
            player.hit(x, y)
            if sunk_ship:
                print("Player %d sunk a %s" % (turn + 1, sunk_ship.name))
                player.sunk(sunk_ship)
        else:
            player.missed(x, y)

    def winning(self, turn):
        return self.grids[1 - turn].all_sunk()


def main():
    if len(sys.argv) < 3:
        print("Usage: %s PLAYER1 PLAYER2" % sys.argv[0])
        sys.exit(1)
    first_player = __import__(sys.argv[1]).Player()
    second_player = __import__(sys.argv[2]).Player()
    game = Tigreship(first_player, second_player)
    game.start()

if __name__ == '__main__': # pragma: no cover
    main()
