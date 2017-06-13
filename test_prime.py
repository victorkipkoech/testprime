import unittest

from prime_number import get_prime_numbers

class TestForPrime(unittest.TestCase):
    def test_if_int(self):
        with self.assertRaises(TypeError):
            get_prime_numbers ('success')

    def test_if_all_prime(self):
       result =get_prime_numbers(10)
       self.assertEqual(result,[2,3,5,7],msg="value not prime")

    def test_if_list(self):
        self.assertTrue(type(get_prime_numbers(10))==list,msg="output is not a list")    
    def test__if_value_empty(self):
        self.assertTrue(get_prime_numbers(10) != None)

    def test_output_positive(self):
        result=get_prime_numbers(10)
        for i in result:
            self.assertTrue(i>0)