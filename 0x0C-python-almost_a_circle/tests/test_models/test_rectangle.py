#!/usr/bin/python3
"""Module Test_Rectangle
Unittests to perform on the Rectangle class
"""


import io
import contextlib
import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print('Rectangle setUpClass')

    @classmethod
    def tearDownClass(cls):
        print('Rectangle tearDownClass')

    def setUp(self):
        print('setUp')

    def tearDown(self):
        print('tearDown')

    def test_instance_id(self):
        rec = Rectangle(10, 2, 0, 0, 12)
        self.assertEqual(12, rec.id)

    def test_width_height_setters(self):
        with self.assertRaises(TypeError):
            x = Rectangle()
        with self.assertRaises(TypeError):
            x = Rectangle(10)
        with self.assertRaises(TypeError):
            x = Rectangle([9, 2])
        with self.assertRaises(TypeError):
            x = Rectangle('2', 8)
        with self.assertRaises(ValueError):
            x = Rectangle(-9, 2)
        with self.assertRaises(ValueError):
            x = Rectangle(8, -8)
        with self.assertRaises(TypeError):
            x = Rectangle(78, None)
        with self.assertRaises(TypeError):
            x = Rectangle(8, '3')
        with self.assertRaises(TypeError):
            x = Rectangle(None, 89)
        with self.assertRaises(TypeError):
            x = Rectangle(8.9, 9)
        with self.assertRaises(TypeError):
            x = Rectangle(8, 9.2)
        with self.assertRaises(ValueError):
            x = Rectangle(0, 9)
        with self.assertRaises(ValueError):
            x = Rectangle(9, 0)
        with self.assertRaises(TypeError):
            x = Rectangle(9, True)
        with self.assertRaises(TypeError):
            x = Rectangle(True, 8)

        self.assertTrue(isinstance(Rectangle(7, 9), Rectangle))

    def test_x_y(self):
        with self.assertRaises(TypeError):
            obj = Rectangle(10, 9, '8', 0)
        with self.assertRaises(TypeError):
            obj = Rectangle(10, 9, [8, 7])
        with self.assertRaises(ValueError):
            obj = Rectangle(10, 9, -9)
        with self.assertRaises(TypeError):
            obj = Rectangle(10, 9, 8.9, 0)
        with self.assertRaises(TypeError):
            obj = Rectangle(10, 9, 7, 7.3)
        with self.assertRaises(ValueError):
            obj = Rectangle(10, 9, 0, -7)
        with self.assertRaises(TypeError):
            obj = Rectangle(10, 9, 7, '7')
        with self.assertRaises(TypeError):
            obj = Rectangle(10, 9, None)
        with self.assertRaises(TypeError):
            obj = Rectangle(10, 9, 7, None)
        with self.assertRaises(TypeError):
            obj = Rectangle(10, 9, True)
        with self.assertRaises(TypeError):
            obj = Rectangle(10, 9, 7, True)

        self.assertTrue(isinstance(Rectangle(10, 9, 7, 2), Rectangle))

    def test_area(self):
        self.assertEqual(Rectangle(3, 2).area(), 6)
        self.assertEqual(Rectangle(8, 7, 0, 0, 12).area(), 56)

    def test_str(self):
        r1 = Rectangle(4, 6, 2, 1, 12)
        self.assertEqual(str(r1), "[Rectangle] (12) 2/1 - 4/6")
        r1 = Rectangle(5, 5, 1, 0, 28)
        self.assertEqual(str(r1), "[Rectangle] (28) 1/0 - 5/5")
        r1 = Rectangle(9, 8, 0, 0, 14)
        self.assertEqual(str(r1), "[Rectangle] (14) 0/0 - 9/8")

    def test_update(self):
        r1 = Rectangle(10, 10, 10, 10)
        r1.update(89)
        self.assertEqual(r1.id, 89)
        r1.update(89, 2)
        self.assertEqual(r1.width, 2)
        r1.update(89, 2, 3)
        self.assertEqual(r1.height, 3)
        r1.update(89, 2, 3, 4)
        self.assertEqual(r1.x, 4)
        r1.update(89, 2, 3, 4, 5)
        self.assertEqual(r1.y, 5)
        r1.update(height=1)
        self.assertEqual(r1.height, 1)
        r1.update(width=1, x=2)
        self.assertEqual(r1.width, 1)
        self.assertEqual(r1.x, 2)
        r1.update(y=1, width=2, x=3, id=23)
        self.assertEqual(r1.width, 2)
        self.assertEqual(r1.x, 3)
        self.assertEqual(r1.y, 1)
        self.assertEqual(r1.id, 23)

        r2 = Rectangle(10, 10, 10, 10)
        r2.update(40, 3, 4, y=1, width=2, x=3, id=89)
        self.assertEqual(r2.width, 3)
        self.assertEqual(r2.height, 4)
        self.assertEqual(r2.x, 10)
        self.assertEqual(r2.y, 10)
        self.assertEqual(r2.id, 40)

    def test_display(self):
        f = io.StringIO()
        s1 = Rectangle(2, 2)
        with contextlib.redirect_stdout(f):
            s1.display()
        s1 = f.getvalue()
        self.assertEqual(s1, "##\n##\n")

        s2 = Rectangle(3, 2, 3, 1)
        x = io.StringIO()
        with contextlib.redirect_stdout(x):
            s2.display()
        s2 = x.getvalue()
        self.assertEqual(s2, "\n   ###\n   ###\n")

    def test_to_dict(self):
        r1 = Rectangle(10, 2, 1, 9, 30)
        res = {'x': 1, 'y': 9, 'id': 30, 'height': 2, 'width': 10}
        self.assertEqual(r1.to_dictionary(), res)
