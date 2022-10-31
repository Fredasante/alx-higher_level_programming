#!/usr/bin/python3
"""Test_Base Module
Perform unittests on our Base class.
"""


import unittest
from models.base import Base
from models.square import Square
from models.rectangle import Rectangle
import os.path


class TestBase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("Base setUpClass")

    @classmethod
    def tearDownClass(cls):
        print("Base tearDownClass")

    def setUp(self):
        Base._Base__nb_objects = 0
        print("Base setUp")

    def tearDown(self):
        print("Base tearDown")

    def test_instance_id(self):
        b1 = Base()
        b2 = Base()
        b3 = Base(9)
        b4 = Base()
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)
        self.assertEqual(b3.id, 9)
        self.assertEqual(b4.id, 3)
        self.assertEqual(Base("Betty").id, "Betty")
        self.assertEqual(Base([1, 2, 3]).id, [1, 2, 3])
        self.assertEqual(Base({"id": 89}).id, {"id": 89})
        self.assertEqual(Base((7,)).id, (7,))

    def test_to_json_string(self):
        obj = {'x': 2, 'width': 10, 'id': 1, 'height': 7, 'y': 8}
        json_str = Base.to_json_string([obj])
        self.assertTrue(str, type(json_str))
        res = '[{"x": 2, "width": 10, "id": 1, "height": 7, "y": 8}]'
        self.assertCountEqual(json_str, res)

        json_str2 = Base.to_json_string([])
        self.assertEqual(json_str2, '[]')

        json_str3 = Base.to_json_string(None)
        self.assertEqual(json_str3, '[]')
        with self.assertRaises(TypeError):
            j = Base.to_json_string()

    def test_save_to_file(self):
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        Rectangle.save_to_file([r1, r2])

        with open("Rectangle.json", "r") as file:
            x = (file.read())
        res = ('[{"y": 8, "x": 2, "id": 1, "width": 10, "height": 7},' +
               ' {"y": 0, "x": 0, "id": 2, "width": 2, "height": 4}]')
        self.assertEqual(len(x), len(res))

        Rectangle.save_to_file(None)
        res = "[]"
        with open("Rectangle.json", "r") as f:
            self.assertEqual(f.read(), res)

        r1 = Square(10, 7, 2, 8)
        r2 = Square(2, 4, 0, 18)
        Square.save_to_file([r1, r2])

        with open("Square.json", "r") as file:
            x = (file.read())
        res1 = ('[{"y": 2, "x": 7, "id": 8, "size": 10}, ' +
                '{"y": 0, "x": 4, "id": 18, "size": 2}]')
        self.assertEqual(len(x), len(res1))

        Square.save_to_file(None)
        res = "[]"
        with open("Square.json", "r") as f:
            self.assertEqual(f.read(), res)

        with self.assertRaises(AttributeError) as x:
            Base.save_to_file([Base(9), Base(5)])
        self.assertEqual(
            "'Base' object has no attribute 'to_dictionary'", str(
                x.exception))
        with self.assertRaises(AttributeError) as x:
            Rectangle.save_to_file([3, 4])
        self.assertEqual(
            "'int' object has no attribute 'to_dictionary'", str(
                x.exception))
        with self.assertRaises(TypeError) as x:
            Rectangle.save_to_file(5)
        self.assertEqual(
            "'int' object is not iterable", str(
                x.exception))
        s1 = ("save_to_file() missing 1 required" +
              " positional argument: 'list_objs'")
        with self.assertRaises(TypeError) as x:
            Rectangle.save_to_file()
        self.assertEqual(s1, str(x.exception))
        s2 = ("save_to_file() takes 2 positional" +
              " arguments but 3 were given")
        with self.assertRaises(TypeError) as x:
            Rectangle.save_to_file([Rectangle(9, 4), Rectangle(8, 9)], 98)
        self.assertEqual(s2, str(x.exception))

    def test_from_json_str(self):
        list_input = [
            {'id': 89, 'width': 10, 'height': 4},
            {'id': 7, 'width': 1, 'height': 7}
        ]
        json_list_input = Rectangle.to_json_string(list_input)
        list_output = Rectangle.from_json_string(json_list_input)
        res = [{'width': 10, 'height': 4, 'id': 89},
               {'width': 1, 'height': 7, 'id': 7}]
        self.assertCountEqual(list_output, res)
        self.assertEqual(type(list_output), list)

        list_output = Rectangle.from_json_string(None)
        self.assertEqual(list_output, [])

        with self.assertRaises(TypeError):
            list_output = Rectangle.from_json_string([8, 9])
        with self.assertRaises(TypeError):
            list_output = Rectangle.from_json_string(8)
        with self.assertRaises(TypeError):
            list_output = Rectangle.from_json_string(9.6)
        with self.assertRaises(TypeError):
            list_output = Rectangle.from_json_string((4, 5))
        with self.assertRaises(TypeError):
            list_output = Rectangle.from_json_string({1: 'Hello', 2: 'Hi'})
        with self.assertRaises(TypeError):
            Rectangle.from_json_string()

    def test_create(self):
        q1 = Rectangle(3, 5)
        q1_dictionary = q1.to_dictionary()
        q2 = Rectangle.create(**q1_dictionary)
        self.assertEqual(str(q1), str(q2))
        self.assertFalse(q1 is q2)
        self.assertFalse(q1 == q2)
        p1 = Square(3)
        p1_dictionary = p1.to_dictionary()
        p2 = Square.create(**p1_dictionary)
        self.assertEqual(str(p1), str(p2))
        self.assertFalse(p1 is p2)
        self.assertFalse(p1 == p2)

        with self.assertRaises(TypeError):
            r1 = "Hello"
            r2 = Rectangle.create(r1)

    def test_load_from_file(self):
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        list_rectangles_input = [r1, r2]

        Rectangle.save_to_file(list_rectangles_input)
        list_rectangles_output = Rectangle.load_from_file()
        for x in zip(list_rectangles_input, list_rectangles_output):
            self.assertEqual(str(x[0]), str(x[1]))

        s1 = Square(10, 2)
        s2 = Square(9)
        list_squares_input = [s1, s2]

        Square.save_to_file(list_squares_input)
        list_squares_output = Square.load_from_file()
        for x in zip(list_squares_input, list_squares_output):
            self.assertEqual(str(x[0]), str(x[1]))

        with self.assertRaises(TypeError):
            list_rectangles_output = Rectangle.load_from_file("Hello")

        if os.path.exists("Rectangle.json"):
            os.remove("Rectangle.json")
        if os.path.exists("Square.json"):
            os.remove("Square.json")
        if os.path.exists("Base.json"):
            os.remove("Base.json")
        list_rectangles_output = Rectangle.load_from_file()
        self.assertEqual(list_rectangles_output, [])
        list_squares_output = Square.load_from_file()
        self.assertEqual(list_squares_output, [])
