#!/usr/bin/python3
"""Unittest for BaseModel"""
import unittest
from models.base_model import BaseModel
import pep8


class Test_pep8(unittest.TestCase):
    """Class that checks pep8 for all files"""

    def test_pep8(self):
        """Function that checks pep8"""
        pep = pep8.StyleGuide(quiet=True)
        f_base_model = "models/base_model.py"
        f_user = "models/user.py"
        f_file_storage = "models/engine/file_storage.py"
        check = pep.check_files([f_base_model, f_user, f_file_storage])
        self.assertEqual(check.total_errors, 0,
                         "Found code style errors (and warning).")


class Test_BaseModel(unittest.TestCase):
    """Class that contains all tests for BaseModel"""

    def setUp(self):
        """Set-up function, first to execute"""
        self.test1 = BaseModel()
        self.test1json = self.test1.to_dict()
        self.newtest1 = BaseModel(self.test1json)

    def tearDown(self):
        """Tear-down function, last to execute"""
        pass

    def test_new(self):
        """Test for new instances, checks for different dates"""
        self.assertNotEqual(self.test1json, self.newtest1)

    def test_save(self):
        """Test for save method, checks for different dates"""
        first = self.test1.updated_at
        self.test1.save()
        last = self.test1.updated_at
        self.assertNotEqual(first, last)

    def test_instance(self):
        """Test for instance creation of BaseModel"""
        self.assertIsInstance(self.test1, BaseModel)

    def test_dictionary(self):
        """Test for creation of dictionary"""
        self.assertIsInstance(self.test1json, dict)

if __name__ == '__main__':
    unittest.main()
