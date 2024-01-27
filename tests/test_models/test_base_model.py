#!/usr/bin/python3
"""Test BaseModel for expected behavior and documentation"""
from datetime import datetime
import inspect
import models
import pep8 as pycodestyle
import time
import unittest
from unittest import mock
from models.base_model import BaseModel
BaseModel = models.base_model.BaseModel
module_doc = models.base_model.__doc__

class TestBaseModelDocs(unittest.TestCase):
	"""Tests to check the documentation and style of BaseModel class"""

	@classmethod
	def setUpClass(self):
		"""Set up for docstring tests"""
		self.base_funcs = inspect.getmembers(BaseModel, inspect.isfunction)
	
	def test_pep8_conformance(self):
		"""Test that models/base_model.py conforms to PEP8."""
		for path in ['models/base_model.py',
			'tests/test_models/test_base_model.py']:
			with self.subTest(path=path):
				errors = pycodestyle.Checker(path).check_all()
				self.assertEqual(errors, 0)