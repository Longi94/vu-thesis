import argparse
import random

parser = argparse.ArgumentParser()
parser.add_argument('--input', '-i', type=str, required=True)
parser.add_argument('--count', '-c', type=int, default=100)
args = parser.parse_args()

evaluations = {}

with open(args.input, 'r', encoding="utf8") as f:
    lines = set(f.readlines())

lines = random.sample(lines, args.count)

for line in lines:
    result = input(line + ' ')

    if result not in evaluations:
        evaluations[result] = 1
    else:
        evaluations[result] += 1

for key, value in evaluations.items():
    print('{} {}'.format(key, value / args.count))
