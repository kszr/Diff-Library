# Diff-Library
A diff library of sorts. Key phrase: "of sorts".

Usage: ```python diffchecker.py [filename1] [filename2] ([binaryDiff | efficientDiff])```

* Assumes filename1 is the original version of the file and filename2 is a modified version.
* Returns the diff between these files as a ratio.
* Default third argument is binaryDiff, which does a diff between the two sequences (files) without looking at things like alignment.
  * Another possible third argument is efficientDiff, which is as yet unimplemented, and, as the name suggests, highly efficient.
