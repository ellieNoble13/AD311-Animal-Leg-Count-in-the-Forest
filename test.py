from animalCount import countLegs
import unittest

class TestAnimalCount(unittest.TestCase):
    def test_countLegs(self):
        animals = ['frog', 'horse', 'spider', 'ant']
        self.assertEqual(countLegs(animals), 1)

    def test_countLegs2(self):
        animals =['lion', 'monkey', 'deer', 'snake', 'elephant']
        self.assertEqual(countLegs(animals), 3)

    def test_countLegs3(self):
        animals = ['elephant']
        self.assertEqual(countLegs(animals), 1)

    def test_countLegsEdge1(self):
        animals = []
        self.assertEqual(countLegs(animals), 0)

    def test_countLegsEdge2(self):
        animals = ['SNAKE', 'deEr', 'DOG', 'cAT']
        self.assertEqual(countLegs(animals), 3)

    def test_countLegsEdge3(self):
        animals = ['elephant', 'elephant', 'elephant', 'elephant', 'elephant']
        self.assertEqual(countLegs(animals), 5)