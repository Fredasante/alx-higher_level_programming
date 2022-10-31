#!/usr/bin/python3
"""Module Test_Square
Unittests to perform on the Square class
"""


import contextlib
import io
import unittest
from models.square import Square
from models.base import Base
import json


class TestSquare(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print('Square setUpClass')

    @classmethod
    def tearDownClass(cls):
        print('Square tearDownClass')

    def setUp(self):
        print('setUp')

    def tearDown(self):
        print('tearDown')

    def test_instance_id(self):
        rec = Square(10, 0, 0, 12)
        self.assertEqual(12, rec.id)

    def test_width_height_setters(self):
        with self.assertRaises(TypeError):
            x = Square()
        with self.assertRaises(TypeError):
            x = Square([9])
        with self.assertRaises(TypeError):
            x = Square('2')
        with self.assertRaises(ValueError):
            x = Square(-9)
        with self.assertRaises(TypeError):
            x = Square(None)
        with self.assertRaises(TypeError):
            x = Square(8.9)
        with self.assertRaises(ValueError):
            x = Square(0)
        with self.assertRaises(TypeError):
            x = Square(True)

        self.assertTrue(isinstance(Square(7), Square))

    def test_x_y(self):
        with self.assertRaises(TypeError):
            obj = Square(10, '8', 0)
        with self.assertRaises(TypeError):
            obj = Square(10, [8, 7])
        with self.assertRaises(ValueError):
            obj = Square(10, 9, -9)
        with self.assertRaises(TypeError):
            obj = Square(10, 8.9, 0)
        with self.assertRaises(TypeError):
            obj = Square(10, 7, 7.3)
        with self.assertRaises(ValueError):
            obj = Square(10, 0, -7)
        with self.assertRaises(TypeError):
            obj = Square(10, 7, '7')
        with self.assertRaises(TypeError):
            obj = Square(10, 9, None)
        with self.assertRaises(TypeError):
            obj = Square(10, None, 9)
        with self.assertRaises(TypeError):
            obj = Square(10, 9, True)
        with self.assertRaises(TypeError):
            obj = Square(10, True, 7)

        self.assertTrue(isinstance(Square(10, 7, 2), Square))

    def test_area(self):
        self.assertEqual(Square(3).area(), 9)
        self.assertEqual(Square(8, 0, 0, 12).area(), 64)

    def test_str(self):
        r1 = Square(4, 2, 1, 12)
        self.assertEqual(str(r1), "[Square] (12) 2/1 - 4")
        r1 = Square(5, 1, 0, 28)
        self.assertEqual(str(r1), "[Square] (28) 1/0 - 5")
        r1 = Square(9, 0, 0, 14)
        self.assertEqual(str(r1), "[Square] (14) 0/0 - 9")

    def test_update(self):
        r1 = Square(10, 10, 10, 10)
        r1.update(89)
        self.assertEqual(r1.id, 89)
        r1.update(89, 2)
        self.assertEqual(r1.size, 2)
        r1.update(89, 2, 3)
        self.assertEqual(r1.x, 3)
        r1.update(89, 2, 3, 4)
        self.assertEqual(r1.y, 4)

        r1.update(size=1)
        self.assertEqual(r1.size, 1)
        r1.update(sizeh=1, x=2)
        self.assertEqual(r1.size, 1)
        self.assertEqual(r1.x, 2)
        r1.update(y=1, size=2, x=3, id=23)
        self.assertEqual(r1.size, 2)
        self.assertEqual(r1.x, 3)
        self.assertEqual(r1.y, 1)
        self.assertEqual(r1.id, 23)

        r2 = Square(10, 10, 10, 10)
        r2.update(40, 3, 4, y=1, size=2, x=3, id=89)
        self.assertEqual(r2.size, 3)
        self.assertEqual(r2.x, 4)
        self.assertEqual(r2.y, 10)
        self.assertEqual(r2.id, 40)

    def test_display(self):
        f = io.StringIO()
        s1 = Square(2)
        with contextlib.redirect_stdout(f):
            s1.display()
        s1 = f.getvalue()
        self.assertEqual(s1, "##\n##\n")

        s2 = Square(3, 1, 3)
        x = io.StringIO()
        with contextlib.redirect_stdout(x):
            s2.display()
        s2 = x.getvalue()
        self.assertEqual(s2, "\n\n\n ###\n ###\n ###\n")

    def test_to_dict(self):
        s = Square(10, 2, 1, 18)
        res = {'id': 18, 'x': 2, 'size': 10, 'y': 1}
        self.assertEqual(s.to_dictionary(), res)

    def test_to_json_type(self):
        sq = Square(8)
        json_dict = sq.to_dictionary()
        json_string = Base.to_json_string([json_dict])
        self.assertEqual(type(json_string), str)

    def test_to_json_value(self):
        sq = Square(8, 0, 0, 18)
        json_dict = sq.to_dictionary()
        json_string = Base.to_json_string([json_dict])
        self.assertEqual(json.loads(json_string),
                         [{"id": 18, "y": 0, "size": 8, "x": 0}])

    def test_to_json_None(self):
        sq = Square(8, 0, 0, 18)
        json_dict = sq.to_dictionary()
        json_string = Base.to_json_string(None)
        self.assertEqual(json_string, "[]")

    def test_to_json_Empty(self):
        sq = Square(8, 0, 0, 18)
        json_dict = sq.to_dictionary()
        json_string = Base.to_json_string([])
        self.assertEqual(json_string, "[]")
