import argparse
import random
import json

parser = argparse.ArgumentParser()
parser.add_argument('--input', '-i', type=str, required=True)
parser.add_argument('--count', '-c', type=int, default=100)
args = parser.parse_args()

evaluations = {}
csv_lines = []

with open(args.input, 'r', encoding="utf8") as f:
    lines = set(f.readlines())

lines = random.sample(lines, args.count)

for line in lines:
    result = input(line + ' ')
    csv_lines.append('{},{}'.format(result, line))

    if result not in evaluations:
        evaluations[result] = 1
    else:
        evaluations[result] += 1

for key, value in evaluations.items():
    print('{} {}'.format(key, value / args.count))

with open('{}.score.json'.format(args.input), 'w') as f:
    json.dump(evaluations, f)

with open('{}.evals.csv'.format(args.input), 'w') as f:
    f.writelines(csv_lines)
