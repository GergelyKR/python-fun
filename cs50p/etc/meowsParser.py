# With this module, we can automate the parsing of command line arguments

import argparse

parser = argparse.ArgumentParser(description="Meow like a cat")
parser.add_argument("-n", default=1,help="Number of times to meow", type=int)
args = parser.parse_args()

for _ in range(int(args.n)):
    print("meow")