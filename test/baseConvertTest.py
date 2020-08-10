import unittest
import baseConvert as BaseConvertClass


class BaseConvertTestCase(unittest.TestCase):

    def setUp(self):
        self.binBase = 2
        self.otcBase = 8
        self.hexBase = 16

    def tearDown(self):
        self.binBase = None
        self.otcBase = None
        self.hexBase = None

    def test_1_baseConverter_BtoH(self):
        expected = '1100'
        input_decimal = 10
        actual = BaseConvertClass.base_converter(input_decimal, self.binBase)
        self.assertEqual(expected, actual)

    def test_2_baseConverter_None(self):
        input_decimal = None
        base = None

        with self.assertRaises(Exception) as context:
            BaseConvertClass.base_converter(input_decimal, base)

        self.assertTrue('The input decimal or base is invalidate.' in str(context.exception))

    def test_3_test_2_baseConverter_lessthanone(self):
        input_decimal = -10
        base = 0

        with self.assertRaises(Exception) as context:
            BaseConvertClass.base_converter(input_decimal, base)

        self.assertTrue('The input decimal or base is less than 0' in str(context.exception))

if __name__ == '__main__':

    suite = (unittest.TestLoader().loadTestsFromTestCase(BaseConvertTestCase))
    unittest.main(verbosity=2)

