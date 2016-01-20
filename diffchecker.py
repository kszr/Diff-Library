"""
Different ways of measuring diffs between files.
"""

from difflib import SequenceMatcher
import sys

"""
Returns the binary diff between two files as a ratio.
file1 is assumed to be the original version of the file, and 
file2 is assumed to be a modified version of file1.
From the documentation for SequenceMatcher:


From: http://stackoverflow.com/a/1334758
"""
def binaryDiff(file1, file2):
    try:
        text1 = open(file1).read()
        text2 = open(file2).read()
        m = SequenceMatcher(None, text1, text2)
        return m.ratio()
    except IOError as e:
        print "I/O error({0}): {1}".format(e.errno, e.strerror)

"""
@TODO: Implement this.
"""
def efficientDiff(file1, file2):
    return None

def main():
    if(len(sys.argv) != 4 and len(sys.argv) != 3):
        print "Usage: python diffchecker.py [file1] [file2] ([binaryDiff | efficientDiff])"
        exit(1)

    file1 = str(sys.argv[1])
    file2 = str(sys.argv[2])
    diffMethod = binaryDiff

    function_dict = {'binaryDiff' : binaryDiff,
                     'efficientDiff' : efficientDiff}
    if(len(sys.argv) == 4):
        diffMethodString = sys.argv[3]
        try:
            diffMethod = function_dict[diffMethodString]
        except KeyError:
            raise ValueError('invalid input')

    print diffMethod(file1, file2)


if __name__ == "__main__":
    main()
