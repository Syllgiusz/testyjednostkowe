from unittest import TestCase
from pythonProject.zadanie1 import *
from pythonProject.zadanie1.zad1 import sumFileNumbers

class Test(TestCase):
    def test_sum_file_numbers(self):
        self.assertEqual(sumFileNumbers("file1"), 10)

    def empty_file(self):
        self.assertEqual(sumFileNumbers("file2"), 0)

    def file_doesnt_exist(self):
        with self.assertRaises(FileNotFoundError):
            self.assertEqual(sumFileNumbers("file3"))
