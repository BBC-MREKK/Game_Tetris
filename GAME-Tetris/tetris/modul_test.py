import unittest
from main import Tetris

class TestTetris(unittest.TestCase):
    def test_game_over(self):
        tetris = Tetris()
        self.assertFalse(tetris.is_game_over())

        tetris.field[0][0] = 1
        tetris.set_tetromino([(0, 0)], 2, [0, 0])
        self.assertTrue(tetris.is_game_over())

    def test_score_and_level(self):
        tetris = Tetris()
        self.assertEqual(tetris.get_score(), 0)
        self.assertEqual(tetris.get_level(), 0)

        tetris.apply_tetromino()
        self.assertEqual(tetris.get_score(), 0)
        self.assertEqual(tetris.get_level(), 0)

        tetris.total_lines_eliminated = 10
        tetris.apply_tetromino()
        self.assertEqual(tetris.get_score(), 400)
        self.assertEqual(tetris.get_level(), 1)

    def test_move(self):
        tetris = Tetris()
        tetris.move(1, 0)
        self.assertEqual(tetris.get_tetromino_coords(), [(0, 3), (0, 4), (1, 3), (1, 4)])

    def test_rotate(self):
        tetris = Tetris()
        tetris.rotate()
        self.assertNotEqual(tetris.get_tetromino_coords(), [(0, 0), (0, 1), (1, 1), (2, 1)])

if __name__ == '__main__':
    unittest.main()