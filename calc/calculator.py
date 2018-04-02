import argparse
import math
import inspect
import logging

def add(arg1, arg2):
    return arg1 + arg2

def subtract(arg1, arg2):
    return arg1 - arg2

def multiply(arg1, arg2):
    return arg1 * arg2

def division(arg1, arg2):
    if arg2 == 0:
        result = "Divison by zero is not possible. Please enter another number."
        return result
    else:
        result = arg1 / arg2
        return result

def square_root(arg1):
    return math.sqrt(arg1)

def mean(arg1, arg2):
    return (arg1 + arg2) / 2

def print_range(arg1, arg2):
    res = []
    for num in range(min(arg1, arg2)+ 1, max(arg1, arg2)):
        res.append(num)
    return res

def calculate(args, arg_dict):
    if args.sum:
        val1 = arg_dict.get('sum')[0]
        val2 = arg_dict.get('sum')[1]
        print("Sum of {} and {} is: {}".format(val1, val2, (add(val1, val2))))

    elif args.sub:
        val1 = arg_dict.get('sub')[0]
        val2 = arg_dict.get('sub')[1]
        print("Difference between {} and {} is: {}".format(val1, val2, (subtract(val1, val2))))

    elif args.mul:
        val1 = arg_dict.get('mul')[0]
        val2 = arg_dict.get('mul')[1]
        print("Product of {} and {} is: {}".format(val1, val2, (multiply(val1, val2))))

    elif args.div:
        val1 = arg_dict.get('div')[0]
        val2 = arg_dict.get('div')[1]
        print("The result of divison of {} and {} is: {}".format(val1, val2, "{0:.2f}".format(division(val1, val2))))

    elif args.root:
        val1 = arg_dict.get('root')[0]
        print("Square root of {} is: {}".format(val1, "{0:.2f}".format(square_root(val1))))

    elif args.mean:
        val1 = arg_dict.get('mean')[0]
        val2 = arg_dict.get('mean')[1]
        print("Mean of {} and {} is: {}".format(val1, val2, (mean(val1, val2))))

    elif args.range:
        val1 = arg_dict.get('range')[0]
        val2 = arg_dict.get('range')[1]
        print("Range of numbers between {} and {} is: {}".format(val1, val2, (print_range(val1, val2))))

def create_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument("--sum", help="adds the two numbers specified", type=int, nargs=2)
    parser.add_argument("--sub", help="adds the two numbers specified", type=int, nargs=2)
    parser.add_argument("--mul", help="adds the two numbers specified", type=int, nargs=2)
    parser.add_argument("--div", help="adds the two numbers specified", type=float, nargs=2)
    parser.add_argument("--root", help="adds the two numbers specified", type=int, nargs=1)
    parser.add_argument("--mean", help="adds the two numbers specified", type=float, nargs=2)
    parser.add_argument("--range", help="adds the two numbers specified", type=int, nargs=2)

    return parser

def main():
    parser = create_parser()
    args = parser.parse_args()
    arg_dict = vars(args)
    calculate(args, arg_dict)

if __name__ == '__main__':
    main()