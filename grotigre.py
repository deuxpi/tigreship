import random


class Player:
    def place_ship(self, ship):
        """Returns the coordinates and orientation of a ship to be placed on
        the game grid. This method will be called repeatedly with the same
        arguments if the ship cannot be placed at the requested position.

        The `ship` argument contains an object with name and a length
        attibutes.

        The returned value is a tuple composed of the horizontal and vertical
        indices and a string that specifies the orientation."""
        x = random.randint(0, 9)
        y = random.randint(0, 9)
        orientation = random.choice(['vertical', 'horizontal'])
        return x, y, orientation

    def target(self):
        """Returns the grid coordinates of the next guess. If the coordinates
        are outside the grid, the player will lose this turn. Depending on the
        outcome of the guess, the hit() or missed() method will be called."""
        return random.randint(0, 9), random.randint(0, 9)

    def hit(self, x, y):
        """Called in response to a successful guess returned from the target()
        method."""
        pass

    def missed(self, x, y):
        """Called in response to a failed guess returned from the target()
        method."""
        pass

    def sunk(self, ship):
        """Called following hit() in response to a guess that sunk a ship of
        the opposing player."""
        pass
