def consume(filename):
    chars = 0
    words = 0
    lines = 0

    with open(filename, 'rt') as fp:
        for line in fp:
            lines += 1
            words += len(line.strip().split())
            chars += len(line)

    return chars, words, lines

def daaaangerous(param=0):
    print("I'm the most dangerous function West of the Missippi, no test "\
          "will cover me!")
    return 3 / param
