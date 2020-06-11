"""wargame.test.test_wargame

This module contains unit tests for various modules in wargame package.

This module is compatible with Python 3.5.x. It contains
supporting code for the book, Learning Python Application Development,
Packt Publishing.

:copyright: 2016, Ninad Sathaye

:license: The MIT License (MIT) . See LICENSE file for further details.
"""

from __future__ import print_function
import sys

if sys.version_info < (3, 0):
    print("This code requires Python 3.x and is tested with version 3.5.x ")
    print("Looks like you are trying to run this using "
          "Python version: %d.%d " % (sys.version_info[0],
                                      sys.version_info[1]))
    print("Exiting...")
    sys.exit(1)

# Add the top level directory wargame to sys.path
sys.path.append("../")
import unittest
from unittest import mock

from knight import Knight
from orcrider import OrcRider
from abstractgameunit import AbstractGameUnit
from gameutils import weighted_random_selection
from hut import Hut
from attackoftheorcs import AttackOfTheOrcs

class TestWarGame(unittest.TestCase):
    """This class contains unit tests for the game Attack of The Orcs."""

    def setUp(self):
        """Overrides the setUp fixture of the superclass."""
        self.knight = Knight()
        self.enemy = OrcRider()

    @unittest.skip("Skipping test_injured_unit_selection")
    def test_injured_unit_selection(self):
        """Unit tests to verify working of weighted_random_selection()."""
        for i in range(100):
            injured_unit = weighted_random_selection(self.knight, self.enemy)
            
            self.assertIsInstance(
                injured_unit, 
                AbstractGameUnit,
                "Injured unit must be an instance of AbstractGameUnit")
        
    def test_acquire_hut(self):
        """Unittest to verify hut occupant after is acquired.
        
        Unit test to ensure that when hut is 'acquired', the 'hut.occupant' 
        is updated to the 'Knight' instance
        """

        print("\nCalling test_hut.test_acquire_hut..")
        hut = Hut(4, None)
        hut.acquire(self.knight)
        self.assertIs(hut.occupant, self.knight)
        

if __name__ == "__main__":
    unittest.main()