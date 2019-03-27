import argparse

arg_parser = argparse.ArgumentParser()
arg_parser.add_argument('--input', '-i', type=str, required=True)
arg_parser.add_argument('--output', '-o', type=str, required=True)
args = arg_parser.parse_args()

with open(args.output, 'w', encoding="utf8") as o:
    with open(args.input, 'r', encoding="utf8") as f:
        for line in f:
            line = line[3:line.index('\t')]
            line = line[1:-1]

            assertion = line.split(',')

            o.write('<{}> <{}> <{}> .\n'.format(assertion[1][:-1], assertion[0][:-1], assertion[2][:-1]))
