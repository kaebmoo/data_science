# Python program to demonstrate
# command line arguments


import argparse


# Initialize parser
parser = argparse.ArgumentParser()

# Adding optional argument
# parser.add_argument("-o", "--Output", help = "Show Output")
parser.add_argument("File", metavar="revenue file", type=str, help="Input file")
# Read arguments from command line
args = parser.parse_args()
print(args)
input_file = args.File

if args.File:
    print("Displaying Output as: % s" % args.File)
    print("Input file %s" % input_file)
