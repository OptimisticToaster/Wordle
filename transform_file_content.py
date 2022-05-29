#!/usr/bin/env python3

import sys

in_file = 'word_list.txt'
out_file = 'word_list-out.txt'


def main(args):

    # Open the out_file
    out = open(out_file, 'w')

    # Read in files
    with open(in_file) as fh:
        # Step through each line
        for line in fh:
            # Manipulate the text as appropriate and write to out_file
            out.write(line.upper())
    out.close()

if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
