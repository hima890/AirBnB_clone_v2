#!/usr/bin/python3
"""Defines unittests for console.py.
Unittest classes:
    TestHBNBCommand_prompting
    TestHBNBCommand_help
    TestHBNBCommand_exit
    TestHBNBCommand_create
    TestHBNBCommand_show
    TestHBNBCommand_all
    TestHBNBCommand_destroy
    TestHBNBCommand_update
"""
import os
import sys
import unittest
from unittest.mock import patch
from io import StringIO
from console import HBNBCommand
from models import storage
from models.base_model import BaseModel
from models.user import User


class TestHBNBCommand(unittest.TestCase):
    def setUp(self):
        """Set up the test environment"""
        storage._FileStorage__objects = {}

    def tearDown(self):
        """Clean up the test environment"""
        storage._FileStorage__objects = {}

    @patch('sys.stdout', new_callable=StringIO)
    def test_help(self, mock_stdout):
        """Test the help command"""
        HBNBCommand().onecmd("help")
        self.assertIn("Documented commands", mock_stdout.getvalue())

    @patch('sys.stdout', new_callable=StringIO)
    def test_create(self, mock_stdout):
        """Test create command"""
        HBNBCommand().onecmd("create User")
        self.assertTrue(len(mock_stdout.getvalue().strip()) > 0)

    @patch('sys.stdout', new_callable=StringIO)
    def test_show(self, mock_stdout):
        """Test show command"""
        new_user = User()
        new_user.save()
        HBNBCommand().onecmd(f"show User {new_user.id}")
        self.assertIn(new_user.id, mock_stdout.getvalue())

    @patch('sys.stdout', new_callable=StringIO)
    def test_destroy(self, mock_stdout):
        """Test destroy command"""
        new_user = User()
        new_user.save()
        HBNBCommand().onecmd(f"destroy User {new_user.id}")
        self.assertNotIn(new_user.id, storage.all())

    @patch('sys.stdout', new_callable=StringIO)
    def test_all(self, mock_stdout):
        """Test all command"""
        new_user = User()
        new_user.save()
        HBNBCommand().onecmd("all User")
        self.assertIn(new_user.id, mock_stdout.getvalue())

    @patch('sys.stdout', new_callable=StringIO)
    def test_update(self, mock_stdout):
        """Test update command"""
        new_user = User()
        new_user.save()
        HBNBCommand().onecmd(f'update User {new_user.id} first_name "John"')
        self.assertEqual(new_user.first_name, "John")

    @patch('sys.stdout', new_callable=StringIO)
    def test_show_missing_class(self, mock_stdout):
        """Test show command with missing class name"""
        HBNBCommand().onecmd("show")
        self.assertIn("** class name missing **", mock_stdout.getvalue())

    @patch('sys.stdout', new_callable=StringIO)
    def test_show_invalid_class(self, mock_stdout):
        """Test show command with invalid class name"""
        HBNBCommand().onecmd("show InvalidClass")
        self.assertIn("** class doesn't exist **", mock_stdout.getvalue())

    @patch('sys.stdout', new_callable=StringIO)
    def test_show_missing_id(self, mock_stdout):
        """Test show command with missing id"""
        HBNBCommand().onecmd("show User")
        self.assertIn("** instance id missing **", mock_stdout.getvalue())

    @patch('sys.stdout', new_callable=StringIO)
    def test_show_invalid_id(self, mock_stdout):
        """Test show command with invalid id"""
        HBNBCommand().onecmd("show User invalid_id")
        self.assertIn("** no instance found **", mock_stdout.getvalue())

    @patch('sys.stdout', new_callable=StringIO)
    def test_destroy_missing_class(self, mock_stdout):
        """Test destroy command with missing class name"""
        HBNBCommand().onecmd("destroy")
        self.assertIn("** class name missing **", mock_stdout.getvalue())

    @patch('sys.stdout', new_callable=StringIO)
    def test_destroy_invalid_class(self, mock_stdout):
        """Test destroy command with invalid class name"""
        HBNBCommand().onecmd("destroy InvalidClass")
        self.assertIn("** class doesn't exist **", mock_stdout.getvalue())

    @patch('sys.stdout', new_callable=StringIO)
    def test_destroy_missing_id(self, mock_stdout):
        """Test destroy command with missing id"""
        HBNBCommand().onecmd("destroy User")
        self.assertIn("** instance id missing **", mock_stdout.getvalue())

    @patch('sys.stdout', new_callable=StringIO)
    def test_destroy_invalid_id(self, mock_stdout):
        """Test destroy command with invalid id"""
        HBNBCommand().onecmd("destroy User invalid_id")
        self.assertIn("** no instance found **", mock_stdout.getvalue())

    @patch('sys.stdout', new_callable=StringIO)
    def test_update_missing_class(self, mock_stdout):
        """Test update command with missing class name"""
        HBNBCommand().onecmd("update")
        self.assertIn("** class name missing **", mock_stdout.getvalue())

    @patch('sys.stdout', new_callable=StringIO)
    def test_update_invalid_class(self, mock_stdout):
        """Test update command with invalid class name"""
        HBNBCommand().onecmd("update InvalidClass")
        self.assertIn("** class doesn't exist **", mock_stdout.getvalue())

    @patch('sys.stdout', new_callable=StringIO)
    def test_update_missing_id(self, mock_stdout):
        """Test update command with missing id"""
        HBNBCommand().onecmd("update User")
        self.assertIn("** instance id missing **", mock_stdout.getvalue())

    @patch('sys.stdout', new_callable=StringIO)
    def test_update_invalid_id(self, mock_stdout):
        """Test update command with invalid id"""
        HBNBCommand().onecmd("update User invalid_id")
        self.assertIn("** no instance found **", mock_stdout.getvalue())


if __name__ == '__main__':
    unittest.main()
