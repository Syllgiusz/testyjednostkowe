from unittest import TestCase
from pythonProject.zadanie2.zad2 import *

class TestUczenSchema(TestCase):
    def serializeNormalTest(self):
        #given
        uczen = dict(name='Jan', secondName='Kowalski', mail='jan@example.test', birthDate=date(2024, 3, 12))

        #then
        result = Serialization(UczenSchema(), uczen)
        self.assertEqual(result["name"], "Jan")
        self.assertEqual(result["secondName"], "secondName")
        self.assertEqual(result["mail"], "jan@example.test")
        self.assertEqual(result["birthDate"], "2024-03-12")

    def emptyDictSerializeTest(self):
        # given
        uczen = dict(name='Jan', mail='jan@example.test', birthDate=date(2024, 3, 12))

        # then
        result = Serialization(UczenSchema(), uczen)
        with self.assertRaises(ValueError):
            self.assertEqual(result["name"], "Jan")
            self.assertEqual(result["mail"], "jan@example.test")
            self.assertEqual(result["birthDate"], "2024-03-12")