"""
Different ways of measuring diffs between files.
"""

from difflib import SequenceMatcher
import sys

"""
Returns the binary diff between two files.
The ratio is basically (2*number of simiarlties)/(total number of elements in both files).
By inspection, it turns out that this takes into account things like alignment of common chunks
of text or whatever, meaning this might just turn out to be more like the "efficientDiff" we envisioned
than previously thought.
From: http://stackoverflow.com/a/1334758
"""
def binaryDiff(file1, file2, function="normal"):
    try:
        text1 = open(file1).read()
        text2 = open(file2).read()
        m = SequenceMatcher(None, text1, text2)
        # return m.ratio()
        function_dict = {"normal" : m.ratio,
                        "quick" : m.quick_ratio}
        return function_dict[function]()
    except IOError as e:
        print "I/O error({0}): {1}".format(e.errno, e.strerror)

"""
@TODO: Implement this.
What is this supposed to do anyway?
"""
def efficientDiff(file1, file2):
    return None

"""
This will probably never be implemented, because it has different
interpretations for different files. Just defining it here to distinguish
it from efficient diff.
"""
def logicalDiff(file1, file2):
    return None

def main():
    if(len(sys.argv) > 5 or len(sys.argv) < 3):
        print "Usage: python diffchecker.py [file1] [file2] ([binaryDiff | efficientDiff]) ([normal | quick])"
        exit(1)

    file1 = str(sys.argv[1])
    file2 = str(sys.argv[2])
    diffMethod = binaryDiff
    speed = "normal"

    function_dict = {"binaryDiff" : binaryDiff,
                     "efficientDiff" : efficientDiff}
    if len(sys.argv) >= 4:
        diffMethodString = sys.argv[3]
        try:
            diffMethod = function_dict[diffMethodString]
            if len(sys.argv) == 5:
                speed = sys.argv[4]
        except KeyError:
            diffMethod = binaryDiff
            speed = sys.argv[3]

    print diffMethod(file1, file2, speed)


if __name__ == "__main__":
    main()

