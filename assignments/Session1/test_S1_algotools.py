import unittest
import S1_algotools

class TestAlgoTools(unittest.TestCase):
    
    #Tests Exercise 1
    def test_average_above_zero_non_zeros_values(self):
        result = S1_algotools.average_above_zero([1,2,3,-5])
        self.assertEqual(result,2.0)
        
    def test_average_above_zero_with_zeros_values(self):
        result = S1_algotools.average_above_zero([1,2,3,0,-7])
        self.assertEqual(result,2.0)

    def test_average_above_zero_with_negative_values(self):
        with self.assertRaises(ValueError):
            S1_algotools.average_above_zero([0,-7])  

    def test_average_above_zero_with_string_values(self):
        with self.assertRaises(TypeError):
            S1_algotools.average_above_zero(['ab','c'])  

    def test_average_above_zero_with_empty_tab(self):
        with self.assertRaises(ValueError):
            S1_algotools.average_above_zero([])  