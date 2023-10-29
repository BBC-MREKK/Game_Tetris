import unittest
import tkinter as tk
from main import Tetris, Application

class TestTetrisIntegration(unittest.TestCase):
    def setUp(self):
        self.root = tk.Tk()
        self.app = Application(master=self.root)
    
    def tearDown(self):
        self.root.destroy()

    def test_tetris_initialization(self):
        tetris = self.app.tetris
        self.assertEqual(tetris.score, 0)
        self.assertEqual(tetris.level, 0)
        self.assertEqual(tetris.total_lines_eliminated, 0)
        self.assertFalse(tetris.game_over)
        self.assertIsNotNone(tetris.tetromino)

    def test_tetris_move_and_rotate(self):
        tetris = self.app.tetris
        initial_tetromino_coords = tetris.get_tetromino_coords()
        initial_tetromino_offset = tetris.tetromino_offset

        tetris.move(1, 0)
        self.assertNotEqual(tetris.get_tetromino_coords(), initial_tetromino_coords)
        self.assertNotEqual(tetris.tetromino_offset, initial_tetromino_offset)

        tetris.rotate()
        self.assertNotEqual(tetris.get_tetromino_coords(), initial_tetromino_coords)
        self.assertNotEqual(tetris.tetromino_offset, initial_tetromino_offset)

    def test_game_over_and_reset(self):
        tetris = self.app.tetris
        tetris.game_over = True
        initial_tetromino_coords = tetris.get_tetromino_coords()
        initial_tetromino_offset = tetris.tetromino_offset

        tetris.move(1, 0)
        tetris.rotate()
        self.assertEqual(tetris.get_tetromino_coords(), initial_tetromino_coords)
        self.assertEqual(tetris.tetromino_offset, initial_tetromino_offset)

        tetris.reset_tetromino()
        self.assertFalse(tetris.game_over)
        self.assertNotEqual(tetris.get_tetromino_coords(), initial_tetromino_coords)
        self.assertNotEqual(tetris.tetromino_offset, initial_tetromino_offset)

if __name__ == '__main__':
    unittest.main()