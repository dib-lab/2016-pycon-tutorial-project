import os.path
import tempfile

import wordcount_lib

def _make_testfile(filename, data):
    "Make a temp file containing the given data; return full path to file."
    
    tempdir = tempfile.mkdtemp(prefix='wordcounttest_')
    testfile = os.path.join(tempdir, filename)

    with open(testfile, 'wt') as fp:
        fp.write(data)

    return testfile


def test_consume_1():
    # do a basic test of the consume function.
    testfile = _make_testfile('sometext.txt', 'a b cc\nddd')
    chars, words, lines = wordcount_lib.consume(testfile)

    assert chars == 10
    assert words == 4
    assert lines == 2


def test_consume_2():
    # do another basic test of the consume function.
    testfile = _make_testfile('sometext.txt', 'a\nb\ncc\nddd\ne')
    chars, words, lines = wordcount_lib.consume(testfile)

    assert chars == 12                    # includes whitespace in char count
    assert words == 5
    assert lines == 5
    
def test_consume_3():
    # check something tricky: whitespace at beginning & end of line
    testfile = _make_testfile('sometext.txt', ' a b c ')
    chars, words, lines = wordcount_lib.consume(testfile)

    assert chars == 7                     # includes whitespace in char count
    assert words == 3
    assert lines == 1
    
