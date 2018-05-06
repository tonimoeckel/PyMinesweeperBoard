import unittest
from minesweeperboard import board


class BoardTest(unittest.TestCase):

    def testNotValid(self):
        input = ['AAAAAAA',
                 '# *  * #',
                 '#  *   #',
                 '#    * #',
                 '#   * *#',
                 '# *  * #',
                 '#      #',
                 '########']
        with self.assertRaises(ValueError) as context:
            board(input)

    def testNotSquare(self):
        input = ['AAAAAAA',
                 '# *  * #',
                 '#  *   #',
                 '#    * #',
                 '#   * *#',
                 '# *  * #',
                 '########']
        with self.assertRaises(ValueError) as context:
            board(input)

    def testBoard(self):
        input = ['########',
                 '# *  * #',
                 '#  *   #',
                 '#    * #',
                 '#   * *#',
                 '# *  * #',
                 '#      #',
                 '########']

        res = board(input)
        self.assertEqual(res, [
            '########',
            '#1*22*1#',
            '#12*322#',
            '# 123*2#',
            '#112*4*#',
            '#1*22*2#',
            '#111111#',
            '########'
        ])