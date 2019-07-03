#!/usr/bin/python3
"""Unittest for BaseModel"""
import unittest
from models.base_model import BaseModel
import pep8


class Test_pep8(unittest.TestCase):

    def test_pep8(self):
        pep = pep8.StyleGuide(quiet=True)
        f_base_model = "models/base_model.py"
        f_user = "models/user.py"
        f_file_storage = "models/engine/file_storage.py"
        check = style.check_files([f_base_model, f_user, f_file_storage])
        self.assertEqual(check.total_errors, 0,
                        "Found code style errors (and warning).")


class Test_BaseModel(unittest.TestCase):
    """Class that contains all tests for BaseModel"""

    def setUp(self):
        self.test1 = BaseModel()
        self.test1json = self.test1.to_dict()
        self.newtest1 = BaseModel(self.test1json)

    def tearDown(self):
        pass

    def test_date_created(self):
        with self.assertRaises(TypeError):
            BaseModel(created_at:"hola")
        with self.assertRaises(TypeError):
            BaseModel(created_at:3)

    def test_date_updated(self):
        with self.assertRaises(TypeError):
            BaseModel(updated_at:"hola")
        with self.assertRaises(TypeError):
            BaseModel(updated_at:3)

    def test_save(self):
        self.assertNotEqual(self.test1json, self.newtest1)

if __name__ == '__main__':
    unittest.main()
