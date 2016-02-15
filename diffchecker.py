"""
Different ways of measuring diffs between files.

Be sure to have bsdiff installed: http://starship.python.net/crew/atuining/cx_bsdiff/index.html
"""

import argparse
import bsdiff
from difflib import SequenceMatcher
import os
import sys

"""
Returns the binary diff between two files.
The ratio is basically (2*number of simiarlties)/(total number of elements in both files).
By inspection, it turns out that this takes into account things like alignment of common chunks
of text or whatever, meaning this might just turn out to be more like the "efficientDiff" we envisioned
than previously thought.
From: http://stackoverflow.com/a/1334758
"""
def binaryDiff(file1, file2, speed="normal"):
    try:
        text1 = open(file1).read()
        text2 = open(file2).read()
        m = SequenceMatcher(None, text1, text2)

        function_dict = {"normal" : m.ratio,
                        "quick" : m.quick_ratio}
        return function_dict[speed]()
    except IOError as e:
        print "I/O error({0}): {1}".format(e.errno, e.strerror)

def binaryDiff2(file1, file2):
    try:
        text1 = open(file1).read()
        text2 = open(file2).read()
        
        return 2.0*len(bsdiff.Diff(text1, text2)[1])/(len(text1) + len(text2))
    except IOError as e:
        print "I/O error({0}): {1}".format(e.errno, e.strerror)

"""
@TODO: Implement this, maybe.
"""
def efficientDiff(file1, file2, speed="normal"):
    return None

def argument_init():
    parser = argparse.ArgumentParser()
    parser.add_argument("experiment", default="binary", choices=["binary", "binary2", "efficient"], help="A experiment scenario to run")
    parser.add_argument("-q", "--quick", action="store_true", help="A quick estimate of differences")
    parser.add_argument("-f", "--files", nargs=2, required=True, help="The two files to compare")

    return parser.parse_args()

"""
This will probably never be implemented, because it has different
interpretations for different files. Just defining it here to distinguish
it from efficient diff.
"""
def logicalDiff(file1, file2):
    return None

def main():
    args = argument_init()

    experiment = args.experiment
    quick = args.quick
    files = args.files

    function_dict = {'binary' : binaryDiff,
                     'binary2': binaryDiff2,
                     'efficient' : efficientDiff}
    diffMethod = function_dict[experiment]

    if quick:
        print diffMethod(files[0], files[1], "quick")
    else:
        print diffMethod(files[0], files[1])

    print "File 1 size:", str(os.stat(files[0]).st_size), "B\nFile 2 size:", str(os.stat(files[1]).st_size), "B"

if __name__ == "__main__":
    main()
