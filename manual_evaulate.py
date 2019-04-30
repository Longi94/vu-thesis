import os
import argparse
import random

parser = argparse.ArgumentParser()
parser.add_argument('--input', '-i', type=str, required=True)
parser.add_argument('--count', '-c', type=int, default=100)
args = parser.parse_args()

positive = 0
negative = 0

with open(args.input, 'r', encoding="utf8") as f:
    lines = set(f.readlines())

lines = random.sample(lines, args.count)

for line in lines:
    result = input(line + ' ')
    if result == '0':
        negative += 1
    else:
        positive += 1

print('Accuracy: {}'.format(positive / (positive + negative)))
