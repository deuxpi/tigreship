Tigreship
=========

[![Coverage Status](https://img.shields.io/coveralls/deuxpi/tigreship.svg)](https://coveralls.io/r/deuxpi/tigreship?branch=master) [![Build Status](https://travis-ci.org/deuxpi/tigreship.svg?branch=master)](https://travis-ci.org/deuxpi/tigreship)

Description
-----------

A simple game that allows two programs to compete in a game of [Battleship][1].

How to play
-----------

Write your own module that contains a Player class. A sample player code with
documentation is included in the `grotigre.py` file.

On the command line, following the name of the main script file, enter the
name of the modules that will define the first and second players. For example,
to let grotigre play against itself, type:

    python tigreship.py grotigre grotigre

Testing
-------

You can run the `tigreship_test.py` script directly or use [nosetests][2] for
nicer output.

License
-------

This software is distributed under the GNU Public License, version 3 or later.


[1]: https://en.wikipedia.org/wiki/Battleship_(game)
[2]: https://nose.readthedocs.org/en/latest/
