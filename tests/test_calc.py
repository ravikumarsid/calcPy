import sys
import io
sys.path.append("..")
from calc.calculator import *
import unittest, pytest
import argparse
import unittest.mock
import HtmlTestRunner
from logger.custom_logger import customLogger


class ErrorRaisingArgumentParser(argparse.ArgumentParser):
    def error(self, message):
        raise ValueError(message)


class TestCalculatorCommandLine(unittest.TestCase):

    log = customLogger(logging.DEBUG)

    @classmethod
    def setUp(self):
        # self.parser = create_parser()
        self.parser = ErrorRaisingArgumentParser()

        self.parser.add_argument("--sum", help="adds the two numbers specified", type=int, nargs=2)
        self.parser.add_argument("--sub", help="adds the two numbers specified", type=int, nargs=2)
        self.parser.add_argument("--mul", help="adds the two numbers specified", type=int, nargs=2)
        self.parser.add_argument("--div", help="adds the two numbers specified", type=float, nargs=2)
        self.parser.add_argument("--root", help="adds the two numbers specified", type=int, nargs=1)
        self.parser.add_argument("--mean", help="adds the two numbers specified", type=float, nargs=2)
        self.parser.add_argument("--range", help="adds the two numbers specified", type=int, nargs=2)

        self.args = self.parser.parse_args()
        self.arg_dict = vars(self.args)

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def assert_stdout(self,args, arg_dict, expected_output, mock_stdout):
        calculate(args, arg_dict)
        self.assertIn(mock_stdout.getvalue(), expected_output)

    def test_sum_invalid_input(self):
        args = ['--sum', 'A', '1']
        with self.assertRaises(ValueError) as cm:
            self.parser.parse_known_args(args)

        print('msg', cm.exception)
        self.assertIn("argument --sum: invalid int value: ", str(cm.exception))
        TestCalculatorCommandLine.log.debug('test for sum with invalid inputs message')

    def test_sum_invalid_number_arguments_0(self):
        args = ['--sum']
        with self.assertRaises(ValueError) as cm:
            self.parser.parse_known_args(args)

        print('msg', cm.exception)
        self.assertIn("argument --sum: expected 2 arguments", str(cm.exception))
        TestCalculatorCommandLine.log.debug('test for sum with zero input arguments')

    def test_sum_invalid_number_arguments_1(self):
        args = ['--sum', '54']
        with self.assertRaises(ValueError) as cm:
            self.parser.parse_known_args(args)

        print('msg', cm.exception)
        self.assertIn("argument --sum: expected 2 arguments", str(cm.exception))
        TestCalculatorCommandLine.log.debug('test for sum with one input argument')

    def test_sum_valid_input(self):
        args = ['--sum', '1', '5']
        parsed = self.parser.parse_args(args)
        arg_dict = vars(parsed)
        self.assert_stdout(parsed, arg_dict, "Sum of 1 and 5 is: 6\n" )

        TestCalculatorCommandLine.log.debug('test for sum with valid inputs message')

    def test_sub_invalid_input(self):
        args = ['--sub', '1', '17.0']
        with self.assertRaises(ValueError) as cm:
            self.parser.parse_known_args(args)

        print('msg', cm.exception)
        self.assertIn("argument --sub: invalid int value: ", str(cm.exception))
        TestCalculatorCommandLine.log.debug('test for subtraction with invalid inputs')

    def test_sub_valid_input(self):
        args = ['--sub', '8', '-9']
        parsed = self.parser.parse_args(args)
        arg_dict = vars(parsed)
        self.assert_stdout(parsed, arg_dict, "Difference between 8 and -9 is: 17\n" )

        TestCalculatorCommandLine.log.debug('test for subtraction with valid inputs')

    def test_mul_invalid_input(self):
        args = ['--mul', '__', '1']
        with self.assertRaises(ValueError) as cm:
            self.parser.parse_known_args(args)

        print('msg', cm.exception)
        self.assertIn("argument --mul: invalid int value: ", str(cm.exception))
        TestCalculatorCommandLine.log.debug('test for multiplcation with invalid inputs')

    def test_mul_valid_input(self):
        args = ['--mul', '12', '8']
        parsed = self.parser.parse_args(args)
        arg_dict = vars(parsed)
        self.assert_stdout(parsed, arg_dict, "Product of 12 and 8 is: 96\n" )

        TestCalculatorCommandLine.log.debug('test for multiplication with valid inputs')

    def test_div_invalid_input(self):
        args = ['--mul', '__', '1']
        with self.assertRaises(ValueError) as cm:
            self.parser.parse_known_args(args)

        print('msg', cm.exception)
        self.assertIn("argument --mul: invalid int value: ", str(cm.exception))
        TestCalculatorCommandLine.log.debug('test for multiplcation with invalid inputs')

    def test_div_valid_input(self):
        args = ['--div', '8', '9']
        parsed = self.parser.parse_args(args)
        arg_dict = vars(parsed)
        self.assert_stdout(parsed, arg_dict, "The result of divison of 8.0 and 9.0 is: 0.89\n" )
        TestCalculatorCommandLine.log.debug('test for division with valid inputs')

    def test_root_invalid_input(self):
        args = ['--root', 'C']
        with self.assertRaises(ValueError) as cm:
            self.parser.parse_known_args(args)

        print('msg', cm.exception)
        self.assertIn("argument --root: invalid int value: ", str(cm.exception))
        TestCalculatorCommandLine.log.debug('test for root with invalid input')

    def test_root_valid_input(self):
        args = ['--root', '15']
        parsed = self.parser.parse_args(args)
        arg_dict = vars(parsed)
        self.assert_stdout(parsed, arg_dict, "Square root of 15 is: 3.87\n")
        TestCalculatorCommandLine.log.debug('test for root with valid input')

    def test_mean_invalid_input(self):
        args = ['--mean', '1', '_O']
        with self.assertRaises(ValueError) as cm:
            self.parser.parse_known_args(args)

        print('msg', cm.exception)
        self.assertIn("argument --mean: invalid float value: ", str(cm.exception))
        TestCalculatorCommandLine.log.debug('test for mean with invalid input')

    def test_mean_valid_input(self):
        args = ['--mean', '18.5', '17.9']
        parsed = self.parser.parse_args(args)
        arg_dict = vars(parsed)
        self.assert_stdout(parsed, arg_dict, "Mean of 18.5 and 17.9 is: 18.2\n")
        TestCalculatorCommandLine.log.debug('test for mean with valid input')

    def test_range_invalid_input(self):
        args = ['--range', 'k', 'l']
        with self.assertRaises(ValueError) as cm:
            self.parser.parse_known_args(args)

        print('msg', cm.exception)
        self.assertIn("argument --range: invalid int value: ", str(cm.exception))
        TestCalculatorCommandLine.log.debug('test for range with invalid input')

    def test_range_valid_input(self):
        args = ['--range', '1', '5']
        parsed = self.parser.parse_args(args)
        arg_dict = vars(parsed)
        self.assert_stdout(parsed, arg_dict, "Range of numbers between 1 and 5 is: [2, 3, 4]\n")
        TestCalculatorCommandLine.log.debug('test for range with valid input')

if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='html_dir'))