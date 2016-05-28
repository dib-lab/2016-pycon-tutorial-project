======================
Command line interface
======================

The command line interface to ``wordcount`` is as follows::

  wordcount [ file1 [ ... ] ]

The output is three tab-delimited nubmers -- the total number of
characters (including whitespace), the total number of
whitespace-delimited words, and the total number of lines -- followed
by a count of the number of files consumed.

For example, if you execute::

  ../wordcount example.txt

in the ``doc/`` subdirectory, you will get the output::

   67      13      3       in 1 files
