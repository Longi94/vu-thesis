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

            if not assertion[1].startswith('/c/en/'):
                continue

            if assertion[0] != '/r/ExternalURL/' and not assertion[2].startswith('/c/en/'):
                # skip non english ones
                continue

            if assertion[0] == '/r/ExternalURL/' and assertion[2].startswith('/http'):
                # remove leading slash from links
                assertion[2] = assertion[2][1:]

            o.write('<{}> <{}> <{}> .\n'.format(assertion[1][:-1], assertion[0][:-1], assertion[2][:-1]))
