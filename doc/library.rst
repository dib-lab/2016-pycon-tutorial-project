=================
Library functions
=================

The ``wordcount_lib`` module can be imported, and has one function,
``consume(filename)``.  The function returns a 3-tuple of the
number of characters, words, and lines.

Example usage::

  >>> import wordcount_lib
  >>> chars, words, lines = wordcount_lib.consume('example.txt')
  >>> print(chars, words, lines)
  67 13 3
