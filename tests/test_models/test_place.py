#!/usr/bin/python3
"""Unittest for Place"""
import unittest
import models
import pep8

BaseModel = models.base_model.BaseModel
Place = models.amenity.Amenity

class TestDocumentation(unittest.TestCase):
    """Check for existence of documentation"""

    def test_doc1(self):
        """Check documentation in module"""
        assert models.place.__doc__ is not None

    def test_doc2(self):
        """Check documentation in class"""
        assert Place.__doc__ is not None

    def test_doc3(self):
        """Check documentation in methods"""
        methods = ["__init__", "__str__", "to_dict", "save"]
        for key in Place.__dict__.keys():
            if key in methods:
                assert key.__doc__ is not None


class TestBaseModel(unittest.TestCase):
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

    def test_creation1(self):
        """Test to verify creation of attributes - name"""
        self.test1.name = "Holberton"
        self.assertEqual(self.test1.name, "Holberton")

    def test_creation2(self):
        """Test to verify creation of attributes - number"""
        self.test1.number = 89
        self.assertEqual(self.test1.number, 89)

    def test_attributes(self):
        """Test the creation of attributes in init"""
        comp = str(self.test1)
        attr = ['BaseModel', 'id', 'created_at', 'updated_at']
        counter = 0
        for a in attr:
            if a in attr:
                counter += 1
        self.assertTrue(counter == 4)

if __name__ == '__main__':
    unittest.main()
